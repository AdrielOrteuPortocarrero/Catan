from abc import ABC, abstractmethod
from .Resources import Resource
from typing import List, Dict
from numpy.typing import NDArray
import numpy as np

class CraftingTable:
    def __init__(self):
        self._clay : int = 0
        self._wool : int = 0
    
    def craft_town(self):
        pass
    
    def craft_city(self):
        pass
    
    def craft_knight(self):
        pass

class Player(ABC):
    def __init__(self, name):
        self._name: str = name
        self._points: int = 0
        self._resources : dict[str: Resource] = None
        self._infrastructure_available : dict[str:int] = {"paths" : 15,
                                                          "towns" : 5,
                                                          "cites" : 4}
    def starting_locations(self):
        pass
    
    @property
    def points(self):
        return self._points
    
    @points.setter
    def points(self, value):
        self._points = value
        
    
    
    @property
    def name(self):
        return self._name

class Person(Player):
    pass

class Bot(Player):
    pass

class Players:
    def __init__(self, players: list[Player]):
        self._players : list[Player] = players
        self._scores: list[int] = [player.points for player in self.players]
    
    @property
    def players(self):
        return self._players
    
    @property
    def scores(self):
        self._scores = [player.points for player in self.players]
        return self._scores
    
#    def __contains__(self, item):
#        return item in self._players.
    
    def __getitem__(self, item):
        if type(item) == int:
            return self._players[item]
        elif type(item) == str:
            for p in self._players:
                if p.name == item:
                    return p
            raise ValueError ("Name doesn't correspond to any player.")
        else:
            raise TypeError ("Use int (position in list), str (the player name)")
    