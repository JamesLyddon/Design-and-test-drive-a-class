class Tracks:

    def __init__(self):
        # Parameters:
        #   none
        # Side effects:
        #   creates empty list
        self.track_list = []

    def add_track(self, artist, title):
        # Parameters:
        #   artist: string of artist's name
        #   title: sring of song title
        # Returns:
        #   Nothing
        # Side-effects
        #   adds track dictionary object to list of tracks
        if artist == "":
            raise Exception("Artist field can't be empty")
        if title == "":
            raise Exception("Songtitle field can't be empty")
        self.track_list.append({'artist': artist, 'title': title})

    def show_all_tracks(self):
        # Returns:
        #   a list of all track dictionaries added to track list
        # Side-effects:
        #   None
        return self.track_list