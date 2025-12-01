// LED 3 enciende/apaga según reciba '1' o '0' por Serial
void setup() {
  Serial.begin(9600);
  pinMode(3, OUTPUT);
}

void loop() {
  if (Serial.available()) {
    char c = Serial.read();
    if (c == '1') digitalWrite(3, HIGH);
    if (c == '0') digitalWrite(3, LOW);
  }
}
