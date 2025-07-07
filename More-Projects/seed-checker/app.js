let bip39Words = new Set();

fetch("bip39_english.txt")
  .then(res => res.text())
  .then(data => {
    bip39Words = new Set(data.trim().split("\n"));
  });

const dropZone = document.getElementById("drop-zone");
const result = document.getElementById("result");

dropZone.addEventListener("dragover", (e) => {
  e.preventDefault();
  dropZone.classList.add("hover");
});

dropZone.addEventListener("dragleave", () => {
  dropZone.classList.remove("hover");
});

dropZone.addEventListener("drop", (e) => {
  e.preventDefault();
  dropZone.classList.remove("hover");

  const file = e.dataTransfer.files[0];
  if (!file.name.endsWith(".txt")) {
    result.innerHTML = "<span class='invalid'>🧿 This file lacks cursed energy</span>";
    return;
  }

  const reader = new FileReader();
  reader.onload = () => {
    const text = reader.result.trim().toLowerCase();
    const words = text.split(/\s+/);

    if (words.length < 12 || words.length > 24) {
      result.innerHTML = `<span class='invalid'>🚫 Domain Rejected: ${words.length} words</span>`;
      return;
    }

    const invalidWords = words.filter(w => !bip39Words.has(w));
    if (invalidWords.length > 0) {
      result.innerHTML = `<span class='invalid'>👁️ Cursed Words Detected:<br>${invalidWords.join(", ")}</span>`;
    } else {
      result.innerHTML = `<span class='valid'>✅ Domain Expansion: Phrase Stable!</span>`;
    }
  };
  reader.readAsText(file);
});

