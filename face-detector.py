import cv2
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
face_cascade_path = os.path.join(current_dir, 'haarcascade_frontalface_default.xml')
face_cascade = cv2.CascadeClassifier(face_cascade_path)
if face_cascade.empty():
    print("Error: Could not load cascade classifier!")
    exit(1)

camera = cv2.VideoCapture(0)
if not camera.isOpened():
    print("Error: Could not open camera!")
    exit(1)

while True:
    rectangle, image = camera.read()
    gray_scale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    detect = face_cascade.detectMultiScale(gray_scale, 1.3, 6)

    for (x, y, w, h) in detect:
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)

    cv2.imshow('Face Detector', image)

    if cv2.waitKey(20) & 0xff == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()
print("Face detector stopped.")