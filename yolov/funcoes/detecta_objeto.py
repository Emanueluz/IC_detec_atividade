import cv2
import torch
import os
# Carregar o modelo YOLOv5 pré-treinado
diretorio = os.getcwd()
model_name='last.pt'
model = torch.hub.load(diretorio, 'custom', source='local', path = model_name, force_reload = True)

#model = torch.hub.load('runs/train/mask_yolov5s_results/weights/','models/yolov5s.yaml')  # Você pode escolher o tamanho de modelo desejado

# Carregar a imagem de entrada
image_path = 'imagem.jpeg'
image = cv2.imread(image_path)
print("\n\n\n", image.shape)
# Fazer a detecção de objetos na imagem
results = model(image)

# Acessar as previsões dos objetos encontrados (coordenadas e classes)
predictions = results.pandas().xyxy[0]


 
# Fazer algo com as previsões, como desenhar caixas delimitadoras nos objetos detectados
for _,prediction in predictions.iterrows():
    print('\n\n\n\n',type(prediction),"\n\n\n\n")
'''

    x_min, y_min, x_max, y_max, confidence, class_id = prediction
    class_name = model.names[int(class_id)]

    # Desenhar a caixa delimitadora e o rótulo do objeto
    cv2.rectangle(image, (int(x_min), int(y_min)), (int(x_max), int(y_max)), (0, 255, 0), 2)
    cv2.putText(image, f'{class_name}: {confidence:.2f}', (int(x_min), int(y_min) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

'''
# Exibir a imagem com as caixas delimitadoras e rótulos desenhados
cv2.imshow('Detecção de Objetos YOLOv5', image)

# Aguardar até que uma tecla seja pressionada e fechar a janela
cv2.waitKey(0)
cv2.destroyAllWindows()