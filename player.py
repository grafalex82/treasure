from config import *
from game import *

resources_dir = os.path.join(os.path.dirname(__file__), "resources")

class Player:
    def __init__(self, pos):
        self._block_player = pygame.image.load(f"{resources_dir}/block_player.png")
        self._pos = pos
        
    def get_pos(self):
        return self._pos

    def update(self, screen):
        screen.blit(self._block_player, (self._pos[0]*CELL_WIDTH, self._pos[1]*CELL_HEIGHT))

