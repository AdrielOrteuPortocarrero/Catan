from abc import ABC, abstractmethod
import networkx as nx
from networkHelp import show_graph
from typing import List, Tuple
#from resource import *
class Tile (ABC):
    def __init__(self, num: int, resource: str) -> None:
        self._type : str = resource
        self._num : int = num
        self._intersections : Intersection
    
    @property
    def num(self) -> int:
        return self._num
    @num.setter
    def num(self, new_num: int):
        self._num = new_num
    

class Intersection:
    
    def __init__(self, identifier: Tuple[int]):
        self._identifier : Tuple[int] = identifier
        self._resources : Tuple[str, str, str]
    
    def resource(self):
        pass
    


class Board:
    _num_deserts = 1
    _num_mountains = 3
    _num_clay_banks = 3
    _num_forests = 4
    _num_sheep_herds = 4
    _num_wheat_fields = 4
    def __init__(self, size):
        self._board = nx.Graph()
        #self.create_board(size=size)
    
    def create_layer(self, k: int, vertex_set: List[List[float]]) -> None:
        pass
    def add_new_layer_vertices(self, layer_description: List[List[float]]) -> None:
        pass
    def create_board(self, size: int) -> None:
        for l in range(size, 0, -1):
            new_vertices = [ [j for j in range(l)] for i in range(6)]
            self.add_new_layer_vertices(layer_description=new_vertices)
            self.create_layer(l, vertex_set=new_vertices)
    
    def make_branch(self, length: int, origin: Tuple[int, int, int]):
        # origin = (0,0,k')
        self._board.add_node(origin)
        margin = [origin]
        for i in range(length*2):
            if i%2 == 0:
                # extend()
                for j, node in enumerate(margin):
                    # create_new_name()
                    # margin[j] (old) = (M, L, B)
                    pre_node = margin[j]
                    margin[j] = (pre_node[0], pre_node[1]+1, pre_node[2])
                    ###
                    self._board.add_edge(node, margin[j])
            else:
                # add_layer()
                margin_prime = []
                for j, node in enumerate(margin):
                    margin_prime.append((node[0], node[1] + 1, node[2]))
                    margin_prime.append((node[0] + 1, node[1] + 1, node[2]))
                    
                    self._board.add_edge(node, margin_prime[-1])
                    self._board.add_edge(node, margin_prime[-2])
                margin = margin_prime
            # show_graph(self._board)
        #show_graph(self._board)
    
    def connect_branches(self, layer_num:int, branches: Tuple[int, int]):
        for l in range(0, layer_num*2, 2):
            self._board.add_edge((l//2, l, branches[0]), (0, l, branches[1]))
        
    
    def make_board(self):
        for i in range(6):
            self.make_branch(length=2, origin=(0,0,i))
        show_graph(self._board)
        for i in range(6):
            self.connect_branches(layer_num=3, branches=(i%6, (i+1)%6))
            # show_graph(self._board)
        show_graph(self._board)
        



def create_board_playground(k: int):
    G = nx.Graph()
    for i in range(0, 6*k, k):
        
        og_component = []
        for j in range(k):
            if len(og_component) == 2:
                G.add_node(i*0.1+j*0.1)
                G.add_edge( og_component[0], i*0.1+j*0.1 )
                G.add_edge(og_component[1], i * 0.1 + j * 0.1)
                print("###")
                print(og_component)
                print("###")
                og_component = [og_component[1]]
            else:
                print(og_component)
                print(len(og_component))
            print("#2#")
            print(og_component)
            print("#2#")
            G.add_node(i+j)
            og_component.append(i+j)
            print("#3#")
            print(og_component)
            print("#3#")
        if len(og_component) == 2:
            G.add_node(i*0.1+(k-1)*0.1)
            G.add_edge(og_component[0], i*0.1+(k-1)*0.1 )
            G.add_edge(og_component[1], i * 0.1 + (k-1) * 0.1)
            print("###")
            print(og_component)
            print("###")
            og_component = [og_component[1]]
        
        #for i in range(0, 6 * k, k):
        #    for j in range(k):
        #        G.remove_edge()
    


a = Board(size=3)
a.make_board()

