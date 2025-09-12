# DOESN"T WORK :(
from machine import Pin, PWM, Timer
from time import sleep


# SETUP
led = PWM(Pin(15))
button = Pin(14, Pin.IN, Pin.PULL_UP)
blink_timer = Timer()

def on_button_release(Pin):
    led.freq(1000)
    
button.irq(trigger=Pin.IRQ_FALLING, handler=on_button_release) # had to use AI for this one


# LOOP
while True:
    if button.value() == 0:
        for duty in range(0,65535, 500): 
            led.duty_u16(duty) 
            sleep(2/ (65535/500)) 
        for duty in range(65535, -1, -500): 
            led.duty_u16(duty) 
            time.sleep(1 / (65535/500))
    else:
        led.duty_u16(65535)
    
