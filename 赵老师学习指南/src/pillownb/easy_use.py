from PIL import Image
import os

filePath = os.getcwd() + '/origin/'

# 两图拼一块
def photo_photo():
    img_base = Image.open(filePath + 'bg.jpg')
    img_base.show()
    img_sub = Image.open(filePath + 'subPhoto.jpg')
    img_sub.show()

    x = 0
    y = 0

    box = [x, y, x + img_sub.size[0], y + img_sub.size[1]]

    img_base.paste(img_sub, box)
    img_base.show()
    img_base.save(filePath + 'result.jpg')

# 图上加文字
def photo_word():
    pass

if __name__ == '__main__':
    photo_photo()

