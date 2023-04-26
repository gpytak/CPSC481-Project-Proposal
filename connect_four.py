# Gregory Pytak and Nolan Winter
# CPSC 481 Project Proposal

from games import *

class ConnectFour(TicTacToe):
    def __init__(self, h=7, v=6, k=4):
        TicTacToe.__init__(self, h, v, k)

    def actions(self, state):
        return [(x, y) for (x, y) in state.moves
                if x == self.h or (x + 1 , y ) in state.board]