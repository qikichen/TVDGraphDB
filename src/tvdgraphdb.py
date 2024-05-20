import Pyro4
import networkx as nx
import matplotlib.pyplot as plt
import os
import collections
import heapq



class TVDGraphDB:
    def __init__(self):
        # self.schema = _schema
        # self.data = read_data
        self.adjacency_list = collections.defaultdict(list)
        self.buffer = []
        self.nodes = [] # List of TupleNodes
        # This will be where the distributed systems comes in. I want to seperate the clusters
        self.cluster_to_nodes = collections.defaultdict(list)

    def get_adjacency_list(self):
        '''
        Return the adjacency list
        '''
        return self.adjacency_list
    
    def set_adjacency_list(self, adj):
        '''
        Set the adjacency list [There isn't much use for this as the adjacency list is built within the class]
        '''
        self.adjacency_list = adj
    
    def clear_adjacency_list(self, adj):
        '''
        Clear the adjacency list 
        '''
        self.adjacency_list.clear()


    def load_nodes(self, node_array):
        '''
        Load the self.nodes buffer
        '''
        self.nodes = node_array
    
    def clear_nodes(self):
        '''
        Clear the self.nodes buffer
        '''
        self.nodes.clear()
    
    def return_nodes(self):
        '''
        Returns self.nodes
        '''
        return self.nodes

    
    
    def calculate_distances(self, core, reference_point):
        '''
        Distance metric for calculating the nearest distance
        '''
        res = 0
        for i in range(len(core.data)):
            res += (core.data[i] - reference_point.data[i])**2
        return res


    def bfs_network(self, node,num_of_1st_deg_neighbor) -> None:
        '''
        Self made algorithm to create a network between TupleNodes by populating the adjacency list
        '''
        q = collections.deque()
        visit = set() 
        q.append(node)
        while q and len(visit) != len(self.nodes):
            current_node = q.popleft()
            visit.add(current_node)
            distance_heap = [] #This min heap will help us find the min distances 
            for candidate in self.nodes:
                #Calculate the distance between two nodes except self and populate the heap
                if candidate.get_movie() == current_node.get_movie() or candidate in visit:
                    continue
                distance = self.calculate_distances(current_node, candidate)
                distance_heap.append((distance, candidate))
            heapq.heapify(distance_heap)
            for _ in range(num_of_1st_deg_neighbor-len(self.adjacency_list[current_node])):
                #Processing the nearest neighbors and populate adjacency list
                current_neighbor,pop_node = heapq.heappop(distance_heap)
                if len(self.adjacency_list[pop_node]) != num_of_1st_deg_neighbor:
                    self.adjacency_list[current_node].append(pop_node)
                    self.adjacency_list[pop_node].append(current_node)
                    q.append(pop_node)

    def create_network_graph(self, num_of_1st_deg_neighbor):
        '''
        We have to run the bfs_network for each as to not miss any nodes
        '''
        for node in self.nodes:
            if len(self.adjacency_list[node]) != num_of_1st_deg_neighbor:
                self.bfs_network(node,num_of_1st_deg_neighbor)
                    
    def plot_network(self):
        '''
        Creates a plot of the network graph via movie titles
        '''
        # Create a graph object
        G = nx.Graph()
        # Add all nodes to the graph
        for node in self.adjacency_list.keys():
            G.add_node(node.get_movie())
        # Add edges from the adjacency list
        for node, neighbors in self.adjacency_list.items():
            for neighbor in neighbors:
                G.add_edge(node.get_movie(), neighbor.get_movie())
        # Draw graph and plot
        plt.figure(figsize=(8, 6))
        nx.draw(G, with_labels=True, node_color='skyblue', node_size=2000, edge_color='gray', font_size=15, font_weight='bold')
        # Ensure the save directory exists
        save_dir = '/app'
        os.makedirs(save_dir, exist_ok=True)
        # Save the plot to a file
        output_path = os.path.join(save_dir, 'graph.png')
        plt.savefig(output_path)

    def print_adjacency(self):
        '''
        Print out the adjacency list in a readable format
        '''
        for node, neighbors in self.adjacency_list.items():
            neighbors_movies = ', '.join(neighbor.get_movie() for neighbor in neighbors)
            print(f"{node.get_movie()}: {neighbors_movies}")



    
    
