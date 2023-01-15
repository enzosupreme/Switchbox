import time
import random
import rotaryio
import board
import usb_hid
import busio
import digitalio
from digitalio import DigitalInOut, Direction, Pull
from adafruit_debouncer import Debouncer
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.modules.layers import Layers
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
import terminalio
from kmk.extensions.LED import LED
import board
from adafruit_display_text import label
from adafruit_hid.keycode import Keycode
import adafruit_ssd1306
from kmk.extensions.media_keys import MediaKeys
from adafruit_hid.consumer_control import ConsumerControl
from adafruit_hid.consumer_control_code import ConsumerControlCode
from switchbox_config import SwitchBox
from kmk.scanners import DiodeOrientation
from kmk.modules.encoder import EncoderHandler


klor_oled    = True
encoder_handler = EncoderHandler()
layers = Layers()
keyboard = SwitchBox(klor_oled)
kbd = Keyboard(usb_hid.devices)
cc = ConsumerControl(usb_hid.devices)
keyboard.extensions.append(MediaKeys())

encoder_handler.pins = ((board.GP12, board.GP11, board.GP13, False),)
led_ext = LED(led_pin=[board.GP2,board.GP3,board.GP4,board.GP5])
keyboard.extensions.append(led_ext)
keyboard.modules = [layers, encoder_handler]


while True:
    #title()

    keyboard.keymap = [
        #Dreamcast
        [
         KC.A, KC.S, KC.D,     KC.MPLY,KC.MEDIA_NEXT_TRACK,KC.N1,KC.N5,
                              KC.W,        KC.N8, KC.N9, KC.N0,
                                            KC.U, KC.I, KC.O,

        ],
        #Street Fighter Anniversary
        [
         KC.LEFT, KC.DOWN, KC.RIGHT,     KC.MPLY,KC.MEDIA_NEXT_TRACK,KC.BSPACE,KC.ENTER,
                              KC.UP,        KC.A, KC.S, KC.D,
                                            KC.Z, KC.X, KC.C,

        ],
        #Media
        [
         KC.VOLD, KC.PGDOWN, KC.VOLU,     KC.MSTP,KC.MUTE,KC.MRWD,KC.MFFD,
                              KC.PGUP,        KC.MPRV, KC.MPLY, KC.MNXT,
                                            KC.VOLD, KC.MUTE, KC.VOLU,

        ]

    ]

    encoder_handler.map = [ ((KC.TO(2), KC.TO(1), KC.MUTE),), #Bear/NullDC
                        ((KC.TO(0), KC.TO(2), KC.MUTE),),  #Street Fighter Anniversary
                        ((KC.TO(1), KC.TO(0), KC.MUTE),),
                        ]

    if __name__ == '__main__':
        keyboard.go()



