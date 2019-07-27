from PIL import Image
import os

filePath = os.getcwd()

img_base = Image.open(filePath + 'bg.png')
img_base.show()
img_helmet = Image.open(filePath + 'tip_helmet.png')
img_helmet.show()

helmet_x = 30
helmet_y = 384

box = [helmet_x, helmet_y, helmet_x + img_helmet.size[0], helmet_y + img_helmet.size[1]]

r, g, b, a = img_helmet.split()
img_base.paste(img_helmet, box)
img_base.show()
img_base.save(filePath + 'result.png')