import os
import pygame

from config import *

resources_dir = os.path.join(os.path.dirname(__file__), "resources")

class Game:
    def __init__(self, m):
        self._game = [[0 for i in range(ROWS)] for j in range(COLS)]
        self._map = m

        for x in range(COLS):
            for y in range(ROWS):
                self._game[x][y] = self._map.get_block_type(x, y)

        self._block_empty = pygame.image.load(f"{resources_dir}/block_empty.png")
        self._block_brick = pygame.image.load(f"{resources_dir}/block_brick.png")
        self._concrete_empty = pygame.image.load(f"{resources_dir}/block_concrete.png")
        self._ladder_empty = pygame.image.load(f"{resources_dir}/block_ladder.png")
        self._block_water = pygame.image.load(f"{resources_dir}/block_water.png")
        self._block_thin_floor = pygame.image.load(f"{resources_dir}/block_thin_floor.png")
        self._block_treasure = pygame.image.load(f"{resources_dir}/block_treasure.png")

        self._block_types = [
            self._block_empty,      # 00
            self._concrete_empty,   # 01
            self._ladder_empty,     # 02
            None,                   # 03
            None,                   # 04
            self._block_water,      # 05
            self._block_thin_floor, # 06
            self._block_treasure,   # 07
            self._block_treasure,   # 08            
            None,                   # 09
            None,                   # 0a
            self._block_brick       # 0b
        ]


    def update(self, screen):
        for y in range(ROWS):
            for x in range(COLS):
                bt = self._game[x][y]
                screen.blit(self._block_types[bt], (x*CELL_WIDTH, y*CELL_HEIGHT))



