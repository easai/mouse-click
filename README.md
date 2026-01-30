# USB HID Mouse Clicker (CircuitPython)

<img src="https://github.com/easai/mouse-click/blob/main/IMG_2863.jpeg" width="300" alt="USB HID Mouse Clicker" />

Turn any RP2040-based board into a USB HID mouse that clicks when you press a button. Perfect for automation, accessibility, testing, or repetitive tasks.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![CircuitPython](https://img.shields.io/badge/CircuitPython-9.x-blueviolet.svg)](https://circuitpython.org/)

## Table of Contents
- [Quick Start](#quick-start)
- [Features](#features)
- [Hardware Requirements](#hardware-requirements)
- [Software Requirements](#software-requirements)
- [Installation](#installation)
- [Pin Configuration](#pin-configuration)
- [Usage](#usage)
- [Customization](#customization)
- [Troubleshooting](#troubleshooting)
- [Advanced Features](#advanced-features)
- [Contributing](#contributing)
- [License](#license)

## Quick Start

1. Flash CircuitPython to your RP2040 board
2. Copy libraries to `lib/` folder
3. Copy `code.py` to the CIRCUITPY drive
4. Wire button between GPIO pin and GND
5. Plug in and click!

## Features

- ✅ USB HID mouse functionality using CircuitPython  
- ✅ Physical button input for triggering clicks  
- ✅ Visual feedback through onboard LED or NeoPixel  
- ✅ Debounced input for reliable operation  
- ✅ Cross-platform: Works on Windows, macOS, and Linux without drivers  
- ✅ Low latency response
- ✅ Customizable click timing and behavior

## Hardware Requirements

### Supported Boards
- RP2040-Zero

### Additional Components
- 1× Momentary push button (normally open)
- Optional: Onboard NeoPixel (board-dependent)
- Optional: External LED + 220Ω resistor

## Software Requirements

### CircuitPython Version
- CircuitPython 8.0 or newer recommended
- Download from [circuitpython.org](https://circuitpython.org/downloads)

### Required Libraries
Download the [Adafruit CircuitPython Library Bundle](https://github.com/adafruit/Adafruit_CircuitPython_Bundle/releases) and copy these to your `lib/` folder:

- `adafruit_hid/` (entire folder)
  - `adafruit_hid/mouse.py`
  - `adafruit_hid/keyboard.py`
- `neopixel.mpy` (if using NeoPixel)

## Installation

### Step 1: Install CircuitPython
1. Download the appropriate `.uf2` file for your board from [circuitpython.org](https://circuitpython.org/downloads)
2. Hold the BOOTSEL button while plugging in your board
3. Drag the `.uf2` file to the RPI-RP2 drive that appears
4. Board will reboot and mount as CIRCUITPY

### Step 2: Install Libraries
1. Download the [library bundle](https://github.com/adafruit/Adafruit_CircuitPython_Bundle/releases) matching your CircuitPython version
2. Extract and copy the required libraries to `CIRCUITPY/lib/`

### Step 3: Upload Code
1. Copy `code.py` to the root of the CIRCUITPY drive
2. **Important:** If you want to use `main.py` instead, delete `code.py` first (CircuitPython prioritizes `code.py`)

## Pin Configuration

### Default Pin Assignments

| Board | Button Pin | NeoPixel Pin | Built-in LED |
|-------|-----------|--------------|--------------|
| RP2040-Zero | GP14 | GP16 | N/A |

**Note:** Pin assignments can be customized in the code. See [Customization](#customization) section.

## Wiring

### Basic Button Connection
```
Button Pin 1 ──┐
               │
              [ ] Button
               │
Button Pin 2 ──┴── GND
```

- Connect one button terminal to your chosen GPIO pin
- Connect the other terminal to any GND pin
- Internal pull-up resistor is enabled in software

### Optional External LED
```
GPIO Pin ──→ [220Ω Resistor] ──→ LED(+) ──→ LED(-) ──→ GND
```

## Usage

### Basic Operation
1. Plug the board into any USB port
2. The computer will recognize it as a USB mouse
3. Press the button to generate a left-click
4. LED/NeoPixel provides visual feedback

### File Naming
- **Default:** Use `code.py` - runs automatically on boot
- **Alternative:** Use `main.py` - must remove `code.py` first
- CircuitPython checks for `code.py` before `main.py`

## Customization

### Changing the Button Pin
Edit the pin assignment in `code.py`:
```python
button = digitalio.DigitalInOut(board.GP15)  # Change GP15 to your pin
```

### Adjusting Click Delay
Modify the debounce timing:
```python
time.sleep(0.1)  # Increase for slower response, decrease for faster
```

### Changing LED Color (NeoPixel)
```python
pixels.fill((255, 0, 0))  # Red
pixels.fill((0, 255, 0))  # Green
pixels.fill((0, 0, 255))  # Blue
pixels.fill((255, 255, 0))  # Yellow
```

### Multiple Click Types
You can modify the code to support:
- Double-clicks
- Right-clicks
- Middle-clicks
- Click and drag

Example:
```python
mouse.click(Mouse.RIGHT_BUTTON)  # Right-click instead
```

## Troubleshooting

| Problem | Possible Cause | Solution |
|---------|---------------|----------|
| Board not detected | CircuitPython not installed | Reinstall CircuitPython .uf2 file |
| No clicks generated | Wrong button wiring | Verify button connects GPIO to GND |
| | Wrong pin in code | Check pin assignment matches wiring |
| NeoPixel doesn't light | Missing neopixel library | Copy `neopixel.mpy` to `lib/` folder |
| | Wrong NeoPixel pin | Verify `NEOPIXEL` pin for your board |
| Code doesn't run | File not named correctly | Ensure file is `code.py` or `main.py` |
| | `code.py` blocks `main.py` | Delete `code.py` to run `main.py` |
| Erratic clicking | Button bounce | Increase debounce delay |
| Computer freezes | Infinite loop in code | Fix code logic, reload board |

### Getting Help
- Check the [CircuitPython forums](https://forums.adafruit.com/viewforum.php?f=60)
- Review [CircuitPython HID documentation](https://docs.circuitpython.org/projects/hid/en/latest/)
- Open an issue on this repository

## Advanced Features

### Potential Enhancements
- **Multiple buttons** - Different click types or macros
- **Keyboard combos** - Ctrl+Click, Shift+Click, etc.
- **Auto-clicker mode** - Toggle continuous clicking
- **Click counter** - Track number of clicks
- **Battery power** - Use with LiPo battery for portable operation
- **Wireless** - Bluetooth HID with Pico W

### Example: Adding a Second Button
```python
button2 = digitalio.DigitalInOut(board.GP14)
button2.direction = digitalio.Direction.INPUT
button2.pull = digitalio.Pull.UP

if not button2.value:
    mouse.click(Mouse.RIGHT_BUTTON)  # Right-click
```

## Project Structure
```
mouse-click/
├── code.py              # Main program file
├── README.md            # This file
├── LICENSE              # Project license
└── lib/                 # Required libraries (not included)
    ├── adafruit_hid/
    └── neopixel.mpy
```

## Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Built with [CircuitPython](https://circuitpython.org/)
- Uses [Adafruit HID Library](https://github.com/adafruit/Adafruit_CircuitPython_HID)
- Inspired by accessibility and automation needs


