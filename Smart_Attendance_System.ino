// LED Pins
const int greenLED = 8;
const int redLED = 9;
const int blueLED = 10;

char incomingData;

void setup() {
  pinMode(greenLED, OUTPUT);
  pinMode(redLED, OUTPUT);
  pinMode(blueLED, OUTPUT);

  Serial.begin(9600);
}

// -------- LED FUNCTIONS --------

void allOff() {
  digitalWrite(greenLED, LOW);
  digitalWrite(redLED, LOW);
  digitalWrite(blueLED, LOW);
}

// Processing (Blue ON)
void processingState() {
  allOff();
  digitalWrite(blueLED, HIGH);
}

// Success (Green blink 2 times)
void successState() {
  allOff();
  for (int i = 0; i < 2; i++) {
    digitalWrite(greenLED, HIGH);
    delay(300);
    digitalWrite(greenLED, LOW);
    delay(300);
  }
}

// Failure (Red fast blink)
void failureState() {
  allOff();
  for (int i = 0; i < 4; i++) {
    digitalWrite(redLED, HIGH);
    delay(150);
    digitalWrite(redLED, LOW);
    delay(150);
  }
}

// Duplicate (Red + Blue blink together)
void duplicateState() {
  allOff();
  for (int i = 0; i < 3; i++) {
    digitalWrite(redLED, HIGH);
    digitalWrite(blueLED, HIGH);
    delay(250);
    digitalWrite(redLED, LOW);
    digitalWrite(blueLED, LOW);
    delay(250);
  }
}

// -------- MAIN LOOP --------

void loop() {
  if (Serial.available() > 0) {
    incomingData = Serial.read();

    if (incomingData == 'P') {
      processingState();
    }
    else if (incomingData == 'S') {
      successState();
    }
    else if (incomingData == 'F') {
      failureState();
    }
    else if (incomingData == 'D') {
      duplicateState();
    }
    else if (incomingData == 'O') {
    allOff();
    }
  }
}
