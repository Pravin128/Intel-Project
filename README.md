# Detect-Pixelated-Image-And-correct-It
This Python script processes images by sharpening, denoising, and applying median blur using OpenCV library functions.

## Description

The script performs the following steps on each image in the input folder:
1. **Sharpening**: Uses unsharp masking to enhance edges.
2. **Denoising**: Applies fast non-local means denoising to reduce noise.
3. **Median Blur**: Further reduces noise using median blur.

The processed images are saved in the specified output folder.

## Requirements

- Python 3.x
- OpenCV (`cv2`), numpy (`numpy`)

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/image-processing.git
    cd image-processing
    ```

2. Install required Python packages:
    ```bash
    pip install opencv-python numpy
    ```

## Usage

1. Navigate to the directory where the script is located.

2. Run the script with the following command, providing paths to your input and output folders:
    ```bash
    python image_processing.py path/to/input/folder path/to/output/folder
    ```

3. The script will process each image in the input folder and save the processed images in the output folder.

## Example

Assume you have a folder named `Sample_Images` containing several images. To process these images and save them in a folder named `Results`, run the script as follows:

```bash
python image_processing.py Sample_Images Results
