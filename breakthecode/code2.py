#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tkinter import *
#from tkinter import messagebox

__author__ = "Daniel Merelas"
__license__ = "GNU3"
__version__ = "1.0"
__email__ = "daniel@merelas.es"

# Bangalore, India
# 2017/02/25
# Automated solution for the game for kids called "break the code" offered by CIA (Central Intelligence Agency)
# https://www.cia.gov/kids-page/games/break-the-code/code-2.html


def ciacode2():
    ciphertext = cipherentry.get()

    textentry.delete(0, END)
    plaintext = ''
    pos = 1

    for i in ciphertext:
        temp = pos
        temp %= 3

        if temp == 0:
            plaintext += ciphertext[ciphertext.index(i)]

        pos += 1

    textentry.insert(1, plaintext)
    return


# Window instance
window = Tk()
window.title('CIA Solution exercise 2 - v' + __version__ )
window.resizable(False, False)

# Centering the window in the screen
w = window.winfo_reqwidth()
h = window.winfo_reqheight()
ws = window.winfo_screenwidth()
hs = window.winfo_screenheight()
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)
window.geometry('+%d+%d' % (x, y))

# Variables
fciphertext = StringVar()

# Cipher text
cipherlabel = Label(window, text="Cipher text:")
cipherlabel.grid(column=1, row=1, sticky=(W, E))
cipherentry = Entry(window, width=50)
cipherentry.grid(column=2, row=1, sticky=(W, E))

# Plain text
textlabel = Label(window, text="Plain text:")
textlabel.grid(column=1, row=2, sticky=(W, E))
textentry = Entry(window, width=50)
textentry.grid(column=2, row=2, sticky=(W, E))

# Button
cipherbutton = Button(window, text="Decipher", command=ciacode2)
cipherbutton.grid(column=2, row=3, sticky=(W, E))

window.mainloop()
