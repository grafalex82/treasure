from config import *
from game import *

resources_dir = os.path.join(os.path.dirname(__file__), "resources")

class Arrow:
    def __init__(self, pos, right, game):
        self._pos = pos
        self._right = right
        self._game = game

        self._block_arrow = pygame.image.load(f"{resources_dir}/block_arrow.png")


    def _update_position(self):
        self._pos = self._pos.right() if self._right else self._pos.left()
        return self._game.hit_arrow(self._pos)


    def update(self, screen):
        if self._update_position():
            return True

        screen.blit(self._block_arrow, (self._pos.x*CELL_WIDTH, self._pos.y*CELL_HEIGHT))
        return False
