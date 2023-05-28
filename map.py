from config import *
from utils import *

class Map:
    def __init__(self, filename):
        self._map = [[0 for i in range(ROWS)] for j in range(COLS)]
        self._load_map(filename)


    def _load_map(self, filename):
        with open(filename, "rb") as f:
            data = f.read()

        offset = 0
        while data[offset] != 0:
            block_type = data[offset]
            y1 = data[offset+1]
            y2 = data[offset+2]
            x1 = data[offset+3]
            x2 = data[offset+4]
            offset += 5

            for x in range(x1, x2+1):
                for y in range(y1, y2+1):
                    self._map[x][y] = block_type

        offset += 1
        self._player_pos = Pos(data[offset+1], data[offset])

        enemy_count = 1 if data[offset+10] == 0 else data[offset+10]
        self._enemies_pos = []
        for enemy in range(enemy_count):
            self._enemies_pos.append(Pos(data[offset + 3 + enemy*2], data[offset + 2 + enemy*2]))
        
        offset += 11
        self._exit_pos = Pos(data[offset+1], data[offset])


    def get_block_type(self, x, y):
        return self._map[x][y]
    

    def get_player_pos(self):
        return self._player_pos
    

    def get_exit_pos(self):
        return self._exit_pos


    def get_enemy_positions(self):
        return self._enemies_pos