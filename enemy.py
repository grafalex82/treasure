from config import *
from game import *

resources_dir = os.path.join(os.path.dirname(__file__), "resources")

class Enemy:
    def __init__(self, pos, game):
        self._pos = pos
        self._original_pos = pos
        self._game = game

        self._falling = False
        self._tick = 0

        self._respawn_counter = 0

        self._block_enemy = pygame.image.load(f"{resources_dir}/block_enemy.png")


    def get_pos(self):
        return self._pos
    

    def _die(self):
        self._respawn_counter = 100 # 50 full game ticks in original game, but our ticks runs twice faster


    def _is_dead(self):
        return self._respawn_counter > 0
    

    def _handle_respawn(self):
        self._respawn_counter -= 1
        if self._respawn_counter == 0:
            self._pos = self._original_pos


    def _on_surface(self):
        if self._game.is_ladder(self._pos):
            return True
        
        if self._game.is_thin_floor(self._pos.below()) and not self._falling:
            return True

        return not self._game.is_block_empty(self._pos.below())


    def _can_move(self, new_pos):
        if self._game.is_block_empty(new_pos) or \
           self._game.is_ladder(new_pos):
            return not self._game.is_enemy_on_pos(new_pos)
        
        return False


    def _move(self, new_pos):
        self._pos = new_pos

        if self._game.is_water(self._pos):
            self._die()


    def _try_reach_player(self):
        # Enemy runs 3 of 4 ticks (compared to player that moves faster)
        if (self._tick / 2) % 4 == 0:
            return
        
        player_pos = self._game.get_player_pos()

        # Try matching X position first
        if player_pos.x > self._pos.x and self._can_move(self._pos.right()):
            self._move(self._pos.right())
        elif player_pos.x < self._pos.x and self._can_move(self._pos.left()):
            self._move(self._pos.left())
        # Try matching Y position next]
        elif player_pos.y < self._pos.y and self._can_move(self._pos.above()) and self._game.is_ladder(self._pos.above()):
            self._move(self._pos.above())
        elif player_pos.y > self._pos.y and self._can_move(self._pos.below()):
            self._move(self._pos.below())


    def _handle_falling(self):
        self._move(self._pos.below())


    def _update_position(self):
        if self._on_surface():
            self._falling = False
            self._try_reach_player()
        else:
            self._falling = True
            self._handle_falling()


    def update(self, screen):
        self._tick += 1                     
        
        if self._is_dead():
            self._handle_respawn()
        else:
            # Enemies move twice slower than the arrow
            if self._tick % 2 == 0: 
                self._update_position()

            if not self._is_dead():
                screen.blit(self._block_enemy, (self._pos.x*CELL_WIDTH, self._pos.y*CELL_HEIGHT))

