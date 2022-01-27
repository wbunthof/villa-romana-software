import board
import digitalio
import time
import statemachine
from lib.adafruit_hid.keyboard import Keyboard
from lib.adafruit_hid.keycode import Keycode


class HallEffectSensor:
    def __init__(self,
                 pin: board,
                 keyboard: Keyboard,
                 key_to_press: Keycode):
        self._key_to_press = key_to_press
        self._keyboard = keyboard
        self._hall = digitalio.DigitalInOut(pin)
        self._hall.direction = digitalio.Direction.INPUT
        self._hall.pull = digitalio.Pull.DOWN
        self._list_high_times = []
        self._average_list = []
        self._statemachine = statemachine.StateMachine(['Hall_low', 'Hall_high'])
        self._time_added_to_list = False
        self._amount_in_list = 8

    def HALLEFFECTSENSOR(self) -> float:

        # make list with the times at which the hall sensor goes high
        self.list_high_times()
        return len(self._list_high_times)

        # return round(speed, 1)

    def list_high_times(self):
        if self._statemachine.getState() == 'Hall_low':
            if not self._hall.value:
                print('Hall high')
                self._statemachine.setState('Hall_high')

                # delete first item from the list if necessary
                if len(self._list_high_times) >= self._amount_in_list:
                    self._list_high_times.pop(0)

                # add time to the list
                self._list_high_times.append(time.time())

        elif self._statemachine.getState() == 'Hall_high':
            self._keyboard.press(self._key_to_press)
            if self._hall.value:
                self._keyboard.release(self._key_to_press)
                print('Hall low')
                self._statemachine.setState('Hall_low')

    def compute_average(self):
        self._average_list.clear()
        shifted_list = self._list_high_times.copy()
        shifted_list.pop(0)
        for i, j in zip(self._list_high_times, shifted_list):
            self._average_list.append(j - i)
        return sum(self._average_list) / len(self._average_list)