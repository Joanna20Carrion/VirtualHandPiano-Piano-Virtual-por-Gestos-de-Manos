# VirtualHandPiano

VirtualHandPiano es un piano virtual interactivo que utiliza tu cámara para detectar el movimiento de tus manos y reproducir notas musicales en tiempo real. Este proyecto combina tecnologías como OpenCV, Mediapipe y Pygame para crear una experiencia musical divertida y creativa.

## Características
- 🎵 Piano virtual con 12 teclas que representan las notas musicales.
- 🎹 Detección del dedo índice para tocar las notas según la posición en la pantalla.
- 📹 Uso de la cámara para el seguimiento de las manos en tiempo real.
- 🔊 Reproducción de sonidos mediante archivos .wav.

## Instalación

1. Clona este repositorio:
    ```bash
    gh repo clone Joanna20Carrion/VirtualHandPiano-Piano-Virtual-por-Gestos-de-Manos
    ```

2. Asegúrate de tener instalado Python 3.7 o superior.

3. Instala las dependencias necesarias:
    ```bash
    pip install opencv-python mediapipe pygame
    ```

4. Crea una carpeta llamada `sounds` en el directorio principal del proyecto y añade los archivos `.wav` correspondientes a las notas (por ejemplo, `A.wav`, `B.wav`, etc.).

## Uso

1. Conecta una cámara web a tu computadora.
2. Ejecuta el script principal:
    ```bash
    python piano_virtual.py
    ```
3. Mueve tu mano frente a la cámara para interactuar con el piano virtual. Presiona la tecla **q** para salir.

## Estructura del Proyecto

| Archivo           | Descripción                                   |
|-------------------|-----------------------------------------------|
| `piano_vitual.py` | Código principal del proyecto.                |
| `sounds/`         | Carpeta que contiene los archivos de sonido.  |

## Requisitos

- Python 3.7 o superior.
- Cámara web.
- Archivos de sonido en formato `.wav` para las notas musicales.

## Tecnologías Utilizadas

- **OpenCV**: Para capturar y procesar el video en tiempo real.
- **Mediapipe**: Para el seguimiento de las manos.
- **Pygame**: Para reproducir los sonidos de las notas musicales.

## Autor
**Joanna Alexandra Carrión Pérez**: Bachiller de Ingeniería Electrónica. Apasionada por la Ciencia de Datos y la Inteligencia Artificial. [LinkedIn](https://www.linkedin.com/in/joanna-carrion-perez/)

## Contacto
Para cualquier duda o sugerencia, contáctame a través de **joannacarrion14@gmail.com**.

## Contribuciones
¡Contribuciones son bienvenidas! Si tienes ideas o mejoras, no dudes en hacer un fork del repositorio y enviar un pull request.
