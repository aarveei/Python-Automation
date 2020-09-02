import os
import sys
from PIL import Image

#grab first and second argument from command line
image_folder = sys.argv[1]
output_folder = sys.argv[2]

print(image_folder, output_folder)

#check if new folder exists, if not then create it
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

#looping through Pokedex and saving the images with png format
for filename in os.listdir(image_folder):
    img = Image.open(f'{image_folder}{filename}')
    clean_name = os.path.splitext(filename)[0]
    img.save(f'{output_folder}{clean_name}.png', 'png')
    print('all done!')