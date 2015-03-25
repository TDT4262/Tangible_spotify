# -*- coding: utf-8 -*-
import spotify
#import time
import random

class spotifyPlayer:

	def __init__(self):
		self.session = spotify.Session()
		self.session.login('klevemar', '#TDT*4262', True)
		while self.session.connection.state != True :
			#print "connecting"
			self.session.process_events()
			pass
		audio = spotify.PortAudioSink(self.session)
	
	def generate_playlist(self,q):
		while self.session.connection.state == False :
			print "Waiting"

		random_start = random.randint(0,10)
		print "random start", random_start
		random_amount = random.randint(40,100)
		print "random amount", random_amount
		search = self.session.search(q, None, random_start, random_amount)
		search.load()
		return search.tracks

	def play_song(self, track):
		track.load()
		#duration = track.duration()
		self.session.player.load(track)
		print track.name, track.duration
		self.session.player.play()
		self.session.process_events()
		#return duration FUNKA IKKE

	def stop(self):
		self.session.player.unload()

	def play_playlist(self,query):
		playlist = generate_playlist(query)
		len_playlist = len(playlist)
		random_song = random.randint(0,(len_playlist-1))
		song = playlist[random_song]
		play_song(song)
		#Må klare å stoppe sangen når den er ferdig...

