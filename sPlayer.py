# -*- coding: utf-8 -*-
import spotify
import time
import random
import threading
import serial

end_of_track = threading.Event()

class spotifyPlayer:

    def __init__(self):

        def on_end_of_track(self):
            end_of_track.set()
            print "End of track", end_of_track.isSet()

        self.session = spotify.Session()
        self.session.login('klevemar', '#TDT*4262', True)
        while self.session.connection.state != True :
            self.session.process_events()
            pass
        audio = spotify.PortAudioSink(self.session)
        loop = spotify.EventLoop(self.session)
        loop.start()
        self.end_of_track = end_of_track 
        self.session.on(spotify.SessionEvent.END_OF_TRACK, on_end_of_track)

    def generate_playlist(self,q):
        random_start = random.randint(0,10)
        #print "random start", random_start
        random_amount = random.randint(40,100)
        search = self.session.search(q, None, random_start, random_amount)
        search.load()
        return search.tracks

    def play_song(self, track):
        track.load()
        artists = track.artists
        print 'Track name:', track.name
        for i in artists:
            print 'Artist:',i.name
        print 'Album:', track.album.name
        self.session.player.load(track)
        self.session.player.play()
        self.session.process_events()

    def check_playing(self):
        self.session.process_events()
        return self.session.player.state

    def stop(self):
        self.session.player.unload()

    def play_playlist(self,query):
        playlist = self.generate_playlist(query)
        len_playlist = len(playlist)
        print 'Lenght playlist:', len_playlist
        random_song = random.randint(0,(len_playlist-1))
        #print 'Random song:',random_song
        song = playlist[random_song]
        self.play_song(song)
        while 1:
            if self.end_of_track.isSet():
                new_random_song = random.randint(0,(len_playlist-1))
                if new_random_song != random_song:
                    random_song = new_random_song
                else:
                    random_song = new_random_song-1
                self.play_song(playlist[random_song])
                self.end_of_track.clear()
            
    def change_genre(self,state):
        self.stop()
        if state == 'a':
            self.play_playlist('genre:EDM')
        elif state == 'b':
            self.play_playlist('genre:"singer/songwriter"')
        elif state == 'c':
            self.play_playlist('genre:"big band"')
        elif state == 'd':
            self.play_playlist('genre:ambient')
        elif state == 'e':
            self.play_playlist('genre:blues')
        elif state == 'f':
            self.play_playlist('genre:classical')
        elif state == 'g':
            self.play_playlist('genre:funk')
        elif state == 'h':
            self.play_playlist('genre:jazz')
        elif state == 'i':
            self.play_playlist('genre:reggae')
        elif state == 'j':
            self.play_playlist('genre:pop')
        elif state == 'k':
            self.play_playlist('genre:metal')
        elif state == 'l':
            self.play_playlist('genre:R&B')
        elif state == 'm':
            self.play_playlist('genre:"hip-hop"')
        elif state == 'n':
            self.play_playlist('genre:soul')
        elif state == 'o':
            self.play_playlist('genre:world')
        elif state == 'p':
            self.play_playlist('genre:electronica')
        elif state == 'q':
            self.play_playlist('genre:dubstep')
        elif state == 'r':
            self.play_playlist('genre:hardrock')
        elif state == 's':
            self.play_playlist('genre:indierock')
