import Pyro4
import collections


class TVDGraphDB:
    def __init__(self, read_data,_schema):
        self.schema = _schema
        self.data = read_data
        self.adjacency_list = collections.defaultdict(list)
        self.buffer = []
        self.nodes = []
        # This will be where the distributed systems comes in. I want to seperate the clusters
        self.cluster_to_nodes = collections.defaultdict(list)

    def load_data(self, tuple_node):
        '''
        Load the self.nodes buffer
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


    def create_network_graph(self, num_of_1st_deg_neighbor):
        '''
        Self made algorithm to create a network between TupleNodes by populating the adjacency list
        '''
        q = collections.deque()
        visit = set() 
        q.append(self.nodes[0])
        while q:
            current_node = q.popleft()
            visit.add(current_node)
            distance_heap = [] #This min heap will help us find the min distances 
            for candidate in self.nodes:
                #Calculate the distance between two nodes except self and populate the heap
                if candidate.movie == current_node.movie or current_node in visit:
                    continue
                distance = self.calculate_distances(current_node, candidate)
                distance_heap.append(distance)
            collections.heapq.heapify(distance_heap)
            for _ in range(num_of_1st_deg_neighbor-len(self.adjacency_list[current_node])):
                #Processing the nearest neighbors and populate adjacency list
                current_neighbor = collections.heapq.heappop(distance_heap)
                self.adjacency_list[current_node].append(current_neighbor)
                q.append(current_neighbor)
                
        


    
    
