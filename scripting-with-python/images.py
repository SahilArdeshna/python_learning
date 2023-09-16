from PIL import Image, ImageFilter

# img = Image.open('./pokedex/pikachu.jpg')

# filtered_img = img.filter(ImageFilter.SHARPEN)
# filtered_img.save('blur.png', 'png')

# filtered_img = img.convert('L')

# rotated_img = filtered_img.rotate(270)
# rotated_img.save('grey.png', 'png')

# box = (100, 100, 400, 400)
# croped = filtered_img.crop(box)
# croped.save('grey.png', 'png')

# crooked = filtered_img.resize((300, 300))
# crooked.save('grey.png', 'png')
# filtered_img.show()


# img = Image.open('./astro.jpg')
# resized_img = img.resize((400, 400))
# resized_img.save('new astro.jpg')
# print(resized_img.size)

img = Image.open('./astro.jpg')
img.thumbnail((400, 400))
img.save('new astro.jpg')
print(img.size)
