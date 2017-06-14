/*
pwm.c
This example creates a PWM loop on a period of 500us that will vary between 0% and 100% and vice versa.
This example can be used to show how to use PWM in order to modify the brightness in a LED.
This example wa written with the latest version of mraa (1.7.0) when originally posted.
This example code is in the public domain.
Revision History
------------------------------------------------
Author			  Date			  Description
------------------------------------------------
Pedro Mora		6-14-2017		Example created 
*/

#include <unistd.h>
#include <stdbool.h>
#include "mraa.h"

int main()
{
    mraa_init();
    mraa_pwm_context pwm;
    pwm = mraa_pwm_init(3);
    if (pwm == NULL)
        return 1;
    mraa_pwm_period_us(pwm, 500);
    mraa_pwm_enable(pwm, 1);

    float value = 0.0f;
    bool ch = true;

    while(true)
    {
        if(value >= 1.0f)
            ch = false;
        if(value <= 0.0f)
            ch = true;
        if(ch == true)
            value = value + 0.05f;
        if(ch == false)
            value = value - 0.05f;
        mraa_pwm_write(pwm, value);
        usleep(50000);
        float output = mraa_pwm_read(pwm);
        printf("PWM value is %f\n", output);
    }
    return 0;
}
