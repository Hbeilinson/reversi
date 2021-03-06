# reversi


Created by Hannah Beilinson, for Haverford College CS106, with Professor John Dougherty\
\
The module RUNME, when run will automatically start a game of Reversi.\
All classes are in RUNME because the classes reference each other (in a cyclical way). Therefore, putting them in different files causes the Python import system to malfunction. (The player classes reference the game class and the game class references the player class).\
\
RUNME includes methods:\
Game (to implement the flow of the game);\
Board (to maintain a game board);\
Player (to maintain a player throughout the game);\
Hum_Player (which is a player that allows a user to input moves);\
and Comp_Player (which is a player that works as a computer opponent).\
It also includes a start_reversi() function that automatically starts the game when the module is run.\
\
The game is played on an 8x8 grid. When you place a piece in a space, any pieces of the opponent's color that are in a straight line and bounded by the piece just placed and another piece of your color are turned over to your color. (Credit to Wikipedia for this description of the rules) A period represents an empty space. You can only place pieces in empty spaces. Every piece placed MUST change the color of other pieces. Otherwise it will not be a valid move, which the computer will kindly alert you of. When you input coordinates, make sure to notice that the first row and column are 0, not 1.\
\
\
The game class has attributes:\
board;\
p_one (meaning player one);\
and p_two (meaning player two).\
It includes methods:\
game_move(), which carries the flow of the game up until the game is over;\
end_game(), which calculates the scores and declares the winner, then calls again(); and\
again(), which offers the user a chance to play again and calls start_reversi() if the user does want to play again.\
\
\
The board class has only one attribute, boardList, which is a list containing dictionaries that represent rows on the board.\
It includes methods:\
__repr__(), which prints the board as a grid with labels for each row and column, periods to represent empty spaces, Bs to represent black pieces, and Ws to represent white pieces;\
is_valid(row, col, color), which returns a boolean to represent whether an input move (represented as the color that wants to move and the coordinates where it wants to move) is valid; and\
board_move(row, col, color), which updates the board based off a move input in the same format as the input for is_valid().\
\
The player class is only a constructor because there is nothing else that a player does that would be the same for a human player and a computer player. It has attributes color and turn.\
\
The hum_player class has the same attributes as the player class, and includes only one method, player_move(). This method allows the user to input a move, checks if the move is valid, and if it is calls board_move() to update the board according to the input move.\
\
The comp_player class has the same attributes as the player class, and includes only one method, the same one as hum_player. Comp_player\'92s player_move() method generates a move for the current board. If any of the corners is a valid move it will move in a corner (with preference starting with the top left corner, then moving in a clockwise direction). If none of the corners are a valid move, it will choose the move that flips the most pieces, preferring moves that are farthest to the right and down on the board if there are multiple equally optimal moves. This is essentially a greedy algorithm because, other than the corner preference, it is making the optimal move in each turn with the assumption that this will create an optimal overall strategy.\
\
In addition to the five classes, there is a function start_reversi(). This is an independent function because it must create a new game object before any game object exists, and so cannot be a method in the game class. This function gets input from the user to determine if the user wants a one player game or a two player game, then initializes a game object based off this preference.\
\
The module also contains a call of start_reversi() so that a game will automatically be started when the module is run.\
\
}
