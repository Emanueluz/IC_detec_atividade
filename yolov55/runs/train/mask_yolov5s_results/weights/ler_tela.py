import pyautogui 
import cv2 
import numpy as np 
import torch

resolution = (1920, 1080) 
codec = cv2.VideoWriter_fourcc(*"XVID") 
filename = "Recording.avi"
fps = 60.0
model = torch.hub.load('/home/emanuel/Documents/detc_ativi/yolov5/runs/train/mask_yolov5s_results/weights/best.pt', 'yolov5s')  # Você pode escolher o tamanho de modelo desejado

  
#out = cv2.VideoWriter(filename, codec, fps, resolution) 
cv2.namedWindow("Live", cv2.WINDOW_NORMAL) 
cv2.resizeWindow("Live", 500, 500) 
  
while True: 
    
    img = pyautogui.screenshot() 
  
    
    frame = np.array(img) 
    results = model(frame)
    # Acessar as previsões dos objetos encontrados (coordenadas e classes)
    predictions = results.pandas().xyxy[0]

    # Fazer algo com as previsões, como desenhar caixas delimitadoras nos objetos detectados
    for _, prediction in predictions.iterrows():
        x_min, y_min, x_max, y_max, confidence, class_id = prediction
        class_name = model.names[int(class_id)]

        # Desenhar a caixa delimitadora e o rótulo do objeto
        cv2.rectangle(frame, (int(x_min), int(y_min)), (int(x_max), int(y_max)), (0, 255, 0), 2)
        cv2.putText(frame, f'{class_name}: {confidence:.2f}', (int(x_min), int(y_min) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) 
  
    
    #out.write(frame) 
      
    
    cv2.imshow('Live', frame) 
      
    
    if cv2.waitKey(1) == ord('q'): 
        break
out.release() 
cv2.destroyAllWindows()