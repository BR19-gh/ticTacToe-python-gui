
# ticTacToe-python
## What is the game?
It's a `tic-tac-toe` game written in Python and runs on Tkinter. 
## Gamemodes

There's two game modes:
-	Single Player:
	-	Player plays against a logic (Computer) which choose any empty place to play in
-	Multiplayers:
	-	Two players play against each other   

## Properties
- In multiplayer, the 1st player can choose to be any character (X or O) and the other player will be marked with the remaining one 

- In single player, the player can choose to be any character (X or O) and Computer will be marked with the remaining one

- First turn will be randomly determined (between 1st player and 2nd player in multiplayer, and between player and Computer in single player)

## Starting Up
You should first download `Python-3.9` then run the file in the Python terminal
## Some Game Preview
Start Menu
```
Welcome to <X && O>.

Choose form the menu:
1- Single Player
2- Multi-Players
```
<hr>

Choosing Character
```
Player-1, choose your character, either X or O: 
```
<hr>

Gameplay
```
% Computer played in position #3 %

The current state of the board is:
-------------
| O | X | O |
-------------
| - | X | - |
-------------
| - | O | - |
-------------
 
Use the below figure as a reference:
-------------
| 1 | 2 | 3 |
-------------
| 4 | 5 | 6 |
-------------
| 7 | 8 | 9 |
-------------

Player-X choose position between 1 to 9: 
```
<hr>

Wining Message
```
-------------
| X | X | X |
-------------
| O | O | - |
-------------
| O | - | - |
-------------
Player-X won, congrats.
Press Enter to Exit
```
<hr>
