from abc import ABC, abstractmethod
import networkx as nx

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


class Board:
    _num_deserts = 1
    _num_mountains = 3
    _num_clay_banks = 3
    _num_forests = 4
    _num_sheep_herds = 4
    _num_wheat_fields = 4
    def __init__(self):
        self._board = nx.Graph()
