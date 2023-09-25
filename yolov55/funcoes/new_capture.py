import cv2
import torch

# Carregar o modelo YOLOv5 pré-treinado
model = torch.hub.load('/home/emanuel/Documents/detc_ativi/yolov5/runs/train/mask_yolov5s_results/weights/', 'yolov5s')  # Você pode escolher o tamanho de modelo desejado

# Iniciar a captura de vídeo da webcam (0 indica a webcam padrão)
video_capture = cv2.VideoCapture(0)

while True:
    ret, frame = video_capture.read()

    # Fazer a detecção de objetos no quadro atual
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

    # Exibir o quadro com as caixas delimitadoras e rótulos desenhados
    cv2.imshow('Detecção em Tempo Real YOLOv5', frame)

    # Verificar se a tecla 'q' foi pressionada para sair
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar a captura de vídeo e fechar janelas
video_capture.release()
cv2.destroyAllWindows()
