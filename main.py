# -*- coding: utf-8 -*-
from sPlayer import spotifyPlayer
#from timer import Timer

#sensorinput kommer her

player = spotifyPlayer()
playlist = player.generate_playlist('genre:pop')
print "Playlist lenght:", playlist.__len__() #printer ut lengden på playlisten
player.play_song(playlist[1]) #Hvis du kaller denne i while loopen så vil den prøve å spille på nytt og på nytt og vil da ikke spille noe

#gjerne lag en funksjon dere kaller play_playlist i klassen eller her
#er ikke helt stabil så dere kan jo prøve å se om det er noen ting dere kan fikse.

while(1):
	pass