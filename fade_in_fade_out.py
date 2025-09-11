from machine import Pin, PWM, Timer
from time import sleep


# SETUP
led = PWM(Pin(15))
led.freq(1000) 

# LOOP 

while True: 

    for duty in range(0,65535, 500): 
        led.duty_u16(duty) 
        sleep(2/ (65535/500)) 
       
    for duty in range(65535, -1, -500): 
        led.duty_u16(duty) 
        time.sleep(1 / (65535/500))
