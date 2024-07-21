# Low Level Design

---

## 1 . Tic Tac Toe Game

### Overview

This project implements a flexible N x N Tic Tac Toe game where two players compete to place their marks on the board. The first player to align N marks in a row, column, or diagonal wins the game. If the board is filled without any player achieving this, the game ends in a tie.

### Game Rules

1. **Players**:

   - Player 1 ('Bob')
   - Player 2 ('Alice')

2. **GamePlay**:

   - Player 1 starts the game by placing an 'Bob' on the board.
   - Player 2 follows by placing an 'Alice'.
   - Players take turns to place their marks in an empty cell of the board.
   - The game continues until a player wins or the board is full.

3. **Winning Conditions**:
   - A player wins by placing N marks consecutively in a row, column, or diagonal.
   - If all cells are filled and no player has N consecutive marks, the game is a tie.

### Class Design

1. **Player**:

   - Represents a player in the game.
   - Can be extended to include additional player attributes and methods.

2. **Board**:

   - Manages the state of the game board.
   - Contains the business logic to check for valid moves and determine the game status (win/tie).

3. **Game**:

   - Orchestrates the game flow.
   - Interacts with the Player and Board classes to manage turns and check for game completion.

#### Algorithm Design

   - The time complexity for determining whether a player has won, tied, or has more moves left is constant time,
     𝑂(1)
