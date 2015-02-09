/*
SendImagetoWS.js
This example send a picture located in your board to a webserver using the IP address of the board

This example code is in the public domain.

Revision History
------------------------------------------------
Author			  Date			  Description
------------------------------------------------
Carlos Mata			2-6-2015		Example created 
>>>>>This example was tested using a Galileo Gen2
*/

var http = require('http')  
  , fs = require('fs');  
  
  
fs.readFile('/home/test/Capture.PNG', function(err, data) {  
  if (err) throw err;   
  http.createServer(function(req, res) {  
    res.writeHead(200, {'Content-Type': 'image/png'});  
    res.end(data);   
  }).listen(81,'XXX.XXX.XX.XXX');  
  console.log('Go to http://XXX.XXX.XX.XXX:81 and see the Capture.PNG');  
});  
