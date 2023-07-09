import os
import cv2

def FrameCapture(path): 
    pasta="frames"
    if os.path.isdir(pasta):
        return 
    else:

        os.mkdir(pasta)
    vidObj = cv2.VideoCapture(path) 
    count = 0
    success = 1
    while success: 
        success, image = vidObj.read() 
        cv2.imwrite("frames/frame%d.jpg" % count, image) 
        count += 1
    
    
FrameCapture("/home/emanuel/Vídeos/PREVENÇÃO À COVID-19 PESSOAS ANDAM PELAS RUAS SEM MÁSCARA DE PROTEÇÃO.mp4") 