from abc import ABC, abstractmethod
import networkx as nx
from networkx import Graph
from random import choice

from .networkHelp import show_graph
from typing import List, Tuple
# from resource import *

from .Player import Player

class Intersection:
    
    def __init__(self, identifier: Tuple[int, int, int]) -> None:
        self._identifier : Tuple[int, int, int] = identifier # format -> (modulo, layer, branch)
        self._building : int = 0
        self._settler : str = "" # The settler parameter stores the UNIQUE string that identifies the player that settled in this intersectionn
    
    @property
    def settler(self):
        return self._settler
    
    @settler.setter
    def settler(self, settler: Player) -> None:
        self._settler = settler
    
    @property
    def building(self) -> int:
        return self._building
    
    @building.setter
    def building(self, building : int) -> None:
        if type(building) == int:
            if 0 == building or 1 == building or 2 == building:
                self._building = building
            else:
                raise ValueError ("buildings have a value of 0 or 1 or 2")
        else:
            raise TypeError ("buildings are integers")
    
    @property
    def identifier(self) -> Tuple[int, int, int]:
        return self._identifier
    
    def __str__(self):
        return f"{self._identifier}"
    
    def __getitem__(self, item: int) -> int:
        return self._identifier[item]
    
    def __eq__(self, other) -> bool:
        if type(other) == Intersection:
            return self.identifier == other.identifier
        elif type(other) == tuple:
            return self.identifier == other
        else:
            raise TypeError ("The comparison must be between an Intersection and another (Intersection or Tuple)")
    
    def __hash__(self) -> int:
        return hash(self.identifier)  # Use the same attribute as in __eq__


class Tile:
    def __init__(self, intersections: List[Intersection], num: int, resource: str) -> None:
        self._intersections: List[Intersection] = intersections
        self._num: int = num
        self._resource: str = resource
    
    @property
    def num(self) -> int:
        return self._num
    
    @property
    def resource(self) -> str:
        return self._resource
    
    @property
    def intersections(self) -> list[Intersection]:
        return self._intersections
    
    @num.setter
    def num(self, new_num: int):
        if new_num < 1 or new_num > 6:
            raise ValueError ("The tile number must be between 1 and 6 (included).")
        self._num = new_num
    
    @resource.setter
    def resource(self, new_resource):
        self._resource = new_resource
    
    @intersections.setter
    def intersections(self, new_intersections: list[Intersection]) -> None:
        self._intersections = new_intersections
    
    def __len__(self):
        return len(self._intersections)
    
    def __getitem__(self, item: int):
        return self.intersections[item]
    
    def __str__(self):
        return f"resource={self.resource} | num={self.num}\n{ [str(intersect) for intersect in self.intersections] }"
    
    def generate_resources(self, luck) -> dict[str:Tuple[str,int]]:
        if self.num == luck:
            generated_resources = {}
            for intersect in self.intersections:
                if intersect.settler in generated_resources:
                    generated_resources[intersect.settler] += intersect.building
                else:
                    generated_resources[intersect.settler] += intersect.building
        
        return generated_resources


class Map (ABC):
    
    def __init__(self):
        self._map : Graph = Graph()
        self._tiles : list[Tile] = []
    
    @property
    def map(self):
        return self._map
    @map.setter
    def map(self, new_map:Graph):
        self._map = new_map
    
    def get_tiles(self):
        """Sets the values of a list of tiles, each tile is a list of directed edges of the board."""
        planar_bool, embedding = nx.check_planarity(self.map)
        seen_half_edges = set()
        self._tiles = []
        
        if planar_bool:
            for u in embedding:
                for v in embedding[u]:
                    if (u, v) not in seen_half_edges:
                        # Walk around the tile to the right of (u, v)
                        
                        ### compute necessary values for Tile instance ###
                        tile_nodes = embedding.traverse_face(u, v)
                        if tile_nodes == [(0, 0, 0), (0, 0, 1), (0, 0, 2), (0, 0, 3), (0, 0, 4), (0, 0, 5)] or len(
                                tile_nodes) != 6:
                            r = "d"
                            n = 0
                        else:
                            r = choice(self._resources)
                            n = choice(self._nums)
                            self._resources.remove(r)
                            self._nums.remove(n)
                        ###
                        
                        tile = Tile(intersections=tile_nodes, num=n, resource=r)
                        
                        self._tiles.append(tile)
                        # Mark all directed edges in the tile as seen
                        for i in range(len(tile)):
                            a, b = tile[i], tile[(i + 1) % len(tile)]
                            seen_half_edges.add((a, b))


