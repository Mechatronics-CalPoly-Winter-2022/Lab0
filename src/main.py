import pyb
import time

def led_setup():
    """ This sets up the LED pin with the timer and the PWM
    """

    TIMER = 2
    CHANNEL = 1

    led_pin = pyb.Pin(pyb.Pin.board.PA0, pyb.Pin.OUT_PP)
    tim2 = pyb.Timer(TIMER, freq=20000)
    ch2 = tim2.channel(CHANNEL, pyb.Timer.PWM_INVERTED, pin=led_pin)
    return ch2


def led_brightness(brightness: int, led) -> None:
    """ Changes the brightness of the LED using PWM.
    """

    if brightness < 0 or brightness > 100:
        raise ValueError("Brightness must be between 0 and 100")

    led.pulse_width_percent(brightness)


if __name__ == "__main__":
    led_ch = led_setup()

    brightness = 0
    while True:
        if brightness > 100:
            brightness = 0
        led_brightness(brightness, led_ch)
        time.sleep(0.05)
        brightness += 1