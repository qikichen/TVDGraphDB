import Pyro4
from src.tvgraph import TVGraph

@Pyro4.expose
class GraphServer:
    def __init__(self, _server_number, _data):
        self.data = _data
        self.server_number = _server_number

    def create_node_list(self):
        return None
    def create_graph(self):
        self.tv_graph = TVGraph()
        print("Graph added to: ", self.server_number)
        # Need to create nodes and then load onto the graph
        return None
        

        