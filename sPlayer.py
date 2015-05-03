# -*- coding: utf-8 -*-
import spotify
import random
import threading
import time

class SpotifyPlayer(object):
    def __init__(self):

        # Events
        logged_in_event = threading.Event()

        # Create a Spotify session
        session = spotify.Session()
        session.preferred_bitrate(2)  # 160 kib/s
        loop = spotify.EventLoop(session)
        loop.start()

        # Event functions
        def connection_state_listener(session):
            if session.connection.state is spotify.ConnectionState.LOGGED_IN:
                logged_in_event.set()

        # Login
        session.on(
            spotify.SessionEvent.CONNECTION_STATE_UPDATED,
            connection_state_listener
        )
        session.login('klevemar', '#TDT*4262')
        while not logged_in_event.wait(0.1):
            session.process_events()  # waits until the login is complete

        # Create playlist
        self.playlist = Playlist(session)
        self.player = Player(session, self.playlist)

        print 'ok' 

        self.edm = self.playlist.new_playlist('genre:EDM')
        self.singerSongwriter = self.playlist.new_playlist('genre:"singer/songwriter"')
        self.bigBand = self.playlist.new_playlist('genre:"big band"')
        self.ambient = self.playlist.new_playlist('genre:ambient')
        self.blues = self.playlist.new_playlist('genre:blues')
        self.classical = self.playlist.new_playlist('genre:classical')
        self.funk = self.playlist.new_playlist('genre:funk')
        self.jazz = self.playlist.new_playlist('genre:jazz')
        self.reggae = self.playlist.new_playlist('genre:reggae')
        self.pop = self.playlist.new_playlist('genre:pop')
        self.metal = self.playlist.new_playlist('genre:metal')
        self.rnb = self.playlist.new_playlist('genre:R&B')
        self.hipHop = self.playlist.new_playlist('genre:"hip-hop"')
        self.soul = self.playlist.new_playlist('genre:soul')
        self.world = self.playlist.new_playlist('genre:world')
        self.electronica = self.playlist.new_playlist('genre:electronica')
        self.dubstep = self.playlist.new_playlist('genre:dubstep')
        self.hardrock = self.playlist.new_playlist('genre:hardrock')
        self.indierock = self.playlist.new_playlist('genre:indierock')
        print '100 % lastet, klar til bruk'

        # Handle next song in the same playlist
        session.on(spotify.SessionEvent.END_OF_TRACK, self.player.next_song)

    def play_playlist(self, genre):
        start_time = time.time()
        self.genre = genre
        self.player.next_song()
        print 'Time elapsed: ' + str(time.time() - start_time)
        
    def change_genre(self, state):
        if state == 'a':
            self.play_playlist(self.edm)
        elif state == 'b':
            self.play_playlist(self.singerSongwriter)
        elif state == 'c':
            self.play_playlist(self.bigBand)
        elif state == 'd':
            self.play_playlist(self.ambient)
        elif state == 'e':
            self.play_playlist(self.blues)
        elif state == 'f':
            self.play_playlist(self.classical)
        elif state == 'g':
            self.play_playlist(self.funk)
        elif state == 'h':
            self.play_playlist(self.jazz)
        elif state == 'i':
            self.play_playlist(self.reggae)
        elif state == 'j':
            self.play_playlist(self.pop)
        elif state == 'k':
            self.play_playlist(self.metal)
        elif state == 'l':
            self.play_playlist(self.rnb)
        elif state == 'm':
            self.play_playlist(self.hipHop)
        elif state == 'n':
            self.play_playlist(self.soul)
        elif state == 'o':
            self.play_playlist(self.world)
        elif state == 'p':
            self.play_playlist(self.electronica)
        elif state == 'q':
            self.play_playlist(self.dubstep)
        elif state == 'r':
            self.play_playlist(self.hardrock)
        elif state == 's':
            self.play_playlist(self.indierock)
        elif state == 't':
            print "Stopped"
            self.player.stop()
        elif state =='u':
            self.player.add_to_starred(self.track)

class Player(object):
    def __init__(self, session, playlist):
        assert isinstance(session, spotify.Session)
        assert isinstance(playlist, Playlist)

        self.session = session
        self.playlist = playlist

        self.audio = spotify.PortAudioSink(session)

    def stop(self):
        self.session.player.unload()

    def next_song(self, s=None): #hvorfor s=None, må den være der?
        self.stop()
        self.play_song(self.playlist.next_song())

    def play_song(self, track):
        track.load()
        print 'Track name: {0}'.format(track.name)
        print'Artist(s): {0}'.format(', '.join([str(artist.name) for artist in track.artists]))
        #print 'Album: {0}'.format(track.album.name)
        self.session.player.load(track)
        self.session.player.play()
        self.session.process_events()

    def add_to_starred(self, track):
        track.starred = True
        print 'Track starred'

class Playlist(object):
    def __init__(self, session):
        self.index = 0
        self.session = session
        self.playlist = list()
        self.genre = None

    def new_playlist(self, genre):
        self.genre = genre

        random_start = random.randint(0, 10)
        random_amount = random.randint(40, 100)

        search = self.session.search(genre, None, random_start, random_amount)
        search.load()
        self.playlist = search.tracks
        
    def next_song(self):
        #if not self.playlist:
            #return None
        song = self.playlist[self.index]
        self.index += 1
        if self.index >= len(self.playlist):
            self.index = 0
        return song
