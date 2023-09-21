import sys, os

path = os.getcwd() + r'/src'
sys.path.append(path)

import video2text
import cv2
import numpy as np

img=cv2.imread("test/jntm.jpg")
out=video2text.transfer(img,50,200)
print(out)
