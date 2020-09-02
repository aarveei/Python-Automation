from PIL import Image, ImageFilter

img = Image.open("aarveei.PNG")
#filtered_img = img.filter(ImageFilter.SMOOTH)
filtered_img = img.convert('L')
#filtered_img.rotate(90)
#filtered_img.save("smooth.png", "png")
rotated_img = img.rotate(90)
rotated_img.save("rotated_img.png", "png")
filtered_img.show()

box = (100, 100, 400, 400)
region = filtered_img.crop(box)
region.save("cropped.png", "png")

#For resizing a pic with proper aspect ratio
img_2 = Image.open("smooth.png")
img_2.thumbnail((400, 400))
img_2.save("thumbnail.jpg")