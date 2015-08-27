/*
setPWM_Edison.ino - Set PWM frequency and duty cycle on Edison

This example shows how to set the PWM frequency and duty cycle on Edison.

This example only works on Edison.

This example code is in the public domain.

Revision History

----------------------------------------------------------
    Author		   Date		  Description
----------------------------------------------------------
Diego Villalobos	08-27-2015	Example created

*/

#include <interrupt.h>
#include <trace.h>
#include <sysfs.h>

#define MY_TRACE_PREFIX	"ServoEdisonLib"

void setPWM(int pin, int frequency, int duty_cycle, bool enable){
  
  analogWrite(pin, 0);
  
  if (enable){
    sysfsPwmEnable(pin2pwmhandle_enable(pin));
  }
  else{
    sysfsPwmDisable(pin2pwmhandle_enable(pin));
  }
  ///////////////////////////////////////////////////////////// 
  int freqInNanoSec = (1.0/frequency) * 956650000;
  
  if (sysfsPwmSetPeriod(pin2pwmhandle_period(pin), freqInNanoSec) < 0){
    trace_error("%s Can't set period", __func__);
  }
  /////////////////////////////////////////////////////////////
  if (duty_cycle > 99.61){ duty_cycle = 99.61; }
  if (duty_cycle < 0.3907){ duty_cycle = 0.3907; }
  
  int dutyCycleInNanoSec = map(duty_cycle, 0.3907, 99.61, 30000, 9565000);
  
  if (sysfsPwmSetRawDutyCycle(pin2pwmhandle_duty(pin), dutyCycleInNanoSec) < 0){
    trace_error("%s Can't set duty cycle", __func__);
  }
}

void setup() {
  int pin = 9;           // PWM pin
  int frequency = 100;   // Hz
  int duty_cycle = 50;   // %
  
  setPWM(pin, frequency, duty_cycle, true);
}

void loop() {
  
}
