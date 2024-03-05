String inputString = "";
bool isStringComplete = false;

void setup() {
    inputString.reserve(200);
    Serial.begin(19200);
}

void loop() {
    if (isStringComplete) {
        // Do stuff with the command!
        if (inputString.equals("RESET")) {
            Serial.println("READY,  SAGIAN PE Loader, ROM Ver. 1.1.6, 12APR2001");
        } else if (inputString.startsWith("X-AXIS ")) {
            Serial.println("READY");
        } else if (inputString.equals("GRIPPER OPEN")) {
            Serial.println("READY, OPEN");
        } else if (inputString.equals("GRIPPER CLOSE")) {
            Serial.println("READY, CLOSED, NOPLATE");
        } else if (inputString.startsWith("MOVE ")) {
            delay(3000);
            Serial.println("READY");
        } else if (inputString.startsWith("LOADER_STATUS")) {
            Serial.println("READY, POSITION 3, Z-AXIS RETRACTED, GRIPPER CLOSED, NOPLATE" );
        } 

        
        else {
            Serial.print("Unknown command: ");
            Serial.println(inputString);
        }

        inputString = "";
        isStringComplete = false;
    }
}

void serialEvent() {
    while(Serial.available()) {
        char inChar = (char) Serial.read();
        if (inChar == '\n') {
            isStringComplete = true;
        } else {
            inputString += inChar;
        }
    }
}