import board
import digitalio
import usb_hid
from adafruit_hid.mouse import Mouse
import time

# Initialize mouse
mouse = Mouse(usb_hid.devices)

# Button setup
button = digitalio.DigitalInOut(board.GP14)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP

# LED feedback (optional)
try:
    led = digitalio.DigitalInOut(board.LED)
    led.direction = digitalio.Direction.OUTPUT
except:
    led = None

while True:
    # When button is pressed, hold mouse button down
    if not button.value:
        if led:
            led.value = True

        # Press and hold the mouse button
        mouse.press(Mouse.LEFT_BUTTON)
        
        # Keep holding while button is pressed
        while not button.value:
            time.sleep(0.01)
        
        # Release when button is released
        mouse.release(Mouse.LEFT_BUTTON)
        
        if led:
            led.value = False
        
        # Small debounce
        time.sleep(0.05)
    
    time.sleep(0.01)
