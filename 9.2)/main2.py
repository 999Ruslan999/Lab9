import os
from PIL import Image, ImageFilter

folder_path = 'papka'
save_path = 'processed_images'

if not os.path.exists(save_path):
    os.makedirs(save_path)

for filename in os.listdir(folder_path):
    if filename.endswith('.jpg') or filename.endswith('.png'):
        img_path = os.path.join(folder_path, filename)
        img = Image.open(img_path)
        img = img.filter(ImageFilter.CONTOUR)
        new_filename = 'new_' + filename
        save_img_path = os.path.join(save_path, new_filename)
        img.save(save_img_path)

print('Все изображения обработаны успешно!')