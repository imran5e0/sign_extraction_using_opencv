import os
from PIL import Image

BASE_FOLDER = 'output'
TARGET_SIZE_KB = 5

def compress_png(input_path, output_path):
    compress_level = 9  # max compression
    with Image.open(input_path) as img:
        img = img.convert('RGBA')  # Ensure alpha channel support for PNG
        img.save(output_path, format='PNG', optimize=True, compress_level=compress_level)

        size_kb = os.path.getsize(output_path) / 1024
        if size_kb > TARGET_SIZE_KB:
            print(f"⚠️ Still too large after compression: {output_path} ({size_kb:.2f} KB)")
        else:
            print(f"✅ Compressed: {output_path} ({size_kb:.2f} KB)")

def process_all_png_images(base_folder):
    for root, dirs, files in os.walk(base_folder):
        if os.path.basename(root).startswith('output'):
            for file in files:
                if file.lower().endswith('.png'):
                    full_path = os.path.join(root, file)
                    size_kb = os.path.getsize(full_path) / 1024
                    if size_kb > TARGET_SIZE_KB:
                        print(f"🔄 Compressing: {full_path} ({size_kb:.2f} KB)")
                        compress_png(full_path, full_path)

if __name__ == '__main__':
    process_all_png_images(BASE_FOLDER)
