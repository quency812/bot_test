import qrcode
import random
import os


def generate(url, user_id):
    img = qrcode.make(url)
    name = str(user_id) + str(random.randint(233, 943234))
    file_path = os.path.join("qrcode_img", name + ".png")
    img.save(file_path)
    return file_path
