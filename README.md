# Space-Battleship
A game similar to battleship, where 5 ships of different sizes and patterns are randomly layed out on a 10-by-12 grid. The rows of the grid are labeled 0 throuh 9, and the columns are labeled A throuh L. Target the ships by entering the row and column of the location you wish to shoot. A ship is destryoed when all of the spaces it fills have have been hit.

# Menu 
Menu:
  1 : Instructions
  2 : View Example Map
  3 : New Game
  4 : Hall of Fame
  5 : Quit
What would you like to do?

# View Example Map
When you view an example map you will be able to see the various examples of how the different ships can be layed out. For example:

   A  B  C  D  E  F  G  H  I  J  K  L
0  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~
1  ~  ~  ~  ~  ~  ~  ~  ~  P  ~  ~  ~
2  ~  ~  ~  ~  ~  ~  ~  ~  P  ~  ~  ~
3  ~  ~  ~  ~  S  ~  ~  ~  ~  ~  B  B
4  ~  ~  ~  ~  S  ~  ~  ~  ~  ~  B  B
5  ~  ~  ~  ~  S  ~  D  ~  ~  ~  ~  ~
6  ~  ~  ~  ~  ~  ~  M  D  M  ~  ~  ~
7  ~  ~  ~  ~  ~  ~  D  M  ~  ~  ~  ~
8  ~  ~  ~  ~  ~  ~  M  ~  M  ~  ~  ~
9  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~


# New Game
When starting a new game the default board will be printed asking where you wish to target fist. Taking the row and column input (i.e '6G').

   A  B  C  D  E  F  G  H  I  J  K  L
0  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~
1  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~
2  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~
3  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~
4  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~
5  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~
6  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~
7  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~
8  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~
9  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~

Where should we target next (q to quit)?

When you input a target and there are no ships at that location a 'o' will be filled in that space indicating a miss. If there is a ship located in that position a 'x' will be filled inidicating a hit.

   A  B  C  D  E  F  G  H  I  J  K  L
0  o  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~
1  ~  ~  ~  o  ~  ~  ~  x  ~  ~  o  ~
2  o  ~  ~  ~  ~  ~  ~  o  ~  ~  ~  ~
3  ~  ~  ~  ~  o  ~  ~  ~  ~  ~  ~  ~
4  ~  ~  ~  o  ~  ~  ~  ~  o  o  ~  ~
5  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~
6  ~  ~  ~  o  ~  ~  o  ~  ~  o  ~  ~
7  ~  ~  ~  ~  o  ~  ~  o  ~  ~  ~  ~
8  ~  o  ~  ~  ~  o  o  ~  ~  ~  o  o
9  ~  ~  ~  ~  ~  o  ~  ~  ~  ~  ~  ~

When a ship is destroyed it will be indicated which ship you destroyed.

   A  B  C  D  E  F  G  H  I  J  K  L
0  o  ~  ~  ~  ~  ~  o  o  o  ~  ~  o
1  ~  ~  ~  o  ~  ~  o  x  o  ~  o  ~
2  o  ~  ~  ~  ~  ~  o  o  x  ~  ~  ~
3  ~  ~  ~  ~  o  ~  ~  x  ~  ~  ~  ~
4  ~  ~  ~  o  ~  ~  ~  ~  o  o  ~  ~
5  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~
6  ~  ~  ~  o  ~  ~  o  ~  ~  o  ~  ~
7  ~  ~  ~  ~  o  ~  ~  o  ~  ~  ~  ~
8  ~  o  ~  ~  ~  o  o  ~  ~  ~  o  o
9  ~  ~  ~  ~  ~  o  ~  ~  ~  ~  ~  ~

The enemy's Destroyer has been destroyed.

This process is repeated until all ships are sunk

# Hall of Fame
This feature is meant to be a score board filled with the best scores. This section is still being worked on.


