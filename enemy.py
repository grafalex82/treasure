from config import *
from game import *

resources_dir = os.path.join(os.path.dirname(__file__), "resources")

class Enemy:
    def __init__(self, pos, game):
        self._pos = pos
        self._game = game

        self._block_enemy = pygame.image.load(f"{resources_dir}/block_enemy.png")


    def _update_position(self):
        pass

    def update(self, screen):
        self._update_position()

        screen.blit(self._block_enemy, (self._pos.x*CELL_WIDTH, self._pos.y*CELL_HEIGHT))

