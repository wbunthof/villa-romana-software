import board
import digitalio

from lib import statemachine
from lib.adafruit_hid.keyboard import Keyboard
from lib.adafruit_hid.keycode import Keycode


class button:
    def __init__(self,
                 btn: board,
                 led: board,
                 keyboard: Keyboard,
                 key_to_press: Keycode):
        # Set up button
        self._key_to_press = key_to_press
        self._keyboard = keyboard
        self._btn = digitalio.DigitalInOut(btn)
        self._btn.direction = digitalio.Direction.INPUT
        self._btn.pull = digitalio.Pull.UP

        # Set up led
        self._led = digitalio.DigitalInOut(led)
        self._led.direction = digitalio.Direction.OUTPUT
        self._led.value = False

        # Set up statemachine
        self._statemachine = statemachine.StateMachine(['BTN_released', 'BTN_pressed'])

    def BUTTON(self):
        if self._statemachine.getState() == 'BTN_released':
            if self._btn.value:
                self._led.value = True
                print('BTN1 pressed')
                self._statemachine.setState('BTN_pressed')

        elif self._statemachine.getState() == 'BTN_pressed':
            self._keyboard.press(self._key_to_press)
            if not self._btn.value:
                self._keyboard.release(self._key_to_press)
                self._led.value = False
                print('BTN1 released')
                self._statemachine.setState('BTN_released')
