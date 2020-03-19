int firstSensor = 0;
int secondSensor = 0;
int button;
void setup() {
  // start serial port
  Serial.begin(9600);
  pinMode(2, INPUT);
  while (!Serial) {
    ; // wait for serial port to connect. Needed for native USB port only
  }
  establishContact();  // send a byte to establish contact until receiver responds
}

void loop() {
  // if we get a valid byte, read analog ins:
  //we devide by for so that the data fits in 1 byte
  if (Serial.available() > 0) {
    inByte = Serial.read();
    firstSensor = analogRead(A0) / 4;
    Serial.println(firstSensor);
    secondSensor = analogRead(A1) / 4;
    Serial.println(secondSensor);
    button = digitalRead(2);
    Serial.println(button);
}
//handshake-----------------------------
void establishContact() {
  while (Serial.available() <= 0) {
    Serial.print('A');   // send a capital A
    delay(300);
  }
}