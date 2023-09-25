import numpy as np
import cv2
from mss import mss
from PIL import Image
from time import time 
import torch 
import sys
#from screeninfo import get_monitors

bounding_box = {'top': 0, 'left': 0, 'width': 500, 'height': 500}

sct = mss()

while True:
    start=time()
    sct_img = sct.grab(bounding_box)

    cv2.imshow('screen', np.array(sct_img))


    if (cv2.waitKey(1) & 0xFF) == ord('q'):
        cv2.destroyAllWindows()
        break
    

    end=time()
    fps = 1/(end-start)
print(type(np.array(sct_img)))