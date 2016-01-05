/*
NewFilePerDate.js
This example checks the current file location, and creates a new file depending on its location. 
The script will create a new file naming it with the current date. If tere are other files with the same name it will 
change the termination for the new file.
This example code is in the public domain.
Revision History
------------------------------------------------
Author			  Date			  Description
------------------------------------------------
Pedro Mora	 9-3-2015		 Script created 
*/
var fs = require('fs');
var dat = new Date();
var day = dat.getDate();
var month = dat.getMonth() + 1;
var year = dat.getFullYear();
var fn = "";
var files = fs.readdirSync(__dirname);
var fillen = files.length - 1;
var ac = [];
var rd = month + "-"  + day + "-" + year;
fn = rd + "_1";
var bc = fn.split('');
var gen = false;
var mf = 0;
for(var c = 0; c <= fillen; c++)
{
    if(gen == true)
        if(mf < ac[bc.length-1])
        {
            mf = parseInt(ac[(bc.length - 1)]);
            gen = false;
        }
    ac = files[c].split('');
    for(var c1 = 0; c1 < (bc.length - 1); c1++)
    {
        if(ac.length != bc.length)
            break;
        if(ac[c1] != bc[c1])
            break;
        else
            if(ac[bc.length-2] == bc[(bc.length - 2)])
            {
                gen = true;
                break;
            }
    }
}
var fnam = rd + "_" + (mf+1);
var ws = fs.createWriteStream(fnam);
ws.end();
