# USB HID Mouse Clicker (CircuitPython)

<img src="https://github.com/easai/mouse-click/blob/main/IMG_2863.jpeg" width="300" alt="USB HID Mouse Clicker" />

This project turns an RP2040‑based board into a USB HID mouse that performs a left‑click whenever a physical button is pressed. It also provides visual feedback using the board’s built‑in LED or NeoPixel, depending on the hardware.

## Overview

The device appears to the computer as a standard USB mouse. When the user presses the connected button, the board sends a left‑click event and briefly activates an onboard light indicator. This makes the device useful for automation, accessibility tools, testing, or any situation where a physical trigger should generate a mouse click.

## Features

- USB HID mouse functionality using CircuitPython  
- Physical button input for triggering clicks  
- Visual feedback through onboard LED or NeoPixel  
- Debounced input for reliable operation  
- Works on Windows, macOS, and Linux without drivers  

## Hardware Requirements

- RP2040‑based development board (such as Raspberry Pi Pico, Pico W, RP2040 Zero, QT Py RP2040, etc.)  
- One momentary push button  
- Optional: onboard NeoPixel (varies by board)  

## Software Requirements

- CircuitPython installed on the board  
- Required HID and NeoPixel libraries placed in the `lib` folder on the CIRCUITPY drive  

## Wiring

- One side of the button connects to a chosen GPIO pin  
- The other side connects to GND  
- Internal pull‑up is enabled in software  
- NeoPixel wiring is handled by the board’s built‑in hardware  

## Behavior

When the board is plugged into a computer, it enumerates as a USB mouse. Pressing the button triggers a left‑click event. During the click, the onboard LED or NeoPixel lights up briefly to indicate activity. The light turns off once the click is complete.

## Usage

1. Install CircuitPython on the RP2040 board.  
2. Copy the required libraries into the `lib` directory.  
3. Place the program file on the CIRCUITPY drive as `code.py`.  
4. Connect the button to the appropriate GPIO pin and GND.  
5. Plug the board into a computer and press the button to generate mouse clicks.  

## Troubleshooting

- If the board is detected but does not click, verify the button wiring and pin assignment.  
- If the NeoPixel stays white or does not light, confirm the correct data pin and required libraries.  
- If nothing happens, ensure the file is named `code.py` and that CircuitPython is running.  

## Notes

This project can be extended with additional buttons, multiple click modes, macros, or keyboard shortcuts. CircuitPython’s HID support allows the device to act as a composite keyboard and mouse if needed.
