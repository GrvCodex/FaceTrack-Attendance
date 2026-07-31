import cv2
import face_recognition

cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()

    rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    faces = face_recognition.face_locations(rgb)

    for (top, right, bottom, left) in faces:
        cv2.rectangle(img, (left, top), (right, bottom), (0,255,0), 2)

    cv2.imshow("Test Camera", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()