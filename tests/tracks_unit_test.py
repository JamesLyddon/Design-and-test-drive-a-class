from lib.tracks import Tracks
import pytest

def test_instantiation():
    tracks = Tracks()
    assert isinstance(tracks, Tracks)

"""
Given a new Tracks object
track list is empty
"""
def test_check_track_list_empty_after_instantiation():
    tracks = Tracks()
    assert tracks.track_list == []

"""
Given a new track dictionary added to track list
track list contains new track
"""
def test_new_track_in_track_list_after_add_track():
    tracks = Tracks()
    tracks.add_track('chumbawumba', 'tubthumpin')
    assert tracks.track_list == [{'artist': 'chumbawumba', 'title': 'tubthumpin'}]

"""
Given 2 new track dictionaries added to track list
track list contains both track
"""
def test_two_new_tracks_in_track_list_after_add_track_twice():
    tracks = Tracks()
    tracks.add_track('chumbawumba', 'tubthumpin')
    tracks.add_track('haim', 'summer girl')
    assert tracks.show_all_tracks() == [{'artist': 'chumbawumba', 'title': 'tubthumpin'}, {'artist': 'haim', 'title': 'summer girl'}]

"""
Given empty artist 
Exception raised
"""
def test_empty_string_artist_input_exception_raised():
    tracks = Tracks()
    with pytest.raises(Exception) as e:
        tracks.add_track('', 'tubthumpin')
    error_message = str(e.value)
    assert error_message == "Artist field can't be empty"

"""
Given empty title
Exception raised
"""
def test_empty_string_title_input_exception_raised():
    tracks = Tracks()
    with pytest.raises(Exception) as e:
        tracks.add_track('chumbawumba', '')
    error_message = str(e.value)
    assert error_message == "Songtitle field can't be empty"
