import board
import busio
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner


_KEY_CFG = [
    board.GP14,board.GP15,board.GP16,       board.GP6,board.GP7,board.GP8,board.GP9,
                                board.GP17,     board.GP26,board.GP22,board.GP21,
                                                board.GP20,board.GP19,board.GP18
           ]


class SwitchBox(KMKKeyboard):

    def __init__(self,klor_oled):
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



        self.setup_oled(klor_oled)

    SCL = board.GP1
    SDA = board.GP0
    #i2c = busio.I2C(SCL,SDA)

    def setup_oled(self, klor_oled):
        if klor_oled == True:
            from kmk.extensions.peg_oled_Display import Oled,OledDisplayMode,OledReactionType,OledData

            oled_ext = Oled(
                OledData(
                    corner_one={0:OledReactionType.STATIC,1:["SwitchBox"]},                     # | Adjust these lines
                    corner_two={0:OledReactionType.LAYER,1:["Dreamcast","SFighter","Media"]},                  # | when you add more
                    corner_three={0:OledReactionType.LAYER,1:["  Pause Next 1 5","Pause Next BSPC Enter","  Stop Mute RR FF"]},     # | layers to your keyboard.keymap
                    corner_four={0:OledReactionType.LAYER,1:["     8 9 0\n     U I O","     A S D\n     Z X C","Prev Pause Next\nVolD Mute VolU"]}        # | in main.py
                    ),
                    toDisplay=OledDisplayMode.TXT,
                    flip=False,
                    oHeight=64,
            )
            self.extensions.append(oled_ext)

        coord_mapping = [
             1,2,3,     5,6,7,8,
                   4,    9,10,11,
                         12,13,14,
                        ]

