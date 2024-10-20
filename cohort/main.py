import cv2
import pytesseract
import matplotlib.pyplot as plt

# Set the path for Tesseract executable (change this path if necessary)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Load the image
image = cv2.imread("sample.jpeg")

# Check if the image was loaded successfully
if image is None:
    print("Error: Could not load image.")
    exit()

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Gaussian Blur
blurred = cv2.GaussianBlur(gray, (5, 5), 0)

# Apply thresholding to the image
thresh = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

# Perform OCR on the thresholded image
text = pytesseract.image_to_string(thresh)

# Print the raw OCR output
print("OCR Output:")
print(text)

# Split the text into lines
lines = text.strip().splitlines()

# Create a dictionary to store the headers and their corresponding content
output_dict = {}

# Initialize a variable to hold the current header
current_header = None

# Iterate over the lines and extract the headers and content
for line in lines:
    line = line.strip()  # Clean up any leading/trailing whitespace
    # Check if the line is a header
    if line.endswith(":"):
        current_header = line[:-1].strip()  # Remove ':' and clean up
    # If a header is present, add the content to the dictionary
    elif current_header and line:
        output_dict[current_header] = line.strip()  # Clean the content

# Print the output dictionary
print("Output Dictionary:")
print(output_dict)

# Display the images using Matplotlib
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.title('Grayscale Image')
plt.imshow(gray, cmap='gray')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title('Thresholded Image')
plt.imshow(thresh, cmap='gray')
plt.axis('off')

plt.show()
