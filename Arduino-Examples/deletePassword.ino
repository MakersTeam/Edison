/*
deletePassword.ino - Removes Edison's password

This example removes the root password in case it has been forgotten.
This example code was originally written by the user Intel_Raad and shared it in the 
Edison's Community: https://communities.intel.com/thread/60008

This example only works on Edison.

This example code is in the public domain.

Revision History

----------------------------------------------------------
    Author		   Date		  Description
----------------------------------------------------------
Diego Villalobos	09-14-2015	Example created

*/

void setup() {
     system("cp /etc/shadow /etc/shadow.save");
     system("cp /etc/shadow- /etc/shadow");
     system("echo Done > /dev/ttyGS0");
}
void loop() {
  
}
