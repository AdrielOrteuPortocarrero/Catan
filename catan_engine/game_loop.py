from .Maps import Board
from .Player import Player, Players
from random import randint

import numpy as np

class Game:
    
    def __init__(self, players: Players, board: Board):
        self._players : Players = players
        self._board : Board = board
    
    @property
    def players(self):
        return self._players
    @players.setter
    def players(self, new_players):
        if type(new_players) == list:
            if all(type(player)==Player for player in new_players):
                self._players = new_players
            else:
                TypeError("The items of the list being assigned to attribute players need to belong to the Player class (or subclasses)")
        else:
            raise TypeError("The players attribute must be a LIST")
        
    
    def set_up(self):
        for player in self.players.players:
            player.starting_locations()
        for player in reversed(self.players.players):
            pass
    
    def play(self):
        
        
        i = 0
        while 10 not in self.players.scores:
            roll = sum([ randint(1, 6) for i in range(2)])
            print(roll)
            i += 1
            if i > 5:
                self.players[0].points = 10
            print(self.players.scores)