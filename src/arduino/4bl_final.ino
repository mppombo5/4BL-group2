  
String frequency;
void setup() {
  frequency = "";
  pinMode(12, OUTPUT);
  digitalWrite(12, LOW);
  Serial.begin(9600);
}

void loop() {

  if (Serial.available()) {
    char inByte = Serial.read();
    if (inByte == '\n') {
      // this is just to make sure communication works
      // TODO: write to LEDs using the value of frequency here instead of these tests
      if (frequency.charAt(0) == '1') {
        digitalWrite(12, LOW);
      } else {
        digitalWrite(12, HIGH);
      }

      frequency = "";
    } else {
      frequency += inByte;
    }
  }
  
//  while(!Serial.available()) {} //Does nothing while no frequency is read
//  while(Serial.available())
//  {
//    if (Serial.available() != 0 )   //0 is the terminating character
//    {
//      char digit = Serial.read();
//      frequency += digit;
//    }
//  }
//
//  //Outputs the number in some form
//  if (frequency.length() > 0) //If some data is recieved
//  {
//    //Here we can decide on how we want to output the data.
//  }
//
//  delay(3000); //Wait for 3 seconds to display the results
//  frequency = ""; //Reset the string to read new data
}