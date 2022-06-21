# A text-based Python program to convert Strings into Morse Code (text + audio).

import fun

text = input("What you want to say in Morse Code?\nText: ")

encrypted = fun.encrypt(text)
print(encrypted)

fun.play_morse(encrypted)