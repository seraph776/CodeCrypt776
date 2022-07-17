#!/usr/bin/env python3
"""
created: 2022-07-05 11:19:36
@author: seraph776
contact: admin@codecrypt76.com
project: Playlist Class
metadoc: From 101 Computer.Net
license: None
"""

import os
import sys
import datetime
from random import shuffle
from track import Track


class PlayList:
    """A Playlist class."""

    def __init__(self, title: str, filename: str) -> None:
        """Initialize attributes."""
        self.title = title
        self.filename = filename
        self.tracks: list[Track]= []

    def __repr__(self) -> str:
        """String representation the class."""
        return f'{self.__class__.__name__}(title={self.title}, filename={self.filename}, tracks={self.tracks})'

    def load_playlist(self):
        """Loads a saved playlist, and displays its contents"""
        if not os.path.isfile(os.path.join('music_files', self.filename)):
            print(f'{self.title} could not be loaded.\n{self.filename} does not exists!', file=sys.stderr)
        else:
            with open(os.path.join('music_files', self.filename)) as file_obj:
                song_list = [i.strip().split(',') for i in file_obj]
            for song in song_list:
                self.add_track(Track(song[0], song[1], song[2]))
            self.show_playlist()

    def save_playlist(self, filename=None):
        """Saves the current playlist in a textfile"""
        self.filename = self.filename if filename is None else filename

        with open(os.path.join('music_files', self.filename), 'w+') as file_object:
            for track in self.tracks:
                song, artist, duration = track.title, track.artist, track.duration
                file_object.write(f'{song},{artist},{duration}' + '\n')
        print(f'{self.title} has been successfully saved.')

    def add_track(self, track):
        """Add a single track to the playlist."""
        self.tracks.insert(0, track)
        print(f'"{track.title}" has been added successfully!')

    def remove_track(self, track_name):
        """Removes a track from the playlist"""
        is_located = False
        for i, track in enumerate(self.tracks):
            if track_name == track.title:
                self.tracks.pop(i)
                print(f'"{track_name}" has been successfully removed.')
                is_located = True
        if not is_located:
            print(f'"{track_name}" could not be located. Please try again.')

    def show_playlist(self):
        """Displays entire playlist, including title, artist, and duration."""
        if self.tracks:
            print('Track list:')
            for track in self.tracks:
                song, artist, duration = track.title, track.artist, track.duration
                print(f'\t• {song} - {artist} ({duration})')
        else:
            print('Track list is empty!')

    def shuffle_playlist(self, n):
        """Shuffles playlist n x"""
        if self.tracks:
            for i in range(n):
                shuffle(self.tracks)
            print(f'Playlist was shuffled {n}xs!')
        else:
            print('Playlist could not be found.')

    def get_number_of_tracks(self):
        """Prints the total number of tracks stored in the playlist."""
        print(f'Total tracks: {len(self.tracks)}')

    def get_total_duration(self):
        """Prints the total duration time of all tracks."""
        current_year = datetime.datetime.now().year
        datetime_original = datetime.datetime(year=current_year, month=1, day=1)
        for track in self.tracks:
            minutes, seconds = [int(i) for i in track.duration.split(':')]
            datetime_original += datetime.timedelta(minutes=minutes, seconds=seconds)
        print('Total duration: {:%H:%M:%S}'.format(datetime_original))

    def reset_playlist(self):
        """Clears the playlist."""
        self.tracks.clear()
        print(f'{self.title} has been reset.')

    def is_empty(self):
        """Returns True if playlist is empty, False otherwise"""
        return len(self.tracks) == 0
