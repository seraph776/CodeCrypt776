#!/usr/bin/env python3
"""
created: 2022-07-05 12:34:30
@author: seraph776
contact: admin@codecrypt76.com
project: MP3 Playlist Class
metadoc: The Track class, and a few tracks to preload the MP3 player. I now save the files to textfile, and
load the songs in a track object
license: None
"""


class Track:
    """A Track class"""

    def __init__(self, title, artist, duration):
        """Initialize attributes."""
        self.title = title
        self.artist = artist
        self.duration = duration

    def __repr__(self):
        return f'{self.__class__.__name__}(title={self.title}, artist={self.artist}, duration={self.duration} seconds)'


if __name__ == '__main__':
    # Initialize Tracks:
    track0 = Track('kunglim guli', 'yulduz usmanova', '3:45')
    track1 = Track('veridis quo', 'daft punk', '5:58')
    track2 = Track('tokyo', 'skeler', '3:39')
    track3 = Track("don't cry", "guns n' roses", '4:45')
    track4 = Track('no ordinary love', 'sade', '2:41')
    track5 = Track("solitude", "marion", '4:11')
    track6 = Track('when doves cry', 'prince', '3:45')
    track7 = Track('one', 'metallica', '7:27')
    track8 = Track("nobody's fool", 'cinderella', '4:23')
    track9 = Track('un simple histoire', 'thievery corporation', '3:45')
    track10 = Track('cruel summer', 'bananarama', '3:50')
    track11 = Track('in the air tonight', 'phil collins', '5:37')
    track12 = Track('hotel california', 'eagles', '6:30')
    track13 = Track('mea culpa', 'enigma', '5:02')

    # Initially this was used to preload the MP3 player. The player now loads from a textfile.
    pre_loader = [track0, track1, track2, track3, track4, track5, track6, track7, track8,
                  track9, track10, track11, track12, track13]
