import cv2
import os
import argparse


def generate_sketch(image_path, output_path):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)  # Convert to grayscale
    blurred = cv2.GaussianBlur(image, (5, 5), 0)  # Reduce noise
    edges = cv2.Canny(blurred, 50, 150)  # Detect edges
    
    cv2.imwrite(output_path, edges)  # Save the sketch


def process_folder(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    for filename in os.listdir(input_folder):
        if filename.lower().endswith(('png', 'jpg', 'jpeg')):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)
            generate_sketch(input_path, output_path)
            print(f"Processed: {filename}")


def main():
    parser = argparse.ArgumentParser(description="Create sketches from preprocessed images.")
    parser.add_argument(
        "--input_folder",
        type=str,
        required=True,
        help="The directory containing preprocessed images"
    )
    parser.add_argument(
        "--output_folder",
        type=str,
        required=True,
        help="The directory where sketches will be saved"  # Fixed description for clarity
    )

    # Parse the arguments
    args = parser.parse_args()

    # Call process_folder with the provided arguments
    process_folder(args.input_folder, args.output_folder)
    print("All images processed successfully!")


if __name__ == "__main__":
    main()