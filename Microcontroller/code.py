import board
import digitalio
import usb_hid
from microcontroller import pin

import lib.display as display
from lib.adafruit_hid.keyboard import Keyboard
from lib.adafruit_hid.keycode import Keycode
from lib.button import button
from lib.halleffectsensor import HallEffectSensor

keyboard = Keyboard(usb_hid.devices)
btn1 = button(board.GP15, board.GP10, keyboard, Keycode.A)
btn2 = button(board.GP14, board.GP11, keyboard, Keycode.D)
hallSensor1 = HallEffectSensor(board.GP16, keyboard, Keycode.W)
hallSensor2 = HallEffectSensor(board.GP17, keyboard, Keycode.W)
hallSensor3 = HallEffectSensor(board.GP18, keyboard, Keycode.W)
hallSensor4 = HallEffectSensor(board.GP19, keyboard, Keycode.W)
hallSensor5 = HallEffectSensor(board.GP20, keyboard, Keycode.W)

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT
led.value = False

# screen = display.Display(sda=pin.GPIO4, scl=pin.GPIO5)

# old_speed = 0
# speed = 0
try:
    while True:
        # Keycode.A
        led.value = True
        btn1.BUTTON()
        btn2.BUTTON()
        hallSensor1.HALLEFFECTSENSOR()
        hallSensor2.HALLEFFECTSENSOR()
        hallSensor3.HALLEFFECTSENSOR()
        hallSensor4.HALLEFFECTSENSOR()
        hallSensor5.HALLEFFECTSENSOR()
        # if hallSensor.HALLEFFECTSENSOR() > 2:
        #     speed = hallSensor.compute_average()
        # if not old_speed == speed:
        #     print(speed)
        #     screen.speed(speed)
        #     old_speed = speed
except:
    print("Error occurred")
    led.value = False
