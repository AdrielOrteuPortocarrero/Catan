from abc import ABC, abstractmethod
from Resources import Resource

class Player:
    def __init__(self):
        pass
    def starting_locations(self):
        pass
    

class Offer:
    _time : int = None
    _give : Resource = None
    _receive : Resource = None
