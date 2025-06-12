

## 1. Describe the Problem

As a user
So that I can keep track of my music listening
I want to add tracks I've listened to and see a list of them.

## 2. Design the Class Interface

_Include the initializer, public properties, and public methods with all parameters, return values, and side-effects._

```python
# EXAMPLE

class Tracks:
    # User-facing properties:
    #   name: string

    def __init__(self, name):
        # Parameters:
        #   none
        # Side effects:
        #   creates empty list
        pass # No code here yet

    def add_track(self, artist, title):
        # Parameters:
        #   artist: string of artist's name
        #   title: sring of song title
        # Returns:
        #   Nothing
        # Side-effects
        #   adds track dictionary object to list of tracks 
        pass # No code here yet

    def show_all_tracks(self):
        # Returns:
        #   a list of all track dictionaries added to track list
        # Side-effects:
        #   None
        pass # No code here yet
```

## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

``` python
# EXAMPLE

"""
Given a new Tracks object
track list is empty
"""
tracks = Tracks()
tracks.track_list # => []

"""
Given a new track dictionary added to track list
track list contains new track
"""
tracks = Tracks()
tracks.add_track({'artist': 'chumbawumba', 'title': 'tubthumpin'})
tracks.track_list # => [{'artist': 'chumbawumba', 'title': 'tubthumpin'}]

"""
Given 2 new track dictionaries added to track list
track list contains both track
"""
tracks = Tracks()
tracks.add_track({'artist': 'chumbawumba', 'title': 'tubthumpin'})
tracks.add_track({'artist': 'haim', 'title': 'summer girl'})
tracks.show_all_tracks() # => [{'artist': 'chumbawumba', 'title': 'tubthumpin'}, {'artist': 'haim', 'title': 'summer girl'}]
```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._
