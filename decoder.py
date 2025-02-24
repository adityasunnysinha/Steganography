import cv2
import os

image_path = r"C:\Users\Aditya Sinha\Desktop\ibm project stego\Stenography-main\encryptedImage.png"

if not os.path.exists(image_path):
    print(f"Error: Encrypted image '{image_path}' not found!")
    exit()

img = cv2.imread(image_path)
if img is None:
    print("Error: Could not read the encrypted image file.")
    exit()

password_attempt = input("Enter passcode for decryption: ")
original_password = input("Re-enter the original passcode to verify: ")

if password_attempt != original_password:
    print("❌ Incorrect passcode! Access denied.")
    exit()

n, m, z = 0, 0, 0
msg_length_str = ""

for _ in range(4):
    pixel_value = img[n, m, z]
    if 48 <= pixel_value <= 57:  # Check if it's a digit (0-9)
        msg_length_str += chr(pixel_value)
    else:
        print("❌ Error: Invalid message length. Image may be corrupted or incorrectly encoded.")
        exit()
    z = (z + 1) % 3
    if z == 0:
        m += 1
    if m == img.shape[1]:
        m = 0
        n += 1

try:
    msg_length = int(msg_length_str)
except ValueError:
    print("❌ Error: Could not convert message length to an integer.")
    exit()

message = ""

for _ in range(msg_length):
    pixel_value = img[n, m, z]
    if 0 <= pixel_value <= 255:  # Ensure valid ASCII range
        message += chr(pixel_value)
    else:
        print("❌ Error: Unexpected character in message. Image may be corrupted.")
        exit()
    z = (z + 1) % 3
    if z == 0:
        m += 1
    if m == img.shape[1]:
        m = 0
        n += 1

print(f"🔓 Decrypted Message: {message}")
