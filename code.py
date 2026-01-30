import board
import digitalio
import usb_hid
import neopixel
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
    pixel = neopixel.NeoPixel(board.GP16, 1, brightness=0.3)
except:
    pixel = None

while True:
    # When button is pressed, hold mouse button down
    if not button.value:
        if pixel:
            pixel[0] = (0, 255, 0)  # Green LED to indicate button press

        # Press and hold the mouse button
        mouse.press(Mouse.LEFT_BUTTON)
        
        # Keep holding while button is pressed
        while not button.value:
            time.sleep(0.01)
        
        # Release when button is released
        mouse.release(Mouse.LEFT_BUTTON)
        
        if pixel:
            pixel[0] = (0, 0, 0)  # Turn off LED
        
        # Small debounce
        time.sleep(0.05)
    
    time.sleep(0.01)
