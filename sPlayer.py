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

        # Event function checking that login is complete
        def connection_state_listener(session):
            if session.connection.state is spotify.ConnectionState.LOGGED_IN:
                logged_in_event.set()

        # Login
        session.on(
            spotify.SessionEvent.CONNECTION_STATE_UPDATED,
            connection_state_listener)

        session.login('klevemar', '#TDT*4262')
        while not logged_in_event.wait(0.1):
            session.process_events()  # waits until the login is complete

        #Creating instances of the class
        self.playlist = Playlist(session)
        self.player = Player(session, self.playlist)
        self.currentTrack = None
        self.currentPlaylist = None

<<<<<<< Updated upstream
=======
        #Scrobbling to last.fm
        """social = spotify.social.Social(session)
        social.set_social_credentials(2, 'klevemar', '#TDT*4262')
        print social.set_scrobbling(2, 4)"""

>>>>>>> Stashed changes
        # Create playlist
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

<<<<<<< Updated upstream
        # Handle next song in the same playlist
        session.on(
            spotify.SessionEvent.END_OF_TRACK, 
            self.player.next_song)
=======
        # Handle next song within the same playlist
        session.on(
            spotify.SessionEvent.END_OF_TRACK, 
            self.next_song_in_playlist)
>>>>>>> Stashed changes

    def play_playlist(self, genre):
        #start_time = time.time()
        self.playlist = genre
        self.currentTrack = self.player.next_song(self.playlist)
        #print 'Time elapsed: ' + str(time.time() - start_time)
<<<<<<< Updated upstream
        
=======
  
>>>>>>> Stashed changes
    def change_genre(self, state):
        if state == 'a':
            self.currentPlaylist = self.edm
            self.play_playlist(self.currentPlaylist)
        elif state == 'b':
            self.currentPlaylist = self.singerSongwriter
            self.play_playlist(self.currentPlaylist)
        elif state == 'c':
            self.currentPlaylist = self.bigBand
            self.play_playlist(self.currentPlaylist)
        elif state == 'd':
            self.currentPlaylist = self.ambient
            self.play_playlist(self.currentPlaylist)
        elif state == 'e':
            self.currentPlaylist = self.blues
            self.play_playlist(self.currentPlaylist)
        elif state == 'f':
            self.currentPlaylist = self.classical
            self.play_playlist(self.currentPlaylist)
        elif state == 'g':
            self.currentPlaylist = self.funk
            self.play_playlist(self.currentPlaylist)
        elif state == 'h':
            self.currentPlaylist = self.jazz
            self.play_playlist(self.currentPlaylist)
        elif state == 'i':
            self.currentPlaylist = self.reggae
            self.play_playlist(self.currentPlaylist)
        elif state == 'j':
            self.currentPlaylist = self.pop
            self.play_playlist(self.currentPlaylist)
        elif state == 'k':
            self.currentPlaylist = self.metal
            self.play_playlist(self.currentPlaylist)
        elif state == 'l':
            self.currentPlaylist = self.rnb
            self.play_playlist(self.currentPlaylist)
        elif state == 'm':
            self.currentPlaylist = self.hipHop
            self.play_playlist(self.currentPlaylist)
        elif state == 'n':
            self.currentPlaylist = self.soul
            self.play_playlist(self.currentPlaylist)
        elif state == 'o':
            self.currentPlaylist = self.world
            self.play_playlist(self.currentPlaylist)
        elif state == 'p':
            self.currentPlaylist = self.electronica
            self.play_playlist(self.currentPlaylist)
        elif state == 'q':
            self.currentPlaylist = self.dubstep
            self.play_playlist(self.currentPlaylist)
        elif state == 'r':
            self.currentPlaylist = self.hardrock
            self.play_playlist(self.currentPlaylist)
        elif state == 's':
            self.currentPlaylist = self.indierock
            self.play_playlist(self.currentPlaylist)
        elif state == 't':

            print "Stopped"
            self.player.stop()
        elif state =='u':
            if not self.currentTrack == None:
                self.player.add_to_starred(self.currentTrack)
<<<<<<< Updated upstream
            

=======

    def next_song_in_playlist(self, s=None):
        self.player.stop()
        self.currentTrack = self.player.next_song(self.currentPlaylist)  
            
>>>>>>> Stashed changes
class Player(object):
    def __init__(self, session, playlist):
        assert isinstance(session, spotify.Session)
        assert isinstance(playlist, Playlist)

        self.session = session
        self.playlist = playlist
<<<<<<< Updated upstream
        self.currentTrack = None
        self.currentPlaylist = None
=======
        #self.currentTrack = None
        #self.currentPlaylist = None
>>>>>>> Stashed changes

        self.audio = spotify.PortAudioSink(session)

    def stop(self):
        self.session.player.unload()

<<<<<<< Updated upstream
    def next_song(self, genre, s = None): #Må det stå s = None her?
        self.stop()
        self.currentPlaylist = genre
=======
    def next_song(self, genre, s=None): #Må det stå s = None her?
        self.stop()
        #self.currentPlaylist = genre
>>>>>>> Stashed changes
        self.currentTrack = self.playlist.next_song(genre)
        self.play_song(self.currentTrack)
        return self.currentTrack

    def play_song(self, track):
        track.load()
        print ''
        try: 
            print 'Track name: {0}'.format(track.name)
            print'Artist(s): {0}'.format(', '.join([str(artist.name) for artist in track.artists]))
            print 'Album: {0}'.format(track.album.name)
        except UnicodeEncodeError:
            print track.name
        self.session.player.load(track)
        self.session.player.play()
        self.session.process_events()

    def add_to_starred(self, track):
        if track.starred:
            print '"{0}" already starred'.format(track.name)
        else:
            track.starred = True
            print '"{0}" starred'.format(track.name)

class Playlist(object):
    def __init__(self, session):
        self.index = 0
        self.session = session
        self.playlist = list()
<<<<<<< Updated upstream
        self.genre = None
        self.currentPlaylist = None
=======
        #self.genre = None
        #self.currentPlaylist = None
>>>>>>> Stashed changes

    def new_playlist(self, genre):
        random_start = random.randint(0, 10)
        random_amount = random.randint(40, 100)
        search = self.session.search(genre, None, random_start, random_amount)
        search.load()
        return search.tracks
        
    def next_song(self, genre):
<<<<<<< Updated upstream
        self.playlist = genre
        self.currentPlaylist = genre
        song = self.playlist[self.index]
        self.index += 1
        if self.index >= len(self.playlist):
            self.index = 0
=======
        self.index = random.randint(1,len(genre))
        song = genre[self.index]
>>>>>>> Stashed changes
        return song
