import Pyro4

class TupleNode:
    def __init__(self, _movie, _data):
        self.movie = _movie # Movie Title
        self.data = _data # Data of the movie such as rating etc.
    
    def get_movie(self):
        return self.movie
    
    def get_data(self):
        return self.data

