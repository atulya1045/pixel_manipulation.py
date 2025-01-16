from PIL import Image

def encrypt_image(image_path, key, output_path):
    # Open the image
    img = Image.open(image_path)
    pixels = img.load()  # Access pixel data
    width, height = img.size

    # Encrypt the image
    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]
            # Apply encryption using the key
            pixels[x, y] = (
                (r + key) % 256,
                (g + key) % 256,
                (b + key) % 256,
            )

    # Save the encrypted image
    img.save(output_path)
    print(f"Image encrypted and saved as {output_path}")

def decrypt_image(image_path, key, output_path):
    # Open the image
    img = Image.open(image_path)
    pixels = img.load()  # Access pixel data
    width, height = img.size

    # Decrypt the image
    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]
            # Apply decryption using the key
            pixels[x, y] = (
                (r - key) % 256,
                (g - key) % 256,
                (b - key) % 256,
            )

    # Save the decrypted image
    img.save(output_path)
    print(f"Image decrypted and saved as {output_path}")

print("*** IMAGE ENCRYPTION PROGRAM ***")
print()

print("Do you want to encrypt or decrypt an image?")
user_input = input("e/d: ").lower()
print()

if user_input == "e":
    print("ENCRYPTION MODE SELECTED")
    print()
    input_image = input("Enter the path of the image to encrypt: ")
    key = int(input("Enter the encryption key (1 to 255): "))
    output_image = input("Enter the path to save the encrypted image: ")
    encrypt_image(input_image, key, output_image)

elif user_input == "d":
    print("DECRYPTION MODE SELECTED")
    print()
    input_image = input("Enter the path of the encrypted image: ")
    key = int(input("Enter the decryption key (1 to 255): "))
    output_image = input("Enter the path to save the decrypted image: ")
    decrypt_image(input_image, key, output_image)