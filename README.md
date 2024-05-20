Ugolki is a simple board game where players need to move all of their pieces across the board to the opposite corner. 

It is allowed to jump over one's own or the opponent's pieces. The pieces cannot be taken, beaten or promoted.

The goal of the project is to implement a neural network that will learn to play the game. The learning data will be a collection of games played by the AI against itself, using some classic (non-ML) algorithm to make moves. 

Currently implemented:

-computer plays against itself, no human player possible,

-logic of making moves: choose the move that leads to the greatest decrease of distance to the opposite corner, summed over player's pieces,

-current analysis depth: one move only,

-press space repeatedly to observe computer make its moves,

-the moves are saved to the text file game.txt.
