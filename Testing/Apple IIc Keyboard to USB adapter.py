import keypad
import board
import digitalio
import time

import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

caps_lock = digitalio.DigitalInOut(board.GP2)
caps_lock.switch_to_input(pull=digitalio.Pull.UP)

reset_button = digitalio.DigitalInOut(board.GP26)
reset_button.switch_to_input(pull=digitalio.Pull.UP)

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

km = keypad.KeyMatrix(
    row_pins=(
        board.GP27, 
        board.GP4, 
        board.GP5, 
        board.GP12,
        board.GP9,
        board.GP13,
        board.GP11,
        board.GP16,
        board.GP14,
        board.GP15
    ),
    column_pins=(
        board.GP10, 
        board.GP28, 
        board.GP7,
        board.GP6,
        board.GP17,
        board.GP18,
        board.GP19,
        board.GP20
    ),
)

ctrl_keys = keypad.Keys(  # add 5
    (
        board.GP0,
        board.GP1,
    ), 
    value_when_pressed=False, 
    pull=True)

appl_keys = keypad.Keys(  # add 13
    (
        board.GP3,
        board.GP8,
    ), 
    value_when_pressed=True, 
    pull=False)

KEYCODES = (
    Keycode.ESCAPE,
    Keycode.TAB,
    Keycode.A,
    Keycode.Z,
    None,
    Keycode.SHIFT,
    Keycode.CONTROL,
    None,
    Keycode.ONE,
    Keycode.Q,
    Keycode.D,
    Keycode.X,
    None,
    Keycode.COMMAND,
    Keycode.ALT,
    None,
    Keycode.TWO,
    Keycode.W,
    Keycode.S,
    Keycode.C,
    None,
    None,
    None,
    None,
    Keycode.THREE,
    Keycode.E,
    Keycode.H,
    Keycode.V,
    None,
    None,
    None,
    None,
    Keycode.FOUR,
    Keycode.R,
    Keycode.F,
    Keycode.B,
    None,
    None,
    None,
    None,
    Keycode.SIX,
    Keycode.Y,
    Keycode.G,
    Keycode.N,
    None,
    None,
    None,
    None,
    Keycode.FIVE,
    Keycode.T,
    Keycode.J,
    Keycode.M,
    Keycode.BACKSLASH,
    Keycode.GRAVE_ACCENT,
    Keycode.ENTER,
    Keycode.BACKSPACE,
    Keycode.SEVEN,
    Keycode.U,
    Keycode.K,
    Keycode.COMMA,
    Keycode.EQUALS,
    Keycode.P,
    Keycode.UP_ARROW,
    Keycode.DOWN_ARROW,
    Keycode.EIGHT,
    Keycode.I,
    Keycode.SEMICOLON,
    Keycode.PERIOD,
    Keycode.ZERO,
    Keycode.LEFT_BRACKET,
    Keycode.SPACEBAR,
    Keycode.LEFT_ARROW,
    Keycode.NINE,
    Keycode.O,
    Keycode.L,
    Keycode.FORWARD_SLASH,
    Keycode.MINUS,
    Keycode.RIGHT_BRACKET,
    Keycode.EQUALS,
    Keycode.RIGHT_ARROW
)

kbd = Keyboard(usb_hid.devices)
caps_last_state = caps_lock.value
caps_press = time.monotonic() + 1
caps_release = None

while True:
    
    if reset_button.value:
        led.value = False
    else:
        led.value = True

    caps_value = caps_lock.value
    if caps_last_state != caps_value and time.monotonic() > caps_press:
        caps_last_state = caps_value
        kbd.press(Keycode.CAPS_LOCK)
        caps_press = time.monotonic() + 1
        caps_release = time.monotonic() + .2

    if caps_release is not None:
        if time.monotonic() > caps_release:
            kbd.release(Keycode.CAPS_LOCK)
            caps_release = None

    event = km.events.get()
    if event:
        key_number = event.key_number
        if event.pressed:
            kbd.press(KEYCODES[key_number])
        if event.released:
            kbd.release(KEYCODES[key_number])
    
    event = ctrl_keys.events.get()
    if event:
        key_number = event.key_number + 5
        if event.pressed:
            kbd.press(KEYCODES[key_number])
        if event.released:
            kbd.release(KEYCODES[key_number])
    
    event = appl_keys.events.get()
    if event:
        key_number = event.key_number + 13
        if event.pressed:
            kbd.press(KEYCODES[key_number])
        if event.released:
            kbd.release(KEYCODES[key_number])
