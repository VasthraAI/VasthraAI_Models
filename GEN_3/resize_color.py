from PIL import Image
import os
import argparse

def process_images(input_dir, output_dir,resolution):
    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)
    
    # Process each file in the input directory
    for filename in os.listdir(input_dir):
        input_path = os.path.join(input_dir, filename)
        
        # Check if the file is an image
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
            try:
                with Image.open(input_path) as img:
                    # Resize the image to input resolution
                    new_size = (resolution, resolution)
                    resized_img = img.resize(new_size, Image.LANCZOS)

                    # Convert to RGB if necessary
                    if resized_img.mode != 'RGB':
                        resized_img = resized_img.convert('RGB')

                    # Save the processed image in the output directory
                    output_path = os.path.join(output_dir, filename)
                    resized_img.save(output_path)

                    print(f"Processed {filename} and saved to {output_path}")
            except Exception as e:
                print(f"Error processing {filename}: {e}")

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Process and resize images to 512x512 in RGB format.")
    parser.add_argument(
        "--input_folder",
        type=str,
        required=True,
        help="The directory containing raw images to process"
    )
    parser.add_argument(
        "--output_folder",
        type=str,
        required=True,
        help="The directory where processed images will be saved"
    )
    parser.add_argument(
        "--resolution",
        type=int,
        required=True,
        help="Enter the required pixel resolution needed. Default set to 512px"
    )

    # Parse the arguments
    args = parser.parse_args()

    # Call the process_images function with provided directories
    process_images(args.input_folder, args.output_folder, args.resolution)

    print("All images processed successfully!")

if __name__ == "__main__":
    main()