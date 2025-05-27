from ultralytics import YOLO
import matplotlib.pyplot as plt

# Cargar el modelo entrenado
model = YOLO('runs/detect/train4/weights/best.pt')

# Realizar la predicción en una imagen
results = model('images/calle.jpg')

# Obtener la imagen renderizada con las cajas (usamos el método plot() que retorna un arreglo numpy)
img_with_boxes = results[0].plot()

# Mostrar la imagen con matplotlib
plt.imshow(img_with_boxes)
plt.axis('off')
plt.show()
