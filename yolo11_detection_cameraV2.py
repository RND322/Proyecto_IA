import cv2
from ultralytics import YOLO
import matplotlib.pyplot as plt

# Cargar el modelo entrenado
model = YOLO('runs/detect/train4/weights/best.pt')

# Capturar video de la cámara web
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Realizar la predicción en el frame capturado
    results = model(frame)
    
    # Obtener la imagen anotada
    annotated_frame = results[0].plot()  # Esto devuelve la imagen en formato RGB
    
    # Mostrar la imagen usando matplotlib
    plt.imshow(annotated_frame)
    plt.title("Detecciones - Cámara Web")
    plt.axis('off')
    plt.pause(0.001)
    plt.clf()  # Limpiar la figura para el siguiente frame

cap.release()
