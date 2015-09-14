/*
retrieveWiFiPassword.ino - Shows the WiFi AP password within 3 seconds

This example shows the WiFi AP password for 3 seconds in case it has been forgotten.
This example code was originally written by the user Intel_Raad and shared it in the 
Edison's Community: https://communities.intel.com/thread/60076

This example only works on Edison.

This example code is in the public domain.

Revision History

----------------------------------------------------------
    Author		   Date		  Description
----------------------------------------------------------
Diego Villalobos	09-14-2015	Example created

*/

void setup() {
     delay(3000);
     system("grep '^wpa_passphrase' /etc/hostapd/hostapd.conf | sed 's/=/ /g' | awk '{print $2}' > /dev/ttyGS0");
}
 
void loop() {
  
}
