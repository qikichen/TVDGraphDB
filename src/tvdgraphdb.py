import Pyro4
import collections
import heapq



class TVDGraphDB:
    def __init__(self):
        # self.schema = _schema
        # self.data = read_data
        self.adjacency_list = collections.defaultdict(list)
        self.buffer = []
        self.nodes = []
        # This will be where the distributed systems comes in. I want to seperate the clusters
        self.cluster_to_nodes = collections.defaultdict(list)

    def load_nodes(self, node_array):
        '''
        Load the self.nodes buffer
        '''
        self.nodes = node_array
    
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
                if candidate.get_movie() == current_node.get_movie() or candidate in visit:
                    continue
                distance = self.calculate_distances(current_node, candidate)
                distance_heap.append((distance, candidate))
            heapq.heapify(distance_heap)
            for _ in range(num_of_1st_deg_neighbor-len(self.adjacency_list[current_node])):
                #Processing the nearest neighbors and populate adjacency list
                current_neighbor,pop_node = heapq.heappop(distance_heap)
                self.adjacency_list[current_node].append(pop_node)
                q.append(pop_node)
                
    def get_adjacency_list(self):
        return self.adjacency_list


    
    
