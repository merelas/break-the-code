#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tkinter import *
#from tkinter import messagebox

__author__ = "Daniel Merelas"
__license__ = "GNU3"
__version__ = "1.0"
__email__ = "daniel@merelas.es"

# Madrid, España
# 2018/06/15
# Automated solution for the game for kids called "break the code" offered by CIA (Central Intelligence Agency)
# https://www.cia.gov/kids-page/games/break-the-code/code-3.html


def ciacode3():
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

  plaintext = str.lower(textentry.get())
    key = int(keyentry.get())

    cipherentry.delete(0, END)
    ciphertext = ''

    abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
           'v', 'w', 'x', 'y', 'z', ' ']
    number = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]

    for i in plaintext:
        pos = abc.index(i)
        
        if pos == 26:
            ciphertext += ' '
            continue
            
        temp = number[pos] + key
        temp %= 25
        ciphertext += abc[temp]

    cipherentry.insert(1, ciphertext)
    return



# Window instance
window = Tk()
window.title('CIA Solution exercise 3 - v' + __version__ )
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
cipherbutton = Button(window, text="Decipher", command=ciacode3)
cipherbutton.grid(column=2, row=3, sticky=(W, E))

window.mainloop()
