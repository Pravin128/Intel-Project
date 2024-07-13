import cv2
import numpy as np
import os
import argparse

# Function to process an image
def process_image(input_image_path, output_image_path):
    # Read the image
    image = cv2.imread(input_image_path)

    # Check if the image was successfully loaded
    if image is None:
        print(f"Failed to load image from {input_image_path}")
        return

    # Step 1: Sharpen the image - unsharp masking
    blurred = cv2.GaussianBlur(image, (21, 21), 0)
    sharpened = cv2.addWeighted(image, 1.5, blurred, -0.5, 0)

    # Step 2: Denoise the sharpened image
    denoised_sharpened_image = cv2.fastNlMeansDenoisingColored(sharpened, None, 8, 8, 5, 19)

    # Step 3: Apply median blur to further reduce noise
    final_image = cv2.medianBlur(denoised_sharpened_image, 5)

    # Save the final image
    cv2.imwrite(output_image_path, final_image)
    print(f"Denoised, sharpened, and median blurred image saved to {output_image_path}")

# Main function to handle command-line arguments and process images
def main(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        input_image_path = os.path.join(input_folder, filename)
        output_image_path = os.path.join(output_folder, f"processed_{filename}")

        process_image(input_image_path, output_image_path)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process images by sharpening, denoising, and applying median blur.")
    parser.add_argument('input_folder', type=str, help='Path to the input folder containing images')
    parser.add_argument('output_folder', type=str, help='Path to the output folder to save processed images')
    args = parser.parse_args()

    main(args.input_folder, args.output_folder)
