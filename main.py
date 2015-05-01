# -*- coding: utf-8 -*-
import serial
from sPlayer import SpotifyPlayer

player = SpotifyPlayer()

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't']
port = serial.Serial("/dev/tty.usbmodem1421", 9600, timeout=10)
#port = serial.Serial("/dev/tty.usbmodem1411", 9600, timeout=10)

def read():
    if (port.inWaiting() > 0):
        line = port.readline()
        line = line.rstrip()
        if line in letters:
            return line
    return None

previousState = 0

while True:
    state = read()
    if state is not None:
        if not previousState == state:
            player.change_genre(state)
        previousState = state
