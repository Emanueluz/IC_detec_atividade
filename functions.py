
def sep_d_frames(video):
    if os.path.isdir('frames_Tracking'):
        return 
    else:
        os.mkdir('frames_Tracking')
        vidcap = cv2.VideoCapture(video)
        success,image = vidcap.read()
        count = 0
        success = True
        while success:
          success,image = vidcap.read()
          cv2.imwrite("frames_Tracking/frame%d.jpg" % count, image)     # save frame as JPEG file
          if cv2.waitKey(10) == 27:                     # exit if Escape is hit
              break
          count += 1
        return 0
