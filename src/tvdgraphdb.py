import Pyro4
import collections

class TVDGraphDB:
    def __init__(self, _schema):
        self.schema = _schema
        self.adjacency_list = collections.defaultdict(list)
        self.buffer = []

    def load_data(self, tuple_node):
        edge_list = tuple_node.edges
        for neighbor in edge_list:
            self.adjacency_list[tuple_node].append(neighbor)
    
    
