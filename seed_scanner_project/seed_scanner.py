import os
import re
import shutil
import argparse
import logging
from pathlib import Path
from typing import Tuple, List, Set

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
logger = logging.getLogger(__name__)

class SeedPhraseSanitizer:
    def __init__(self, wordlist_path: str = "bip39_wordlist.txt"):
        self.bip39_words = self._load_wordlist(wordlist_path)
        # File extensions to process (text-based files)
        self.processable_extensions = {'.txt', '.md', '.py', '.js', '.json', '.log', '.csv', '.xml', '.html'}
    
    def _load_wordlist(self, wordlist_path: str) -> Set[str]:
        """Load BIP39 wordlist with error handling."""
        try:
            with open(wordlist_path, "r", encoding='utf-8') as f:
                words = set(f.read().splitlines())
            logger.info(f"Loaded {len(words)} words from BIP39 wordlist")
            return words
        except FileNotFoundError:
            logger.error(f"BIP39 wordlist not found at {wordlist_path}")
            raise
        except Exception as e:
            logger.error(f"Error loading wordlist: {e}")
            raise
    
    def _is_valid_seed_phrase(self, phrase: str) -> bool:
        """Check if a phrase is a valid BIP39 seed phrase."""
        words = phrase.strip().split()
        # Valid seed phrase lengths: 12, 15, 18, 21, 24 words
        if len(words) not in [12, 15, 18, 21, 24]:
            return False
        
        # Check if all words are in BIP39 wordlist
        return all(word.lower() in self.bip39_words for word in words)
    
    def _find_seed_phrases(self, content: str) -> Tuple[str, List[str]]:
        """Find and securely remove seed phrases from content."""
        # Pattern to match potential seed phrases (11-23 words + 1 final word)
        pattern = r'\b(?:\w+\s+){11,23}\w+\b'
        matches = re.findall(pattern, content, re.IGNORECASE)
        
        found_phrases = []
        sanitized_content = content
        
        for match in matches:
            candidate = match.strip()
            if self._is_valid_seed_phrase(candidate):
                # Replace with secure placeholder (no reversible information)
                replacement = "[REDACTED_SEED_PHRASE]"
                sanitized_content = sanitized_content.replace(candidate, replacement)
                found_phrases.append(f"Length: {len(candidate.split())} words")
                logger.warning(f"Found seed phrase with {len(candidate.split())} words")
        
        return sanitized_content, found_phrases
    
    def _is_processable_file(self, filepath: Path) -> bool:
        """Check if file should be processed based on extension."""
        return filepath.suffix.lower() in self.processable_extensions
    
    def _create_backup(self, filepath: Path) -> Path:
        """Create a backup of the original file."""
        backup_path = filepath.with_suffix(filepath.suffix + '.bak')
        counter = 1
        while backup_path.exists():
            backup_path = filepath.with_suffix(f'{filepath.suffix}.bak.{counter}')
            counter += 1
        
        shutil.copy2(filepath, backup_path)
        logger.info(f"Backup created: {backup_path}")
        return backup_path
    
    def process_file(self, filepath: Path, destructive: bool = False, backup: bool = True) -> bool:
        """Process a single file for seed phrases."""
        try:
            if not self._is_processable_file(filepath):
                logger.debug(f"Skipping non-processable file: {filepath}")
                return False
            
            # Read file content
            with open(filepath, "r", encoding='utf-8', errors='ignore') as f:
                content = f.read()
            
            # Find and sanitize seed phrases
            sanitized_content, found_phrases = self._find_seed_phrases(content)
            
            if found_phrases:
                logger.warning(f"Found {len(found_phrases)} seed phrase(s) in {filepath}")
                
                # Create backup if requested
                if backup:
                    self._create_backup(filepath)
                
                # Write sanitized content
                if destructive:
                    with open(filepath, "w", encoding='utf-8') as f:
                        f.write(sanitized_content)
                    logger.info(f"Seed phrases removed from: {filepath}")
                else:
                    output_path = filepath.with_suffix('.sanitized' + filepath.suffix)
                    with open(output_path, "w", encoding='utf-8') as f:
                        f.write(sanitized_content)
                    logger.info(f"Sanitized version saved to: {output_path}")
                
                return True
            else:
                logger.debug(f"No seed phrases found in {filepath}")
                return False
                
        except Exception as e:
            logger.error(f"Error processing {filepath}: {e}")
            return False
    
    def process_directory(self, directory: Path, destructive: bool = False, backup: bool = True) -> dict:
        """Process all files in a directory."""
        results = {"processed": 0, "found_phrases": 0, "errors": 0}
        
        for root, _, files in os.walk(directory):
            for file in files:
                filepath = Path(root) / file
                try:
                    if self.process_file(filepath, destructive, backup):
                        results["found_phrases"] += 1
                    results["processed"] += 1
                except Exception as e:
                    logger.error(f"Error processing {filepath}: {e}")
                    results["errors"] += 1
        
        return results
    
    def scan_target(self, target: str, destructive: bool = False, backup: bool = True) -> bool:
        """Main method to scan a file or directory."""
        target_path = Path(target)
        
        if not target_path.exists():
            logger.error(f"Target not found: {target}")
            return False
        
        if target_path.is_file():
            return self.process_file(target_path, destructive, backup)
        elif target_path.is_dir():
            results = self.process_directory(target_path, destructive, backup)
            logger.info(f"Processed {results['processed']} files, "
                       f"found seed phrases in {results['found_phrases']} files, "
                       f"{results['errors']} errors")
            return results["found_phrases"] > 0
        else:
            logger.error(f"Invalid target type: {target}")
            return False


def main():
    parser = argparse.ArgumentParser(
        description="Secure Seed Phrase Scanner and Sanitizer",
        epilog="WARNING: This tool will search for and remove cryptocurrency seed phrases. "
               "Always backup important files before running with --destructive flag."
    )
    parser.add_argument("target", help="Target file or directory to scan")
    parser.add_argument(
        "--destructive", 
        action="store_true", 
        help="Replace seed phrases in original files (DANGEROUS - creates permanent changes)"
    )
    parser.add_argument(
        "--no-backup", 
        action="store_true", 
        help="Skip creating backup files (not recommended)"
    )
    parser.add_argument(
        "--wordlist", 
        default="bip39_wordlist.txt",
        help="Path to BIP39 wordlist file (default: bip39_wordlist.txt)"
    )
    parser.add_argument(
        "--verbose", "-v",
        action="store_true",
        help="Enable verbose logging"
    )
    
    args = parser.parse_args()
    
    # Set logging level
    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)
    
    # Warn about destructive operations
    if args.destructive:
        response = input("WARNING: Destructive mode will permanently modify files. Continue? (y/N): ")
        if response.lower() != 'y':
            logger.info("Operation cancelled by user")
            return
    
    try:
        sanitizer = SeedPhraseSanitizer(args.wordlist)
        sanitizer.scan_target(args.target, args.destructive, not args.no_backup)
    except Exception as e:
        logger.error(f"Fatal error: {e}")
        return 1
    
    return 0


if __name__ == "__main__":
    exit(main())
