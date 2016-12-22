# coding: "UTF-8"

'''
输出验证码内容
'''

from PIL import Image
from PIL import ImageOps
import pytesseract

# 获取二维码文本
def captcha_text(wd, imgID):
    try:
        print("try captcha_text")
        path_currentScreen = "/Users/JinXiaoHao/Desktop/currentScreen.jpg"
        path_captcha = "/Users/JinXiaoHao/Desktop/image_code.jpg"

        wd.save_screenshot(path_currentScreen)

        loc = wd.find_element_by_id(imgID).location  # 获取验证码图片的位置
        size = wd.find_element_by_id(imgID).size  # 获取验证码图片的大小

        box = (loc['x'], loc['y'], float(loc['x']) + float(size['width']), float(loc['y']) + float(size['height']))
        img = Image.open(path_currentScreen)
        img = img.crop(box)

        img = img.point(lambda x: 0 if x < 143 else 255)  # 处理图片上的每个像素点，使图片上每个点“非黑即白”
        img = ImageOps.expand(img, border=20, fill='white')
        img.save(path_captcha)

        return pytesseract.image_to_string(img).replace(' ', '')
    except:
        print('expect captcha_text')
        return ''
    finally:
        print('finally captcha_text')
