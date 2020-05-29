  
String frequency;
void setup() {
  frequency = "";
  Serial.begin(9600);
}

void loop() {

  if (Serial.available()) {
    char inByte = Serial.read();
    if (inByte == '\n') {
      // TODO: write to LEDs using the value of frequency here
      Serial.print(frequency); // this print is just to make sure communication works
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
