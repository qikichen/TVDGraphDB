from src.tvgraph import TVDGraphDB
from src.tuple_node import TupleNode

def test_1():
    A = TupleNode("A", [0,1])
    B = TupleNode("B", [2,1])
    C = TupleNode("C", [-1,1])
    D = TupleNode("D", [-1,-1])
    E = TupleNode("E", [10,10])
    F = TupleNode("F", [11,10])
    G = TupleNode("G", [10,12])
    H = TupleNode("H", [-20,-20])

    movie_list = [A, B, C, D , E, F, G,H]

    db = TVDGraphDB()
    db.load_nodes(movie_list)
    db.create_network_graph(3)
    db.plot_network()
    db.print_adjacency()
    