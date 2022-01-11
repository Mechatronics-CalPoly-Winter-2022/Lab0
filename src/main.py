"""!
@brief This module contains the functions necessary to control an LED
via a PWM signal on pin A0. If run as main, this module will
slowly ramp up the LED brightness from 0 to 100% over the course
of 5 seconds.
"""

##
# @mainpage
# @section description_main Lab 0
# This is the documentation page for Lab 0, a program that controls
# an LED using PWM.
#
# @author Kyle Jennings, William Dorosk, Zarek Lazowski
# @date January 6th, 2022


import pyb     #Library associated with the board
import time    #Library to control amount of time it takes to ramp up

def led_setup():
    """!
    Sets up the LED pin with the timer and channel.
    @return A channel object to control Pin A0 with.
    """
    
    TIMER = 2     #The associated timer for Pin A0
    CHANNEL = 1   #The associated channel for pin A0

    #Define the pin to use and input/output type
    led_pin = pyb.Pin(pyb.Pin.board.PA0, pyb.Pin.OUT_PP)
    
    #Set up the timer used for this pin
    tim2 = pyb.Timer(TIMER, freq=20000)
    
    #Set up the channel used, invert the PWM signal to correctly
    #  control the LED, as the cathode is connected to the pin
    ch2 = tim2.channel(CHANNEL, pyb.Timer.PWM_INVERTED, pin=led_pin)
    
    #Return the channel for control by other functions
    return ch2


def led_brightness(brightness: int, led) -> None:
    """!
    Changes the brightness of the LED using PWM.
    @param brightness A number between 0 and 100, representing
                      percentage brightness.
    @param led A channel object to apply the brightness to.
    """

    #Raise an error if brightness is outside the range of 0 to 100
    if brightness < 0 or brightness > 100:
        raise ValueError("Brightness must be between 0 and 100")

    #Set brightness of LED to given brightness
    led.pulse_width_percent(brightness)


#The following is a script that slowly ramps the brightness of an LED
#  from 0 to 100% over the course of 5 seconds.
if __name__ == "__main__":
    #Set up channel for LED
    led_ch = led_setup()

    #Initialize brightness to 0
    brightness = 0
    
    #Do this until the user intervenes or we run out of power
    while True:
        #Reset brightness once like a ramp function
        if brightness > 100:
            brightness = 0
        
        #Set LED brightness
        led_brightness(brightness, led_ch)
        
        #Delay for 50 ms
        time.sleep(0.05)
        
        #Increment brightness by one
        brightness += 1
