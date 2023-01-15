import board

from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.matrix import DiodeOrientation
from kmk.matrix import intify_coordinate as ic

_KEY_CFG = [
    board.GP6,board.GP7,board.GP8,board.GP9,
    board.GP26,board.GP22,board.GP21,
    board.GP20,board.GP19,board.GP18
           ]

class MyKeyboard(KMKKeyboard):
    def __init__(self):
        # create and register the scanner
        self.matrix = KeysScanner(
            # require argument:
            pins=_KEY_CFG,
            # optional arguments with defaults:
            value_when_pressed=False,
            pull=True,
            interval=0.02,  # Debounce time in floating point seconds
            max_events=64
        )

    diode_orientation = DiodeOrientation.COL2ROW
    #led_pin = board.P1_06
    #rgb_pixel_pin = board.P0_06
    #rgb_num_pixels = 12
    #data_pin = board.SDA
    #data_pin2 = board.SCL
    #i2c = board.I2C
    #powersave_pin = board.P0_13

    # NOQA
    # flake8: noqa
    coord_mapping = [
      0, 1, 2,      4, 5, 6, 7,
             3,       8, 9, 10,
                     11, 12, 13,
                ]
