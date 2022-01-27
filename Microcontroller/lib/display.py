from busio import I2C
from microcontroller import pin

# Import the SSD1306 module.
from lib import adafruit_ssd1306 as adafruit_ssd1306


class Display:
    """"Abstraction layer for display"""

    # pylint: disable-msg=too-many-arguments
    def __init__(
            self,
            sda: pin,
            scl: pin,
            hsize=128,
            vsize=64
    ):
        self.i2c = I2C(sda=sda, scl=scl)
        self.display = adafruit_ssd1306.SSD1306_I2C(hsize, vsize, self.i2c)

        # clean the display
        self.display.fill(0)
        self.display.show()
        self.display.contrast(2)

    def speed(self, speed: float) -> None:
        """Set the speed on the display"""
        self.display.fill(0)
        self.display.text(str(speed), 30, 0, 1, size=6)
        self.display.text("KM/U", 40, 50, 1, size=2)
        self.display.show()


