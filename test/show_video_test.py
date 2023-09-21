import sys, os

path = os.getcwd() + r'/src'
sys.path.append(path)

import video2text
import cv2
import numpy as np

cap = cv2.VideoCapture("test/never_gonna_give_you_up.mp4")
while cap.isOpened():
    ret, frame = cap.read()
    if ret==True:
        out=video2text.transfer(frame,40,200)
        print(out)
cap.release()