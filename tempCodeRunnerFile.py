import cv2
import face_recognition
import os
import serial
import time
from datetime import datetime

# ---------------- SERIAL SETUP ----------------
last_signal = None
last_status = None

try:
    arduino = serial.Serial('COM5', 9600)
    print("Arduino connected")
    time.sleep(2)
except:
    print("Arduino not connected")
    arduino = None

def send_signal(signal):
    global last_signal
    if arduino and signal != last_signal:
        arduino.write(signal)
        print("Signal:", signal)
        last_signal = signal
        time.sleep(0.1)   # 🔥 gives Arduino time to read


# ---------------- FILE SAFETY ----------------
if not os.path.exists('Attendance.csv'):
    with open('Attendance.csv', 'w') as f:
        f.write('Name,Date,Time\n')


# ---------------- LOAD IMAGES ----------------
path = 'ImagesAttendance'
images = []
classNames = []

myList = os.listdir(path)

for cl in myList:
    img = cv2.imread(f'{path}/{cl}')
    if img is not None:
        images.append(img)
        classNames.append(os.path.splitext(cl)[0])


# ---------------- ENCODING ----------------
def findEncodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encodes = face_recognition.face_encodings(img)
        if len(encodes) > 0:
            encodeList.append(encodes[0])
    return encodeList


encodeListKnown = findEncodings(images)
print("Encoding Complete")


# ---------------- ATTENDANCE ----------------
def markAttendance(name):
    today = datetime.now().strftime('%Y-%m-%d')

    with open('Attendance.csv', 'r+') as f:
        data = f.readlines()

        already_marked = False
        for line in data:
            if name in line and today in line:
                already_marked = True
                break

        if not already_marked:
            now = datetime.now()
            timeString = now.strftime('%H:%M:%S')
            f.writelines(f'\n{name},{today},{timeString}')
            send_signal(b'S')
            print(name, "Marked Present")
        else:
            send_signal(b'D')
            print(name, "Already Marked")


# ---------------- WEBCAM ----------------
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Camera not working")
    exit()

# Cooldown to avoid repeated marking
lastMarked = {}
cooldown = 10   # seconds

while True:
    success, img = cap.read()
    if not success:
        print("Failed to capture image")
        break

    # Resize for faster processing
    imgSmall = cv2.resize(img, (0, 0), None, 0.25, 0.25)
    imgSmall = cv2.cvtColor(imgSmall, cv2.COLOR_BGR2RGB)

    faces = face_recognition.face_locations(imgSmall)
    encodes = face_recognition.face_encodings(imgSmall, faces)

    if len(faces) == 0:
        last_status = None

    # Processing signal
    if len(faces) > 0:
        send_signal(b'P')

    for encodeFace, faceLoc in zip(encodes, faces):

        matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
        faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)

        if len(faceDis) == 0:
            continue

        matchIndex = faceDis.argmin()

        if matches[matchIndex] and faceDis[matchIndex] < 0.5:
            name = classNames[matchIndex].split("_")[0].upper()
            current_time = time.time()

            # Print only when state changes
            if last_status != 'known':
                print("Recognized:", name)
                last_status = 'known'

            if name not in lastMarked or (current_time - lastMarked[name]) > cooldown:
                markAttendance(name)
                lastMarked[name] = current_time

            # Draw rectangle
            y1, x2, y2, x1 = faceLoc
            y1, x2, y2, x1 = y1*4, x2*4, y2*4, x1*4

            cv2.rectangle(img, (x1,y1), (x2,y2), (0,255,0), 2)
            cv2.putText(img, name, (x1, y2+25),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,255,0), 2)

        else:
            # Print only once when state changes
            if last_status != 'unknown':
                print("Unknown Face")
                last_status = 'unknown'

            send_signal(b'F')

    cv2.imshow("Webcam", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    # small delay to reduce CPU usage
    time.sleep(0.05)


# ---------------- CLEANUP ----------------
cap.release()
cv2.destroyAllWindows()

if arduino:
    arduino.close()