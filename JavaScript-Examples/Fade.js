/*
PWM.js
his example shows how to use PWM in order to modify the brightness in a LED

This example code is in the public domain.

Revision History
------------------------------------------------
Author			  Date			  Description
------------------------------------------------
Carlos Mata			2-9-2015		Example created 
*/
var mraa = require('mraa');   //Imports MRAA library
var LED = new mraa.Pwm(3);
LED.period_us(700);
LED.enable(true);
Brightness = 0.0;
FadeAmount = 0.01;

function sleep(milliseconds) {
  var start = new Date().getTime();
  for (var i = 0; i < 1e7; i++) {
    if ((new Date().getTime() - start) > milliseconds){
      break;
    }
  }
}
while (true){
        LED.write(Brightness);
	Brightness = Brightness + FadeAmount;
	if ((Brightness >= 1.0) || (Brightness <= 0.0)){
		FadeAmount = -1 * FadeAmount;
	}
	sleep(30);
}

