# The Generated Game Level Corpus

This dataset includes levels for five 2D tile-based games created based on popular classic genres using image tiles from [Kenney](https://www.kenney.nl/) by [Sturgeon](https://github.com/crowdgames/sturgeon-pub).

The five games are:
- **platform**: A simple platformer inspired by Super Mario Bros. Local structures are similar to those in level 1-1 of that game, using a text representation like that in the VGLC. This platformer game includes various platforms arranged at different heights and distances, requiring the player to walk and jump to reach the end from the starting position while avoiding obstacles and falling off. There are more than $10,000$ levels in this dataset coming in $16*32$ size.

- **vertical**: A platformer game inspired by Super Cat Tales. This game is interesting in that the player does not jump directly from a standstill, but can wall climb, jump off walls, and leap off ledges. Levels generally proceed vertically, where each level begins on the bottom platforms with a farm-like atmosphere. As the player goes up through the level, the platforms become increasingly industrialized. There are more than $10,000$ levels in this dataset coming in $20*16$ size.

- **cave**: A simple top-down cave map. Cave levels come in three different versions: simple, doors, and portal. In each level, players navigate maze-like paths to find the exit door leading to the next level. In levels with doors, players must locate keys to unlock these doors and progress. Portal levels feature doors that transport players to other locations within the level, resulting in two independent areas that are not reachable from each other --- thus the path through the level is not contiguous. There are more than $5,000$ simple levels, $20,000$ levels with doors, and $35,000$ levels with portals in this dataset. These levels come in $16 * 32$ and $16 * 16$ sizes. 

- **slide**: A top-down game inspired by Tomb of the Mask. The player must slide through a snowy terrain while avoiding obstacles. The player's movement pattern is special as by starting moving in one direction, they continue in that direction until they hit an obstacle. There are more than $10,000$ levels in this dataset that come in $32*16$ size.

- **crates**: A puzzle game inspired by Sokoban in which the player has to push crates around the level into slots. The player can only push crates, not pull them, and the crates can only be pushed one at a time. Although seemingly easy, game levels can be hard to play as even a single push of crates into constrained positions, such as against walls, corners, or narrow passages, can make it immovable or block access to other areas. There are $10,000$ simple levels in this dataset coming in $16*16$ size and $2$ crates.

Each game level in this dataset contains two representations: an image and a text description. The image representation is a picture of the level and the text representation is a 2D tile of characters, where each character generally indicates the function of the tile at that tile location (e.g., typically X for solid and - for empty). Tiles of each game have been introduced in the **tile.json** file. The movement template of each game is also available in **move.json**.

Each level, if solvable, also has an associated solution. This is either a location-to-location edge path from the start location (usually represented by a { to the goal location (usually represented by a }), or a playthrough sequence of levels.  The solutions are not necessarily unique and there may be (many) other solutions to a given level.

The source code of the generation process is available on https://github.com/TheGGLC/Source.

# Quick setup
to load game level images: 
`levels_imgs, levels_labels = load_img(game)`
for example:
`levels_imgs, levels_labels = load_img("cave")`


to load game level texts: 
`levels_txts, levels_labels = load_txt(game)`
for example:
`levels_txts, levels_labels = load_txt("cave")`


to load solvable game level texts and solutions
`levels_txts, levels_path = load_txt_solutions("game")`
for example:
`levels_txts, levels_path = load_txt_solutions("cave")`