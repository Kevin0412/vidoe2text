import sys, os

path = os.getcwd() + r'/src'
sys.path.append(path)

import video2text
import cv2
import numpy as np
import time
import pygame

cap = cv2.VideoCapture("test/never_gonna_give_you_up.mp4")
n=0
speed=1
start=0
FPS=cap.get(5)
pygame.mixer.init()
pygame.mixer.music.load("test/never_gonna_give_you_up.mp3")
pygame.mixer.music.play(start=0.0)
start_time=time.time()
prev_time=time.time()-start_time
while cap.isOpened():
    if n!=0:
        while curr_time>=n/FPS/speed:
            ret, img = cap.read()
            if not ret:
                break
            n+=1
    else:
        while start*FPS>=n:
            ret, img = cap.read()
            if not ret:
                break
            out=video2text.transfer(img,50,240)
            print(out)
            print(str(int(n/FPS*100)/100)+"/"+str(start))
            n+=1
        if start!=0:
            start_time=time.time()-start/speed
        curr_time = time.time()-start_time
    if not ret:
        break
    if curr_time>=(n-1)/FPS/speed and curr_time<=n/FPS/speed:
        out=video2text.transfer(img,50,240)
        print(out)
        curr_time = time.time()-start_time
        fps = 1/(curr_time-prev_time)
        prev_time = curr_time
        print(str(int(curr_time*speed*100)/100)+'\t'+str(int(fps*10)/10))
pygame.mixer.music.stop()
cap.release()