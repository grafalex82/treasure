# Treasure game

This is a port of Treasure (Russian: Клад) game, which is well known on [Radio-86RK](https://en.wikipedia.org/wiki/Radio-86RK) soviet computer and its derivatives.

The goal if the game is to find exit of each map. The Player has to find a way through the labyrinth of blocks, doors, and ladders, and not to fall into the water. Some doors are blocked, and require a treasure box to be found first. Most of the treasure boxes are empty, and Player has to find the one with a treasure. Enemies want to catch the Player, which makes the game quite challenging.

# Controls

The player can be controlled with the arrow keys. 'Q' and 'W' keys will throw an arrow, that can be used to destroy bricks and open a path. Bricks are restored over time.

The dot ('.') key can be used to abandon the current map and move to the next one.

# Game blocks

The following blocks exist in the game:
- ![](resources/block_concrete.png) - Concrete, cannot be broken with arrows
- ![](resources/block_brick.png) - Brick, can be broken with arrow. Restores over time
- ![](resources/block_ladder.png) - Ladder. Player and enemies may go up and down through the map using ladders.
- ![](resources/block_water.png) - Water. Player dies when falls to the water. Enemies die as well, but respawn over time.
- ![](resources/block_thin_floor.png) - Thin floor. Player and enemies can walk over the thin floor, but will fall through and falling from above
- ![](resources/block_treasure.png) - Treasure box. Most of the boxes are empty, but if you are lucky you can find a treasure (![](resources/block_reward.png))
- ![](resources/block_door_left.png) - Door. Will open when Player approaches from one side, but does not open from the other side. Some of the doors require treasure to be found first
- Other type of blocks (![](resources/block_empty3.png), ![](resources/block_empty4.png), ![](resources/block_empty5.png), ![](resources/block_empty6.png), ![](resources/block_empty7.png), ![](resources/block_empty8.png), ![](resources/block_empty9.png)) are just empty blocks, and added to the game for variety.

# Why the game is so ugly?

The original Treasure game that was released in 1987. The Radio-86RK computer had B/W monitor, that could display only text character (non graphical display). Each block was shown as a symbol. 

This port intentionally mimics all the features of the original game, including player and enemies movement one block at a time. Definitely, movements may be done much smoother, the graphics may be better, enemies could be smarter, but this would be another game.

# History behind the port

I was dissassembling the original [Treasure game](https://github.com/grafalex82/ut88/blob/main/doc/disassembly/klad.asm). The author did tremendous amount of work to implement all the game cases, design the map format, and fit everything into quite poor computer resources. I am impressed how this all could be developed without a rich compiler and debugging tools we have nowadays.

While the overall code quality is ok, some of the functions could be implemented better. I spend over 20 hours trying to understand the how this code is working. I decided to challenge myself and see how fast I can develop a similar game with modern language and tools. I could do this in about 6 hours :)
