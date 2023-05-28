import os
import pygame

from config import *
from player import Player
from utils import *
from enemy import Enemy

resources_dir = os.path.join(os.path.dirname(__file__), "resources")

BLOCK_EMPTY         = 0x00
BLOCK_CONCRETE      = 0x01
BLOCK_LADDER        = 0x02
BLOCK_DOOR_LEFT     = 0x03
BLOCK_DOOR_RIGHT    = 0x04
BLOCK_WATER         = 0x05
BLOCK_THIN_FLOOR    = 0x06
BLOCK_EMPTY_BOX     = 0x07
BLOCK_TREASURE      = 0x08
BLOCK_LCK_DOOR_LEFT = 0x09
BLOCK_LCK_DOOR_RIGHT= 0x0a
BLOCK_BRICK         = 0x0b
BLOCK_BRICK_BROKEN1 = 0x0c
BLOCK_BRICK_BROKEN2 = 0x0d
BLOCK_BRICK_BROKEN3 = 0x0e
BLOCK_BRICK_RESTOR1 = 0x0f
BLOCK_BRICK_RESTOR2 = 0x10
BLOCK_DOOR_OPEN     = 0x11
BLOCK_REWARD        = 0x12


class Game:
    def __init__(self, m):
        self._game = [[0 for i in range(ROWS)] for j in range(COLS)]
        self._map = m

        for x in range(COLS):
            for y in range(ROWS):
                self._game[x][y] = self._map.get_block_type(x, y)

        self._player = Player(self._map.get_player_pos(), self)
        self._treasures_found = 0
        self._destroyed_bricks = {}

        self._enemies = [Enemy(pos, self) for pos in m.get_enemy_positions()]

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
        self._block_brick2 = pygame.image.load(f"{resources_dir}/block_brick2.png")
        self._block_brick3 = pygame.image.load(f"{resources_dir}/block_brick3.png")
        self._concrete_empty = pygame.image.load(f"{resources_dir}/block_concrete.png")
        self._ladder_empty = pygame.image.load(f"{resources_dir}/block_ladder.png")
        self._block_water = pygame.image.load(f"{resources_dir}/block_water.png")
        self._block_thin_floor = pygame.image.load(f"{resources_dir}/block_thin_floor.png")
        self._block_treasure = pygame.image.load(f"{resources_dir}/block_treasure.png")
        self._block_door_left = pygame.image.load(f"{resources_dir}/block_door_left.png")
        self._block_door_right = pygame.image.load(f"{resources_dir}/block_door_right.png")
        self._block_door_open = pygame.image.load(f"{resources_dir}/block_door_open.png")
        self._block_reward = pygame.image.load(f"{resources_dir}/block_reward.png")

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
            (self._block_brick,      False),    # 0b        Full brick
            (self._block_brick2,     False),    # 0b        Partially damaged (still blocking)
            (self._block_brick3,     False),    # 0b        Partially damaged (still blocking)
            (self._block_empty2,     True),     # 0e        Fully destroyed brick (non-blocking)
            (self._block_brick3,     True),     # 0f        Partially restored (non-blocking)
            (self._block_brick2,     True),     # 10        Partially restored (non-blocking)
            (self._block_door_open,  True),     # 11
            (self._block_reward,     True),     # 12
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


    def is_water(self, pos):
        return self._game[pos.x][pos.y] == BLOCK_WATER


    def is_empty_box(self, pos):
        return self._game[pos.x][pos.y] == BLOCK_EMPTY_BOX


    def is_treasure(self, pos):
        return self._game[pos.x][pos.y] == BLOCK_TREASURE
    

    def open_left_door(self, pos):
        if self._game[pos.x][pos.y] == BLOCK_DOOR_LEFT:
            self._game[pos.x][pos.y] = BLOCK_DOOR_OPEN

        if self._game[pos.x][pos.y] == BLOCK_LCK_DOOR_LEFT and self._treasures_found > 0:
            self._game[pos.x][pos.y] = BLOCK_DOOR_OPEN


    def open_right_door(self, pos):
        if self._game[pos.x][pos.y] == BLOCK_DOOR_RIGHT:
            self._game[pos.x][pos.y] = BLOCK_DOOR_OPEN

        if self._game[pos.x][pos.y] == BLOCK_LCK_DOOR_RIGHT and self._treasures_found > 0:
            self._game[pos.x][pos.y] = BLOCK_DOOR_OPEN


    def hit_arrow(self, pos):
        # Concrete stops the arrow, but does not change the map
        if self._game[pos.x][pos.y] == BLOCK_CONCRETE:
            return True
        
        # Bricks are destroyed 1 degree on arrow hits
        if self._game[pos.x][pos.y] >= BLOCK_BRICK and self._game[pos.x][pos.y] <= BLOCK_BRICK_BROKEN2:
            self._game[pos.x][pos.y] += 1
            self._destroyed_bricks[pos] = 250 if self._game[pos.x][pos.y] == BLOCK_BRICK_BROKEN3 else 60
            return True

        return False


    def _handle_treasures(self):
        pos = self._player.get_pos()
        if self.is_empty_box(pos):
            self._game[pos.x][pos.y] = BLOCK_EMPTY

        if self.is_treasure(self._player.get_pos()):
            self._treasures_found += 1
            self._game[pos.x][pos.y] = BLOCK_REWARD


    def _handle_bricks(self):
        for pos, counter in self._destroyed_bricks.items():
            counter -= 1
            self._destroyed_bricks[pos] = counter

            bt = self._game[pos.x][pos.y]

            if counter == 0:
                if bt == BLOCK_BRICK_BROKEN1 or bt == BLOCK_BRICK_RESTOR2:
                    self._game[pos.x][pos.y] = BLOCK_BRICK
                    del self._destroyed_bricks[pos]
                    break

                if bt == BLOCK_BRICK_BROKEN2:
                    self._game[pos.x][pos.y] += -1
                else:
                    self._game[pos.x][pos.y] += +1

                self._destroyed_bricks[pos] = 60



    def _get_block_image(self, block_type):
        return self._block_types[block_type][0]


    def update(self, screen):
        # Draw blocks
        for y in range(ROWS):
            for x in range(COLS):
                bt = self.get_block_type(Pos(x, y))
                screen.blit(self._get_block_image(bt), (x*CELL_WIDTH, y*CELL_HEIGHT))

        self._player.update(screen)
        self._handle_treasures()
        self._handle_bricks()

        for e in self._enemies:
            e.update(screen)
        

    def is_game_over(self):
        # Die when player falls into a water
        if self.get_block_type(self._player.get_pos()) == BLOCK_WATER:
            return True
        
        # Die when player is caught by enemy
        for e in self._enemies:
            if self._player.get_pos() == e.get_pos():
                return True
            
        return False


    def is_player_reached_exit(self):
        return self._player.get_pos() == self._map.get_exit_pos()
    

    def get_player_pos(self):
        return self._player.get_pos()
    

    def is_enemy_on_pos(self, pos):
        for e in self._enemies:
            if e.get_pos() == pos:
                return True
            
        return False
    