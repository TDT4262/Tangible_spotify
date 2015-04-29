# -*- coding: utf-8 -*-
from sPlayer import spotifyPlayer
import random
import serial
from threading import Thread
import threading

player = spotifyPlayer()
port = serial.Serial("/dev/tty.usbmodemfd121", 9600, timeout=10)
#port = serial.Serial("/dev/tty.usbmodem1411", 9600, timeout=10)
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s']

def read():
    if (port.inWaiting() > 0):
        line = port.readline()
        line = line.rstrip()
        if line in letters:
            return line

state = read()
previousState = 0

while(1):
    state = read()
    if state != None:
        if previousState != state:
            print state
            thread = Thread(target = player.change_genre, args = (state))
            thread.start()

        previousState = state
