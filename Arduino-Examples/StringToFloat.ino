/*
StringToFloat.ino - String to Float conversion

Since the string.toFloat() function is not supported in the Edison boards, this example shows how to
perform this conversion using another way.

This example code is in the public domain.

Revision History
----------------------------------------------------------
    Author		   Date		  Description
----------------------------------------------------------
Diego Villalobos	06-09-2015	Example created

*/

String stringValue = "";    // String to be converted

void setup() {
  Serial.begin(9600);
  delay(3000);
  
  Serial.println("This example shows an alternative way to convert");
  Serial.println("a string value into a float value in the Edison boards.");
}

void loop() {
  stringValue = "-0.5527153";
  Serial.println("String value: " + stringValue);
  
  char floatbuf[32];                   // Make this buffer at least enough for the whole string.
  stringValue.toCharArray(floatbuf, sizeof(floatbuf));
  float floatValue = atof(floatbuf);
  
  Serial.print("Float value: ");
  Serial.println(floatValue);
  
  delay(5000);
}
