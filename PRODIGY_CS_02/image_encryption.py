from PIL import Image
import random
import os

def encrypt_image(image_path, output_path):
    img = Image.open(image_path)
    width, height = img.size
    pixels = img.load()

    # Create a shuffled list of indices
    indices = [(x, y) for x in range(width) for y in range(height)]
    random.shuffle(indices)

    # Save the indices of changed pixels for visualization
    with open("changed_pixels.txt", "w") as f:
        for x, y in indices:
            f.write(f"Pixel at ({x}, {y}) was changed.\n")

    encrypted_pixels = {index: pixels[x, y] for index, (x, y) in enumerate(indices)}

    encrypted_img = Image.new(img.mode, img.size)
    for index, color in encrypted_pixels.items():
        x, y = indices[index]
        encrypted_img.putpixel((x, y), color)

    encrypted_img.save(output_path)
    print(f"Image encrypted successfully. Encrypted image saved at: {output_path}")

def decrypt_image(image_path, output_path):
    img = Image.open(image_path)
    width, height = img.size
    pixels = img.load()

    # Load the indices of changed pixels
    indices = [(int(coords[0]), int(coords[1])) for coords in open("changed_pixels.txt")]

    decrypted_pixels = {index: pixels[x, y] for index, (x, y) in enumerate(indices)}

    decrypted_img = Image.new(img.mode, img.size)
    for index, color in decrypted_pixels.items():
        x, y = indices[index]
        decrypted_img.putpixel((x, y), color)

    decrypted_img.save(output_path)
    print(f"Image decrypted successfully. Decrypted image saved at: {output_path}")

# Usage
if __name__ == "__main__":
    current_directory = os.getcwd()
    input_image = os.path.join(current_directory, "kriti bby.jpg")
    encrypted_image = os.path.join(current_directory, "encrypted_image.jpg")
    decrypted_image = os.path.join(current_directory, "decrypted_image.jpg")

    print("Encrypting image...")
    encrypt_image(input_image, encrypted_image)

    print("\nDecrypting image...")
    decrypt_image(encrypted_image, decrypted_image)
