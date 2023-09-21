import sys, os

path = os.getcwd() + r'/src'
sys.path.append(path)

import video2text
import cv2
import numpy as np

n=1
cap = cv2.VideoCapture("test/只因你太美(鸡你太美)原版.只因你太美(鸡你太美)原版.90717632.mp4")
while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        out=video2text.transfer(frame,25,120)
        print(out)
        with open("test/jntm/({}).txt".format(n),"w") as f:
            f.write(out)
        n+=1
    else:
        break
cap.release()