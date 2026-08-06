import cv2

# Load the image
img = cv2.imread('C:/Users/jagan/OneDrive/Documents/testpaper.jpeg')

# Check if it loaded correctly
if img is None:
    print("Error: Image not found or path is wrong")
else:
    print("Image loaded successfully, size:", img.shape)

    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Resize (optional, makes processing faster/consistent)
    resized = cv2.resize(gray, (800, 1000))

    # Save the processed image to check the result
    cv2.imwrite('C:/Users/jagan/OneDrive/Documents/testpaper.jpeg', resized)
    print("Processed image saved!")