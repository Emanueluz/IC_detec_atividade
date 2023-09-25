import cv2

VIDEO = 'P.mp4'

cap = cv2.VideoCapture(VIDEO)
x = 0
while cap.isOpened():
    res, frame = cap.read()
    nomeDoFrame = 'imagens/frame-%d.jpg' % x
    cv2.imwrite(nomeDoFrame,frame)

cap.release()