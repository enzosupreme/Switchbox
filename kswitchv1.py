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
from kmk.extensions.peg_oled_Display import (
    Oled,
    OledData,
    OledDisplayMode,
    OledReactionType,
)
#-------DISPLAY--------------#
i2c = busio.I2C(board.GP1,board.GP0)
display =adafruit_ssd1306.SSD1306_I2C(128,64,i2c)
#oled_display_data=OledData(image={0:OledReactionType.LAYER,1:["1.bmp","2.bmp","1.bmp","2.bmp"]})


#SCL=board.GP1
#SDA=board.GP0

encoder_handler = EncoderHandler()
layers = Layers()
keyboard = SwitchBox()
kbd = Keyboard(usb_hid.devices)
cc = ConsumerControl(usb_hid.devices)
keyboard.extensions.append(MediaKeys())

encoder_handler.pins = ((board.GP12, board.GP11, board.GP13, False),)

led_ext = LED(led_pin=[board.GP2,board.GP3,board.GP4,board.GP5])
keyboard.extensions.append(led_ext)
keyboard.modules = [layers, encoder_handler]
oled_ext = Oled(
    OledData(
        corner_one={0: OledReactionType.STATIC, 1: ['Layout']},
        corner_two={
            0: OledReactionType.LAYER,
            1: ['1', '2', '3'],
        },
        corner_three={
            0: OledReactionType.LAYER,
            1: ['base', 'raise', 'lower'],
        },
        corner_four={
            0: OledReactionType.LAYER,
            1: ['Dreamcast', 'Street Fighter', 'Media'],
        },
    ),
    toDisplay=OledDisplayMode.TXT,
    flip=False,
)
keyboard.extensions.append(oled_ext)
x = 5

def tekken8_key_display():
    display.fill(0)
    display.text("Tekken 8",35,x,1)
    display.text("1",40,25,1)
    display.text("2",70,25,1)
    display.text("3",40,45,1)
    display.text("4",70,45,1)
    display.show()

def sf6_key_display():
    display.fill(0)
    display.text("Street Fighter 6",25,x,1)
    display.text("LP",30,20,1)
    display.text("MP",60,20,1)
    display.text("HP",90,20,1)
    display.text("LK",30,40,1)
    display.text("MK",60,40,1)
    display.text("HK",90,40,1)

# ----- button switch ----- #
def button_display(press):
    if press is 0:
        display.fill(0)
        display.show()
        display.text("LP",60,30,1)
        display.show()
        time.sleep(0.0025)

    if press is 1:
        display.fill(0)
        display.show()
        display.text("MP",60,30,1)
        display.show()
        time.sleep(0.0025)

    if press is 2:
        display.fill(0)
        display.show()
        display.text("HP",60,30,1)
        display.show()
        time.sleep(0.0025)

    if press is 3:
        display.fill(0)
        display.show()
        display.text("LK",60,30,1)
        display.show()
        time.sleep(0.0025)

    if press is 4:
        display.fill(0)
        display.show()
        display.text("MK",60,30 ,1)
        display.show()
        time.sleep(0.0025)

    if press is 5:
        display.fill(0)
        display.show()
        display.text("HK",60,30,1)
        display.show()
        time.sleep(0.0025)

def title():
    for i in range(1,60,10):
        display.fill(0)
        display.text("SwitchBox",30,i,1)
        display.show()


while True:
    title()

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


