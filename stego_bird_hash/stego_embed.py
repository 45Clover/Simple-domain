from PIL import Image
import hashlib

def text_to_hash(text):
    return hashlib.sha256(text.encode()).hexdigest()

def str_to_bin(s):
    return ''.join(format(ord(c), '08b') for c in s)

def embed_hash_into_image(input_text_path, base_image_path, image_out_path):
    with open(input_text_path, 'r') as f:
        text = f.read()
    hash_str = text_to_hash(text)
    binary = str_to_bin(hash_str)

    img = Image.open(base_image_path)
    img = img.convert('RGB')
    pixels = img.load()

    width, height = img.size
    required_pixels = len(binary)
    if required_pixels > width * height:
        raise ValueError("Image is too small to hold the hash.")

    i = 0
    for y in range(height):
        for x in range(width):
            if i >= len(binary):
                break
            r, g, b = pixels[x, y]
            r = (r & ~1) | int(binary[i])
            pixels[x, y] = (r, g, b)
            i += 1

    img.save(image_out_path)
    print(f" Hash embedded into {image_out_path}")

if __name__ == "__main__":
    embed_hash_into_image("bird_migration.txt", "bird.png", "bird_hashed.png")

