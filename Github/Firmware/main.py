import board
import digitalio
from kmk.extensions.media_keys import MediaKeys
from kmk.handlers.sequences import send_string, simple_key_sequence
from kmk.keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.modules.layers import Layers
from kmk.modules.split_keyboards import Split, SplitSide
from kmk.scanners.keypad import KeysScanner
from kmk.scanners.matrix import MatrixScanner

# Initialize keyboard
keyboard = KMKKeyboard()

# Split keyboard configuration
split_side = SplitSide.LEFT  # Change to RIGHT for right half
split = Split(split_side=split_side)
keyboard.modules.append(split)

# Add layers support
keyboard.modules.append(Layers())

# Add media keys
keyboard.extensions.append(MediaKeys())

# Matrix configuration 
# ROWS and COLS 
keyboard.matrix = MatrixScanner(
    row_pins=(board.P0_04, board.P0_05, board.P0_06, board.P0_07, board.P0_08),
    col_pins=(board.P0_09, board.P0_10, board.P0_11, board.P0_12, board.P0_13, board.P0_14, board.P0_15),
)

# UART pins for split communication 
keyboard.uart_pin_tx = board.P1_06
keyboard.uart_pin_rx = board.P1_05

# Keymap 
keyboard.keymap = [
    [
        # Layer 0
        KC.ESC, KC.N1, KC.N2, KC.N3, KC.N4, KC.N5, KC.NO,
        KC.TAB, KC.Q, KC.W, KC.E, KC.R, KC.T, KC.NO,
        KC.CAPS, KC.A, KC.S, KC.D, KC.F, KC.G,
        KC.LSFT, KC.Z, KC.X, KC.C, KC.V, KC.B, KC.NO,
        KC.LCTL, KC.LALT, KC.LGUI, KC.MO(1), KC.SPC,
        
        # Right half
        KC.NO, KC.N6, KC.N7, KC.N8, KC.N9, KC.N0, KC.MINS,
        KC.NO, KC.Y, KC.U, KC.I, KC.O, KC.P, KC.BSLS,
        KC.H, KC.J, KC.K, KC.L, KC.SCLN, KC.QUOT,
        KC.NO, KC.N, KC.M, KC.COMM, KC.DOT, KC.SLSH, KC.RSFT,
        KC.ENT, KC.MO(1), KC.RGUI, KC.RALT, KC.RCTL,
    ]
]

if __name__ == '__main__':
    keyboard.go()