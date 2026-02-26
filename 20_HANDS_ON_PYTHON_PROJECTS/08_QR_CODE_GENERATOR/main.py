'''
We are going to use a python library to generate a url to a qr code
'''

import qrcode

url = input("Enter the url : ")
filename = input("Filename you want to save it as : ")
if not(filename.endswith(".png")):
    filename = filename + ".png"

img = qrcode.make(url)
img.save(filename)