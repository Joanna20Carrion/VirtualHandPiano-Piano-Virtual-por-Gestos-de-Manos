import cv2
import mediapipe as mp
import pygame

# Inicialización de Mediapipe y Pygame
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5)
mp_drawing = mp.solutions.drawing_utils

pygame.init()
pygame.mixer.init()

# Lista de notas y carga de sonidos
keys = ["A", "B", "Bb", "C#", "C", "D", "E", "Eb", "F#", "F", "G#", "G"]
sounds = {key: pygame.mixer.Sound(f"sounds/{key}.wav") for key in keys}

# Configuración de la cámara
cap = cv2.VideoCapture(0)

# Función para determinar la nota según la posición X del dedo
def get_note_from_position(x_position, width):
    step = width // len(keys)  # Calculamos el ancho de cada tecla
    index = min(x_position // step, len(keys) - 1)  # Calculamos qué tecla está más cerca
    return keys[index]

# Dibujar el piano virtual
def draw_piano(frame, width, height, active_note=None):
    piano_height = 100  # Altura del piano
    key_width = width // len(keys)  # Ancho de cada tecla
    colors = {"white": (255, 255, 255), "black": (0, 0, 0), "active": (0, 255, 0)}

    # Dibujar teclas del piano
    for i, key in enumerate(keys):
        x_start = i * key_width
        color = colors["white"] if "#" not in key and "b" not in key else colors["black"]
        if key == active_note:
            color = colors["active"]
        cv2.rectangle(frame, (x_start, height - piano_height), (x_start + key_width, height), color, -1)
        cv2.rectangle(frame, (x_start, height - piano_height), (x_start + key_width, height), (0, 0, 0), 2)

        # Agregar texto de la nota
        text_color = (0, 0, 0) if color == colors["white"] else (255, 255, 255)
        cv2.putText(frame, key, (x_start + 10, height - piano_height + 60), cv2.FONT_HERSHEY_SIMPLEX, 0.6, text_color, 2)

# Ciclo principal
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Error al capturar la imagen.")
        break

    # Procesar el marco de video
    frame = cv2.flip(frame, 1)
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(frame_rgb)

    height, width, _ = frame.shape
    active_note = None

    # Dibujar las manos y detectar notas
    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Coordenadas del dedo índice
            index_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
            x, y = int(index_finger_tip.x * width), int(index_finger_tip.y * height)

            # Obtener nota según la posición X del dedo
            active_note = get_note_from_position(x, width)
            if active_note in sounds:
                sounds[active_note].play()

            # Dibujar la posición del dedo índice
            cv2.circle(frame, (x, y), 10, (0, 255, 0), -1)

    # Dibujar el piano virtual
    draw_piano(frame, width, height, active_note)

    # Mostrar el video
    cv2.imshow("Piano Virtual", frame)

    # Salir con la tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar recursos
cap.release()
cv2.destroyAllWindows()
hands.close()
pygame.quit()
