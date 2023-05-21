import os
from PIL import Image, ImageFilter


source_dir = "papka"
output_dir = "processed_images"


if not os.path.exists(output_dir):
    os.makedirs(output_dir)


filenames = os.listdir(source_dir)


for filename in filenames:

    if filename.endswith(".jpg") or filename.endswith(".png"):

        image_path = os.path.join(source_dir, filename)
        with Image.open(image_path) as img:
            pixels = img.load()

            img_contour = img.filter(ImageFilter.CONTOUR)

            output_path = os.path.join(output_dir, "new_" + filename)
            img_contour.save(output_path)



print("Все изображения обработаны!")