Title- Face Recognition Attendance System

PROJECT OVERVIEW
The Face Recognition Attendance System is a smart attendance management solution that automates the attendance marking process using facial recognition technology. The system captures live video through a webcam, detects and recognizes registered faces, and records attendance with the current date and time in a CSV file. An Arduino Uno is integrated to provide real-time LED indications for different system states, making the project a combination of Computer Vision, Python Programming, and Embedded Systems.

FEATURES
* Real-time face detection and recognition
* Automatic attendance marking with date and timestamp
* Duplicate attendance detection
* Unknown face detection
* Arduino-based LED status indication
* Attendance logging in CSV format
* Fast and contactless attendance system
* Easy to use and extend for classroom or office environments

🛠 TECH STACKS
    Software                                    Hardware        

 * Python 3.10                               * Arduino Uno R3  
 * OpenCV                                    * Breadboard      
 * Face Recognition Library (dlib)           * Green LED       
 * NumPy                                     * Red LED        
 * PySerial                                  * Blue LED        
 * VS Code                                   * 220 Ω Resistors 
 * Git & GitHub                              * Jumper Wires    
 * CSV File Handling                         * Laptop Webcam   

🔌HARDWARE REQUIRED
* Arduino Uno R3
* Laptop/Desktop with Webcam
* Breadboard
* 3 LEDs (Green, Red, Blue)
* 3 × 220 Ω Resistors
* Jumper Wires
* USB Cable

🔄 WORKING PRINCIPLE
* The webcam continuously captures live video.
* The system detects faces using OpenCV.
* The detected face is encoded and compared with the stored dataset.
* If the face matches: Attendance is marked in the CSV file. Green LED blinks.
* If the face is already marked: Duplicate attendance is detected. Red and Blue LEDs blink together.
* If the face is unknown: Red LED blinks.
* During face processing: Blue LED glows continuously.

💡 LED INDICATION
   LED Status                     Meaning      

 🔵 Blue ON                 Face Processing                
 🟢 Green Blink             Attendance Marked Successfully 
 🔴 Red Blink               Unknown Face                   
 🔴 + 🔵 Blink             Duplicate Attendance           

📁 PROJECT STRUCTURE
Face-Recognition-Attendance-System/
│
├── Arduino/
│   └── attendance_led.ino
│
├── ImagesAttendance/
│   ├── Person1.jpg
│   ├── Person2.jpg
│   └── ...
│
├── main.py
├── Attendance.csv
├── requirements.txt
├── README.md
├── .gitignore
└── LICENSE

📸 CIRCUIT DIAGRAM
Arduino Uno
Pin 8  ──220Ω──► Green LED ──► GND
Pin 9  ──220Ω──► Red LED ────► GND
Pin 10 ──220Ω──► Blue LED ───► GND

📈 APPLICATION
* Educational Institutions
* Offices and Workplaces
* Research Laboratories
* Libraries
* Conferences and Seminars
* Smart Campus Management
