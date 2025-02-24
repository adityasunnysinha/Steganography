import cv2
import os

image_path = r"C:\Users\Aditya Sinha\Desktop\ibm project stego\Stenography-main\pic.png"

if not os.path.exists(image_path):
    print(f"Error: Image '{image_path}' not found!")
    exit()

img = cv2.imread(image_path)
if img is None:
    print("Error: Could not read the image file.")
    exit()

image_dir = os.path.dirname(image_path)

msg = input("Enter secret message: ")
password = input("Enter a passcode: ")

msg_length = len(msg)
if msg_length > 9999:
    print("❌ Error: Message too long! Maximum 9999 characters allowed.")
    exit()

msg = str(msg_length).zfill(4) + msg  # Prefix message with its length (4-digit string)

d = {chr(i): i for i in range(255)}

n, m, z = 0, 0, 0

for char in msg:
    img[n, m, z] = d[char]
    z = (z + 1) % 3
    if z == 0:
        m += 1
    if m == img.shape[1]:
        m = 0
        n += 1

output_path = os.path.join(image_dir, "encryptedImage.png")
cv2.imwrite(output_path, img)

if os.path.exists(output_path):
    print(f"✅ Encrypted image saved successfully at: {output_path}")
    os.system(f'start "" "{output_path}"')
else:
    print("❌ Error: Failed to save encrypted image.")
