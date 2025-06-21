from abc import ABC, abstractmethod
import networkx as nx
import matplotlib.pyplot as plt
from networkx import reverse

from networkHelp import show_graph
from typing import List, Tuple

class Tile (ABC):
    _type = None
    def __init__(self, num: int) -> None:
        self._num : int = num
    
    @property
    def num(self) -> int:
        return self._num
    @num.setter
    def num(self, new_num: int):
        self._num = new_num
    

class ProducerTile(Tile):
    
    @property
    def type(self) -> None:
        return self._type
    @type.setter
    def type(self, tile_type):
        self._type = tile_type

class DesertTile (Tile):
    pass


class Intersection:
    
    def __init__(self, identifier: Tuple[int]):
        self._identifier : Tuple[int] = identifier
    


class Board:
    _num_deserts = 1
    _num_mountains = 3
    _num_clay_banks = 3
    _num_forests = 4
    _num_sheep_herds = 4
    _num_wheat_fields = 4
    def __init__(self, size):
        self._board = nx.Graph()
        self.create_board(size=size)
    
    def create_layer(self, k: int, vertex_set: List[List[float]]) -> None:
        pass
    def add_new_layer_vertices(self, layer_description: List[List[float]]) -> None:
        pass
    def create_board(self, size: int) -> None:
        for l in range(size, 0, -1):
            new_vertices = [ [j for j in range(l)] for i in range(6)]
            self.add_new_layer_vertices(layer_description=new_vertices)
            self.create_layer(l, vertex_set=new_vertices)
    
    def make_branch(self, length: int, origin: int):
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
                for j, node in enumerate(margin):
                    
                    pass
                pass
            pass
        


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
    show_graph(G)


# create_board_playground(3)


