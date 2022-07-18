#!/usr/bin/env python3
"""
created: 2022-07-18 13:39:39
@author: seraph★776
contact: admin@codexguru.com
project: My Playlist
metadoc: 
"""

from collections import namedtuple

MusicFile = namedtuple('MusicFile', ['music_title', 'artist', 'duration'])


def get_file(filename):
    with open(filename) as fo:
        playlist = [i.strip().split(';') for i in fo]
    return playlist


def get_playlist():
    output = []

    playlist_file = get_file('playlist.txt')

    for song in playlist_file:
        music_title, artist, duration = song[0], song[1], song[2]
        track = MusicFile(music_title, artist, duration)
        output.append(track)
    return output


if __name__ == '__main__':
    my_playlist = get_playlist()
    print(my_playlist)
