//Example Blink.js
//
//This examples shows how to make a simple Blink script
//
//This example code is in the public domain.
//
//Revision History
//------------------------------------------------
//Author			  Date			  Description
//------------------------------------------------
//Pedro Mora		02-12-2015			Blink.js
//
//

var mraa = require('mraa');                                   //this script requires MRAA
console.log('MRAA Version: ' + m.getVersion());               //this will write the MRAA version
var BLED = new m.Gpio(13);                                    //this binds the variable BLED to pin 13
BLED.dir(mraa.DIR_OUT);                                       //this sets the GPIO to output
var LEDSt = true;                                             //Boolean variable that will remember state of Led
blink();                                                      //this will call the blink function
function blink()
{
	BLED.write(LEDSt?1:0);                                //if the state of the LED is true then write a '1' (high) otherwise it writes a '0' (low)
	LEDSt = !LEDSt;                                       //this will invert the state of the LED
	setTimeout(blink,1000);                               //call the indicated function after 1 second(1000 milliseconds)
}
