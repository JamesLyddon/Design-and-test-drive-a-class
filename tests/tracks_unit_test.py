from lib.tracks import Tracks

def test_instantiation():
    tracks = Tracks()
    assert isinstance(tracks, Tracks)

"""
Given a new Tracks object
track list is empty
"""
# tracks = Tracks()
# tracks.track_list # => []

"""
Given a new track dictionary added to track list
track list contains new track
"""
# tracks = Tracks()
# tracks.add_track({'artist': 'chumbawumba', 'title': 'tubthumpin'})
# tracks.track_list # => [{'artist': 'chumbawumba', 'title': 'tubthumpin'}]

"""
Given 2 new track dictionaries added to track list
track list contains both track
"""
# tracks = Tracks()
# tracks.add_track({'artist': 'chumbawumba', 'title': 'tubthumpin'})
# tracks.add_track({'artist': 'haim', 'title': 'summer girl'})
# tracks.show_all_tracks() # => [{'artist': 'chumbawumba', 'title': 'tubthumpin'}, {'artist': 'haim', 'title': 'summer girl'}]