import os

from game import Game
from map import Map

resources_dir = os.path.join(os.path.dirname(__file__), "resources")

def main():
    for i in range(1, 20):
        m = Map(f"{resources_dir}/map_{i:02}.bin")
        g = Game(m)
        g.print()

if __name__ == '__main__':
    main()
