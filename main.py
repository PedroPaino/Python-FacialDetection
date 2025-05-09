import cv2
from cvzone.FaceDetectionModule import FaceDetector

# Inicializa a captura de vídeo e o detector de faces
video = cv2.VideoCapture(0)
detector = FaceDetector()

while True:
    # Lê o frame da câmera
    ret, img = video.read()
    if not ret:
        print("Erro ao acessar a câmera.")
        break

    # Detecta rostos no frame
    img, bboxes = detector.findFaces(img, draw=True)

    # Exibe o resultado
    cv2.imshow("Resultado", img)

    # Sai do loop ao pressionar 'Esc'
    if cv2.waitKey(1) == 27:
        break

# Libera os recursos
video.release()
cv2.destroyAllWindows()