
void setup() {
   // Set baudrate to match the pi
   Serial.begin(9600);
}

void loop() {

  // Convert the string we read into a number
  int location;
  while (!Serial.available())
    ; // Stay in this loop until Arduino redeives serial
  while (Serial.available() > 0) { 
    location = Serial.parseInt();
    //location = (Serial.read() - '0');
    
  }
  // Encode our location number back into a string to send to RPi
  location += 1;
  Serial.println(location); // sends b'1\r\n'

}
