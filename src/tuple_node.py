import Pyro4

class TupleNode:
    def __init__(self, _movie, _data):
        self.movie = _movie # Movie Title
        self.data = _data # Data of the movie such as rating etc.
        self.edges = []
    
    def set_edges(self, edge_list):
        '''
        set the edges of each individual node
        '''
        self.edges =  edge_list
