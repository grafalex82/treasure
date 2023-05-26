import os
import pygame

from config import *
from player import Player
from utils import *

resources_dir = os.path.join(os.path.dirname(__file__), "resources")

BLOCK_EMPTY         = 0x00
BLOCK_CONCRETE      = 0x01
BLOCK_LADDER        = 0x02
BLOCK_WATER         = 0x05
BLOCK_THIN_FLOOR    = 0x06
BLOCK_BRICK         = 0x0b


class Game:
    def __init__(self, m):
        self._game = [[0 for i in range(ROWS)] for j in range(COLS)]
        self._map = m

        for x in range(COLS):
            for y in range(ROWS):
                self._game[x][y] = self._map.get_block_type(x, y)

        self._player = Player(self._map.get_player_pos(), self)

        self._block_empty = pygame.image.load(f"{resources_dir}/block_empty.png")
        self._block_empty2 = pygame.image.load(f"{resources_dir}/block_empty2.png")
        self._block_empty3 = pygame.image.load(f"{resources_dir}/block_empty3.png")
        self._block_empty4 = pygame.image.load(f"{resources_dir}/block_empty4.png")
        self._block_empty5 = pygame.image.load(f"{resources_dir}/block_empty5.png")
        self._block_empty6 = pygame.image.load(f"{resources_dir}/block_empty6.png")
        self._block_empty7 = pygame.image.load(f"{resources_dir}/block_empty7.png")
        self._block_empty8 = pygame.image.load(f"{resources_dir}/block_empty8.png")
        self._block_empty9 = pygame.image.load(f"{resources_dir}/block_empty9.png")
        self._block_brick = pygame.image.load(f"{resources_dir}/block_brick.png")
        self._concrete_empty = pygame.image.load(f"{resources_dir}/block_concrete.png")
        self._ladder_empty = pygame.image.load(f"{resources_dir}/block_ladder.png")
        self._block_water = pygame.image.load(f"{resources_dir}/block_water.png")
        self._block_thin_floor = pygame.image.load(f"{resources_dir}/block_thin_floor.png")
        self._block_treasure = pygame.image.load(f"{resources_dir}/block_treasure.png")
        self._block_door_left = pygame.image.load(f"{resources_dir}/block_door_left.png")
        self._block_door_right = pygame.image.load(f"{resources_dir}/block_door_right.png")

        self._block_types = [
            (self._block_empty,      True),     # 00
            (self._concrete_empty,   False),    # 01
            (self._ladder_empty,     False),    # 02
            (self._block_door_left,  False),    # 03
            (self._block_door_right, False),    # 04
            (self._block_water,      True),     # 05
            (self._block_thin_floor, True),     # 06
            (self._block_treasure,   True),     # 07
            (self._block_treasure,   True),     # 08            
            (self._block_door_left,  False),    # 09
            (self._block_door_right, False),    # 0a
            (self._block_brick,      False),    # 0b
            (None,                   True),     # 0c
            (None,                   True),     # 0d
            (self._block_empty2,     True),     # 0e
            (None,                   True),     # 0f
            (None,                   True),     # 10
            (None,                   True),     # 11
            (None,                   True),     # 12
            (None,                   True),     # 13
            (None,                   True),     # 14
            (None,                   True),     # 15
            (None,                   True),     # 16
            (self._block_empty3,     True),     # 17
            (self._block_empty4,     True),     # 18
            (self._block_empty5,     True),     # 19
            (self._block_empty6,     True),     # 1a
            (self._block_empty7,     True),     # 1b
            (self._block_empty8,     True),     # 1c
            (self._block_empty9,     True),     # 1d
        ]


    def get_block_type(self, pos):
        return self._game[pos.x][pos.y]


    def is_block_empty(self, pos):
        bt = self._game[pos.x][pos.y]
        return self._block_types[bt][1]


    def is_ladder(self, pos):
        return self._game[pos.x][pos.y] == BLOCK_LADDER


    def is_thin_floor(self, pos):
        return self._game[pos.x][pos.y] == BLOCK_THIN_FLOOR


    def _get_block_image(self, block_type):
        return self._block_types[block_type][0]


    def update(self, screen):
        # Draw blocks
        for y in range(ROWS):
            for x in range(COLS):
                bt = self.get_block_type(Pos(x, y))
                screen.blit(self._get_block_image(bt), (x*CELL_WIDTH, y*CELL_HEIGHT))

        self._player.update(screen)
        

    def is_game_over(self):
        return self.get_block_type(self._player.get_pos()) == BLOCK_WATER


    def is_player_reached_exit(self):
        return self._player.get_pos() == self._map.get_exit_pos()
