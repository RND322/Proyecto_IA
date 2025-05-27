🧠 Detección de Objetos en Tiempo Real con YOLOv11 

Este proyecto implementa un sistema de detección de objetos en imágenes y video en tiempo real utilizando Python y el modelo YOLOv11

📸 Descripción

La detección de objetos es una tarea crucial en visión por computadora con aplicaciones en vigilancia, vehículos autónomos y más. Este proyecto entrena una version del modelo YOLO para detectar múltiples objetos en imágenes usando el conjunto de datos COCO.

🚀 Características

Detección en imágenes y video en tiempo real.
Comparación de métricas: F1-score, precisión, recall, matriz de confusión.
Visualización de bounding boxes sobre objetos detectados.

🛠 Tecnologías

Lenguaje: Python 3.10 como minimo
Framework de IA: Ultralytics YOLO
Modelo: YOLOv11
Dataset: COCO (Common Objects in Context)
Bibliotecas:
opencv-python
ultralytics
matplotlib

🎯 Objetivos

Objetivo General
Desarrollar un modelo que detecte objetos en imágenes y videos en tiempo real.

Objetivos Específicos
Evaluar el rendimiento 10000 imágenes de entrenamiento 5000 imágenes de validacion 
Con un entrenamiento de 20 epocas con imagenes de 640 x 480 pixeles

📄Bibliotecas a instalar

pip install ultralytics
pip install opencv-python
pip install matplotlib

📌Modo de uso 

Para la deteccion en tiempo real
1. Instalar todas las bibliotecas requeridas.
2. EL script tiene que tener acceso al archivo "best.pt" es donde estan los pesos del entrenamiento.
3. Correr el script (yolo11_detection_cameraV2.py) utilizando el comando "python yolo11_detection_camera.py" desde la consola de comandos.
4. Se le mostrara una ventana con la camara web que empezara la deteccion de objetos en tiempo real.

Para la deteccion de imagenes por fotos
1. Instalar todas las bibliotecas requeridas.
2. EL script tiene que tener acceso al archivo "best.pt" es donde estan los pesos del entrenamiento.
3. El script debe tener acceso a la foto que se quiere reconocer a una carpeta en este caso la carpeta images.
4. Correr el script (yolo11_detection_image.py) utilizando el comando "python yolo11_detection_image.py" desde la consola de comandos.
5. Se le mostrara el resultado de la imagen con lo que el modelo pudo reconocer.

⚠️Autoria

Este proyecto fue creado por Ruben Diaz para la clase de Inteligencia Artifical 
