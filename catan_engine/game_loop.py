from .Board import Board
from .Player import Player, Players

import numpy as np

class Game:
    
    def __init__(self, players: Players, board: Board):
        self._players : Players = players
        self._board : Board = board
    
    def set_up(self):
        pass
    
    def play(self):
        board = Board()
        board.make_board()
        
        players = Players( players=[ Player( input("Name:") ) for i in range( int( input("Num Players:") ) ) ] )
        
        i = 0
        while 10 not in players.scores:
            i += 1
            if i > 5:
                players[0].points = 10
            print(players.scores)