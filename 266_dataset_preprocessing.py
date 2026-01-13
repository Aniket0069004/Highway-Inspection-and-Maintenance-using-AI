import os
import cv2
import numpy as np

# Input and output folders
input_path = r'C:\Users\mishr\Desktop\Internship\project_266\DATASET_2.0'  # your original dataset
output_path = r'C:\Users\mishr\Desktop\Internship\project_266\Preprocessed_Dataset'  # where to save preprocessed images

# Resize dimensions (more standard for training)
resize_size = (416, 416)

# Create output directory structure
os.makedirs(output_path, exist_ok=True)

for class_name in os.listdir(input_path):
    class_input_dir = os.path.join(input_path, class_name)
    class_output_dir = os.path.join(output_path, class_name)

    if not os.path.isdir(class_input_dir):
        continue

    os.makedirs(class_output_dir, exist_ok=True)

    for filename in os.listdir(class_input_dir):
        try:
            img_path = os.path.join(class_input_dir, filename)
            img = cv2.imread(img_path)

            if img is None:
                print(f"Failed to read {img_path}")
                continue

            # Resize
            img_resized = cv2.resize(img, resize_size)

            # Normalize to [0, 1]
            img_normalized = img_resized / 255.0

            # Light Gaussian blur for noise reduction
            img_denoised = cv2.GaussianBlur(img_normalized, (3, 3), 0)

            # Convert back to 0–255 and uint8 to save
            img_to_save = (img_denoised * 255).astype(np.uint8)

            # Save with high JPEG quality
            output_img_path = os.path.join(class_output_dir, filename)
            cv2.imwrite(output_img_path, img_to_save, [int(cv2.IMWRITE_JPEG_QUALITY), 95])

        except Exception as e:
            print(f"Error processing {filename}: {e}")
