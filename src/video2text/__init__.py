import cv2
import numpy as np

def transfer(img,x,y):
    '''
    转化 图片 高度 宽度
    '''
    img=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img=cv2.resize(img,(y,x))
    out=""
    for a in range(x):
        for b in range(y):
            c=img[a][b]
            if c<32:
                #print(" ",end="")
                out+=" "
            elif c<64:
                #print(".",end="")
                out+="."
            elif c<96:
                #print(":",end="")
                out+=":"
            elif c<128:
                #print("=",end="")
                out+="="
            elif c<160:
                #print("*",end="")
                out+="*"
            elif c<224:
                #print("#",end="")
                out+="#"
            else:
                #print("@",end="")
                out+="@"
        #print("\n",end="")
        out+="\n"
    return out