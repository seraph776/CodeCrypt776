#!/usr/bin/env python3
"""
created: 2022-07-05 11:19:36
@author: seraph776
contact: admin@codecrypt76.com
project: Playlist Class
metadoc: From 101 Computer.Net
license: None
"""

from playlist import PlayList, Track


def main():
    # Initialize Playlist:
    mp3_playlist = PlayList('MyCoolMusic', 'saved_music_file.txt')

    # Check if empty:
    print(mp3_playlist.is_empty())  # True

    # Load playlist from textfile:
    mp3_playlist.load_playlist()

    # Remove a track by title
    mp3_playlist.remove_track('one')

    # Add a new track:
    track = Track('metallica', 'the unforgiven', '6:23')
    mp3_playlist.add_track(track)

    # Informs user if file cannot be found:
    mp3_playlist.remove_track('bogus_file')  # File cannot be located!

    # Shuffles list n x times:
    mp3_playlist.shuffle_playlist(3)

    # Get total number of tracks:
    mp3_playlist.get_number_of_tracks()

    # Get total duration of playlist
    mp3_playlist.get_total_duration()

    # Save Playlist and filename by name designated at instance initialization
    mp3_playlist.save_playlist()

    # Create a file with a new custom file_name:
    mp3_playlist.save_playlist('backup_copy.txt')


if __name__ == '__main__':
    main()
