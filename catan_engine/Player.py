from abc import ABC, abstractmethod
from .Resources import Resource
from typing import List, Dict

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

class Player:
    def __init__(self):
        self._resources : Dict[str: Resource]
    def starting_locations(self):
        pass
    

class Offer:
    _time : int = None
    _give : Resource = None
    _receive : Resource = None
