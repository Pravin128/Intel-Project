import cv2

def is_blurred(image, threshold=100):
    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Compute the Laplacian
    laplacian = cv2.Laplacian(gray, cv2.CV_64F)
    
    # Compute the variance of the Laplacian
    variance = laplacian.var()
    
    # Determine if the image is blurred based on the threshold
    if variance < threshold:
        return True
    else:
        return False

# Load the image
image = cv2.imread('Sample_Images/girl.jpg')

# Check if the image is blurred
if is_blurred(image):
    print("Image is blurred.")
else:
    print("Image is not blurred.")
