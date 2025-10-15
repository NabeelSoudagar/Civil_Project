from PIL import Image
import numpy as np

# Load the image
img = Image.open('log-circle.jpg')

# Convert to RGBA if not already
if img.mode != 'RGBA':
    img = img.convert('RGBA')

# Get the image data as a numpy array
data = np.array(img)

# Define the black color range (adjust threshold as needed)
black_threshold = 50  # Pixels with RGB values below this are considered black

# Create a mask for black pixels
mask = (data[:, :, 0] < black_threshold) & (data[:, :, 1] < black_threshold) & (data[:, :, 2] < black_threshold)

# Set alpha channel to 0 for black pixels
data[mask, 3] = 0

# Create new image with transparency
transparent_img = Image.fromarray(data, 'RGBA')

# Save as PNG
transparent_img.save('log-circle.png')

print("Transparent logo saved as log-circle.png")
