from PIL import Image

def bin_to_str(b):
    chars = [chr(int(b[i:i+8], 2)) for i in range(0, len(b), 8)]
    return ''.join(chars)

def extract_hash_from_image(image_path, hash_len=64):
    img = Image.open(image_path)
    img = img.convert('RGB')
    pixels = img.load()

    width, height = img.size
    total_bits = hash_len * 8
    bits = ""
    i = 0

    for y in range(height):
        for x in range(width):
            if i >= total_bits:
                break
            r, g, b = pixels[x, y]
            bits += str(r & 1)
            i += 1

    recovered_hash = bin_to_str(bits)
    print(f" Recovered hash: {recovered_hash}")

if __name__ == "__main__":
    extract_hash_from_image("bird_hashed.png")

