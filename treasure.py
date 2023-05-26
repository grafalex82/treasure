import os
import pygame

from game import Game
from map import Map
from config import *

resources_dir = os.path.join(os.path.dirname(__file__), "resources")

def main():
    maps = [Map(f"{resources_dir}/map_{i:02}.bin") for i in range(1, 20)]
    current_map = 0

    screen = pygame.display.set_mode((COLS*CELL_WIDTH, ROWS*CELL_HEIGHT))
    clock = pygame.time.Clock()

    game = Game(maps[current_map])

    while True:
        screen.fill(pygame.Color('black'))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_PERIOD:
                    current_map += 1
                    current_map %= 19
                    game = Game(maps[current_map])    

        if game.is_game_over():
            game = Game(maps[current_map])    

        if game.is_player_reached_exit():
            current_map += 1
            current_map %= 19
            game = Game(maps[current_map])    

        game.update(screen)
        pygame.display.flip()
        clock.tick(4)
        pygame.display.set_caption(f"Treasure game (FPS={clock.get_fps()})")


if __name__ == '__main__':
    main()
