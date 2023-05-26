from config import *
import sys

class Game:
    def __init__(self, m):
        self._game = [[0 for i in range(ROWS)] for j in range(COLS)]
        self._map = m

        for x in range(COLS):
            for y in range(ROWS):
                self._game[x][y] = self._map.get_block_type(x, y)


    def get_symbol(self, block_type):
        return " X#][^-mm][%:. .:|$PE-Q@&*=+><"[block_type]

    def print(self):
        for y in range(ROWS):
            for x in range(COLS):
                sys.stdout.write(self.get_symbol(self._game[x][y]))

            print()

