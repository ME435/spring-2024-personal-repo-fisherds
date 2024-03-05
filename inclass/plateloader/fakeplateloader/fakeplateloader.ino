String inputString = "";
bool isStringComplete = false;

void setup() {
    inputString.reserve(200);
    Serial.begin(19200);
}

void loop() {
    if (isStringComplete) {
        // Do stuff with it!
        if (inputString.equals("RESET")) {
            Serial.println("READY, SAGIAN PE Loader, ROM...");
        } if (inputString.startsWith("X-AXIS ")) {
            Serial.println("READY");
        } else {
            Serial.println("Unknown command!");
            Serial.println(inputString);
        }


        inputString = "";
        isStringComplete = false;
    }
}

void serialEvent() {
    while (Serial.available()) {
        char inChar = (char) Serial.read();
        if (inChar == '\n') {
            isStringComplete = true;
        } else {
            inputString += inChar;
        }
    }
}
