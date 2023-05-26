from config import *
from game import *
from utils import *

resources_dir = os.path.join(os.path.dirname(__file__), "resources")

class Player:
    def __init__(self, pos, game):
        self._block_player = pygame.image.load(f"{resources_dir}/block_player.png")

        self._game = game
        self._pos = pos
        self._falling = False
        self._tick = 0


    def get_pos(self):
        return self._pos


    def _on_surface(self):
        if self._game.is_ladder(self._pos):
            return True
        
        return not self._game.is_block_empty(self._pos.below())


    def _try_move(self, new_pos):
        if self._game.is_block_empty(new_pos) or \
           self._game.is_ladder(new_pos):
            self._pos = new_pos


    def _handle_keypress(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self._try_move(self._pos.left())
        if keys[pygame.K_RIGHT]:
            self._try_move(self._pos.right())
        if keys[pygame.K_UP] and self._game.is_ladder(self._pos):
            self._try_move(self._pos.above())
        if keys[pygame.K_DOWN]:
            self._try_move(self._pos.below())


    def _handle_falling(self):
        self._tick += 1                     

        if self._tick % 4 != 0:                 # Player falls 3 of 4 ticks 
            self._pos = self._pos.below()       # (compared to enemies which fall faster)


    def _update_position(self):
        if self._on_surface():
            self._falling = False
            self._handle_keypress()
        else:
            self._falling = True
            self._handle_falling()
        

    def update(self, screen):
        self._update_position()

        screen.blit(self._block_player, (self._pos.x*CELL_WIDTH, self._pos.y*CELL_HEIGHT))

