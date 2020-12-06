from gpiozero import LED, Button
from signal import pause
import os

led = LED(27)
button = Button(2)

def button_callback(channel):
    os.system('export XAUTHORITY=/home/pi/.Xauthority; export DISPLAY=:0; xdotool key ctrl+Tab')

button.when_pressed = led.on
button.when_pressed = button_callback
button.when_released = led.off

pause()
