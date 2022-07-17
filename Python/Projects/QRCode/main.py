#!/usr/bin/env python3
"""
project: CodeGuppy
created:2022-1-4
@author:seraph1001100
contact:seraph1001100@gmail.com
"""


import qrcode
from image import *


qr = qrcode.QRCode(version=1,
                   error_correction=qrcode.constants.ERROR_CORRECT_L,
                   box_size = 20,
                   border=2)


qr.add_data("https://seraph76.com")
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")

img.save("mycode_adv.png")
