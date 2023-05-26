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

        self._player_pos = self._map.get_player_pos()

        self._block_player = pygame.image.load(f"{resources_dir}/block_player.png")

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
            self._block_empty,      # 00
            self._concrete_empty,   # 01
            self._ladder_empty,     # 02
            self._block_door_left,  # 03
            self._block_door_right, # 04
            self._block_water,      # 05
            self._block_thin_floor, # 06
            self._block_treasure,   # 07
            self._block_treasure,   # 08            
            self._block_door_left,  # 09
            self._block_door_right, # 0a
            self._block_brick,      # 0b
            None,                   # 0c
            None,                   # 0d
            self._block_empty2,     # 0e
            None,                   # 0f
            None,                   # 10
            None,                   # 11
            None,                   # 12
            None,                   # 13
            None,                   # 14
            None,                   # 15
            None,                   # 16
            self._block_empty3,     # 17
            self._block_empty4,     # 18
            self._block_empty5,     # 19
            self._block_empty6,     # 1a
            self._block_empty7,     # 1b
            self._block_empty8,     # 1c
            self._block_empty9,     # 1d
        ]


    def update(self, screen):
        # Draw blocks
        for y in range(ROWS):
            for x in range(COLS):
                bt = self._game[x][y]
                screen.blit(self._block_types[bt], (x*CELL_WIDTH, y*CELL_HEIGHT))

        # Draw the player
        screen.blit(self._block_player, (self._player_pos[0]*CELL_WIDTH, self._player_pos[1]*CELL_HEIGHT))


