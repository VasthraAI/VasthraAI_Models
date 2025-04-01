# Instructions

This document provides detailed instructions for the following steps:
1. Using preprocessing scripts
2. Preparing the dataset
3. Creating sketches for the dataset (optional)
4. Training the GAN model
5. Generating images

# Using Preprocessing Scripts
To simplify the implementation process, several scripts are provided. Below is how to use them effectively.

## scrape.py
[Instructions for scrape.py would go here.]

## resize_color.py
This Python script processes images by resizing them to a specified resolution and converting them to RGB format. This step is essential because the GAN model requires square images and supports only RGB colors.

The script accepts the following arguments:
- **Input directory**: The folder containing the raw images. You can use `/dataset/raw_images` for this purpose, as it is designed to store raw images for preprocessing. Copy your images into this folder to keep your files organized.
- **Output directory**: The folder where the preprocessed images will be saved. The recommended path is `/dataset/real_images` Especially if you are using the generate_sketches.py for sketch generation.
- **Resolution**: The GAN model requires square images. A resolution of 512 pixels is highly recommended, though 1080 pixels is also supported. Note that higher resolutions, such as 1080px, may significantly increase model training time.

Execute the script using the following format, adjusting the directories to match your file paths:

```bash
python resize_color.py --input_folder "path/to/dataset/raw_images" --output_folder "path/to/dataset/real_images" --resolution 512
```

Example
```
python resize_color.py --input_folder "D:\\VasthraAI\\trials\\GEN_1\\dataset\\raw_images" --output_folder "D:\\VasthraAI\\trials\\GEN_1\\dataset\\real_images" --resolution 512
```

## generate_sketches.py

This Python script processes preprocessed images by converting them into sketches using edge detection. It takes RGB or grayscale images, applies a Gaussian blur to reduce noise, and uses the Canny edge detection algorithm to generate sketch-like outputs. This is useful for preparing data for generative models or artistic applications.

The script accepts the following arguments:
- **Input directory**: The folder containing preprocessed images. It is recommended to use `/dataset/real_images` (e.g., output from `resize_color.py`) as the input folder to maintain a clean workflow.
- **Output directory**: The folder where the generated sketches will be saved. A suggested path is `/dataset/sketches` to keep your sketch outputs organized.

Input images should be in .png, .jpg, or .jpeg format and ideally preprocessed (e.g., resized to a square resolution like 512x512 pixels using resize_color.py).

**Usage**

Execute the script using the following format, adjusting the directories to match your file paths:

```bash
python generate_sketches.py --input_folder "path/to/dataset/real_images" --output_folder "path/to/dataset/sketches"
```

Example
```
python generate_sketches.py --input_folder "D:\\VasthraAI\\trials\\GEN_1\\dataset\\real_images" --output_folder "D:\\VasthraAI\\trials\\GEN_1\\dataset\\sketches"
```