class Board:
    _num_deserts = 1
    _num_mountains = 3
    _num_clay_banks = 3
    _num_forests = 4
    _num_sheep_herds = 4
    _num_wheat_fields = 4
    
    def __init__(self, size=6):
        self._board : Graph = nx.Graph()
        self._tiles : List[Tile] = []
        self._size : int = size
        
        self._resources = ["rock", "rock", "rock", "clay", "clay", "clay", "clay", "lumber", "lumber", "lumber", "lumber", "wool", "wool", "wool", "wool", "cereal", "cereal", "cereal", "cereal"]
        self._nums = [2, 3, 3, 4, 4, 5, 5, 6, 6, 8, 8, 9, 9, 10, 10, 11, 11, 12]
        
        self.make_board()
    
    def make_branch(self, length: int, origin: Intersection):
        # origin = Intersection( (0, 0, 0) )
        self._board.add_node(origin)
        layer_nodes = [origin]
        for i in range(length*2):
            if i%2 == 0:
                """extend to the next layer | o---o"""
                for j, node in enumerate(layer_nodes):
                    # create_new_name()
                    # layer_nodes[j] (old) = (M, L, B) (aka. modulo - layer - branch)
                    # pre_node = layer_nodes[j] # ¿pre_node = node?
                    layer_nodes[j] = Intersection((node[0], node[1]+1, node[2]))
                    ###
                    self._board.add_edge(node, layer_nodes[j])
            else:
                """ add a layer | ·<:"""
                margin_prime = []
                for node in layer_nodes:
                    margin_prime.append( Intersection( (node[0], node[1] + 1, node[2]) ) )
                    margin_prime.append( Intersection( (node[0] + 1, node[1] + 1, node[2]) ) )
                    
                    self._board.add_edge(node, margin_prime[-1])
                    self._board.add_edge(node, margin_prime[-2])
                layer_nodes = margin_prime
            #show_graph(self._board)
        #show_graph(self._board)
    
    def connect_branches(self, layer_num:int, branches: Tuple[int, int]):
        for l in range(0, layer_num*2, 2):
            self._board.add_edge( Intersection( (l//2, l, branches[0]) ), Intersection( (0, l, branches[1]) ) )
    
    def make_board(self):
        for i in range(6):
            self.make_branch(length=2, origin= Intersection( (0,0,i) ) )
        #show_graph(self._board)
        for i in range(6):
            self.connect_branches(layer_num=3, branches=(i%6, (i+1)%6))
            # show_graph(self._board)
        #show_graph(self._board)
    
    @property
    def nx_board(self):
        return self._board
    
    def compute_tiles(self):
        """Sets the values of a list of tiles, each tile is a list of directed edges of the board."""
        planar_bool, embedding = nx.check_planarity(self.nx_board)
        seen_half_edges = set()
        self._tiles = []
        
        if planar_bool:
            for u in embedding:
                for v in embedding[u]:
                    if (u, v) not in seen_half_edges:
                        # Walk around the tile to the right of (u, v)
                        
                        ### compute necessary values for Tile instance ###
                        tile_nodes = embedding.traverse_face(u, v)
                        if tile_nodes == [(0, 0, 0), (0, 0, 1), (0, 0, 2), (0, 0, 3), (0, 0, 4), (0, 0, 5)] or len(tile_nodes) != 6:
                            r = "d"
                            n = 0
                        else:
                            r = choice(self._resources)
                            n = choice(self._nums)
                            self._resources.remove(r)
                            self._nums.remove(n)
                        ###
                        
                        tile = Tile(intersections=tile_nodes, num=n, resource=r)
                        
                        self._tiles.append(tile)
                        # Mark all directed edges in the tile as seen
                        for i in range(len(tile)):
                            a, b = tile[i], tile[(i + 1) % len(tile)]
                            seen_half_edges.add((a, b))
    
    @property
    def tiles(self) -> List[Tile]:
        return self._tiles




def show(g):
    show_graph(g)