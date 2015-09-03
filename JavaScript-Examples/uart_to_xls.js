/*
NewFilePerDate.js
This example takes data from the Edison's serial port, then creates a new .xls file with the serial data.
This example code is in the public domain.
Revision History
------------------------------------------------
Author			  Date			  Description
------------------------------------------------
Pedro Mora	 9-1-2015		  Script created 
*/
var m = require('mraa');
var x;
var y = 0;
var fs = require('fs');
var ws = fs.createWriteStream('uart_to_xls.xls');
u = new m.Uart(0);
u.setBaudRate(9600);
console.log("Test for reading UART");
while(y < 10)
{
	x = u.readStr(12);
	ws.write(x);
	y++;
}
ws.end();
