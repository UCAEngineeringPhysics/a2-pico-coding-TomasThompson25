from machine import Pin, PWM, Timer
from time import sleep


# SETUP
led = PWM(Pin(15))
button = Pin(16, Pin.IN, Pin.PULL_UP)
mode = 0

def on_button_release(Pin):
    global mode 
    mode = not mode
    
button.irq(trigger=Pin.IRQ_RISING, handler=on_button_release) 


# LOOP
inc = 65535//200
duty = 0
while True:
    if mode == 0:
        duty = duty + inc
        led.duty_u16(duty)
        if duty>= 65535:
            duty = 65535
            inc = -inc
        elif duty <= 0:
            duty = 0
            inc = -inc
    else:
        led.duty_u16(65535)
        
    sleep(0.01)
    
