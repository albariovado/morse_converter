import var
import subprocess as sp
from time import sleep

def encrypt(text):

    encrypted = ''

    for char in text:
        char = char.upper()
        if char != ' ':
            encrypted += var.MORSE_CODE_DICT[char]
            encrypted += ' '
        else:
            encrypted += '| '
    
    return encrypted

def play_morse(morse_text):

    for char in morse_text:

        if char == '.':
            sp.call(["afplay", var.SHORT])
        elif char == '-':
            sp.call(["afplay", var.LONG])
        elif char == '|':
            sleep(0.5)
        else:
            sleep(0.2)
    
    return