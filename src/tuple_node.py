import Pyro4

class TupleNode:
    def __init__(self, _movie, _data):
        self.movie = _movie # Movie Title
        self.data = _data # Data of the movie such as rating etc.
    
    def get_movie(self):
        '''
        Returns the movie title
        '''
        return self.movie
    
    def get_data(self):
        '''
        Returns the data
        '''
        return self.data

