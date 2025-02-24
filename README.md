Overview

This project implements image steganography using the Least Significant Bit (LSB) encoding method to hide and retrieve secret messages within an image. The approach ensures secure and discreet communication by embedding messages without altering the visual appearance of the image.

Features

-Message Encryption: Hide text inside an image using LSB encoding.

-Message Decryption: Retrieve hidden text from an encrypted image.

-Password Protection: Secure the hidden message with a user-defined passcode.

-Preserved Image Quality: Embeds messages without significant visual distortion.

-Cross-Platform Support: Works on Windows and can be adapted for Linux/macOS.

Technologies Used:

-Programming Language: Python

-Libraries: OpenCV (cv2) for image processing, OS for file management

Installation:

1.Clone the repository:
-https://github.com/adityasunnysinha/Steganography

2.Install the required packages:
-pip install opencv-python numpy



Usage:

1.Encoding (Hiding a Message)

-Place the image (e.g., pic.png) in the same directory.

-Run the encoder script:

-python encoder.py

-Enter the secret message and a passcode when prompted.

-The encrypted image (encryptedImage.png) will be saved in the same folder.

2.Decoding (Retrieving a Message)

-Ensure encryptedImage.jpg is in the same directory.

-Run the decoder script:

-python decoder.py

-Enter the correct passcode to decrypt the message.

-The hidden message will be displayed on the screen.


File Structure:

📂 steganography
 ├── encoder.py    # Script to hide a message in an image
 ├── decoder.py    # Script to extract the hidden message
 ├── mypic.jpg     # Original image (example)
 ├── encryptedImage.jpg # Output encrypted image
 ├── README.md     # Project documentation


 Future Enhancements:

-Implement stronger encryption for enhanced security.

-Expand support to audio, video, and document files.

-Develop a web or mobile app for easy usage.

Contributing:

-Contributions are welcome! Feel free to fork this repository, improve the code, and submit pull requests.

License:

-This project is licensed under the MIT License.
