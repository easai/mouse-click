import time
import board
import digitalio
import usb_hid
import neopixel
from adafruit_hid.mouse import Mouse

mouse = Mouse(usb_hid.devices)

button = digitalio.DigitalInOut(board.GP14)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP

pixel = neopixel.NeoPixel(board.GP16, 1, brightness=0.3)

while True:
    if not button.value:
        pixel[0] = (0, 255, 0)
        mouse.click(Mouse.LEFT_BUTTON)
        time.sleep(0.4)
        pixel[0] = (0, 0, 0)
    time.sleep(0.01)

