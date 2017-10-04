'''
Reversi, by Hannah Beilinson (also known as Othello under Mattel marketing)
#Charlie Marx helped me with debugging a few of the methods

This file includes methods:
Game (to implement the flow of the game);
Board (to maintain a game board);
Player (to maintain a player throughout the game);
Hum_Player (which is a player that allows a user to input moves);
and Comp_Player (which is a player that works as a computer opponent).
It also includes a start_reversi() function that automatically starts the game when the module is run.

'''

from copy import *

#Maintains a board throughout the game
class Board:
    def __init__(self):
        #Each dictionary is a row on the board.
        #Each key is a space, with a value of either ".", meaning empty, "W", meaning white, or "B", meaning black.
        d0 = {0:".", 1:".", 2:".", 3:".", 4:".", 5:".", 6:".", 7:"."}
        d1 = {0:".", 1:".", 2:".", 3:".", 4:".", 5:".", 6:".", 7:"."}
        d2 = {0:".", 1:".", 2:".", 3:".", 4:".", 5:".", 6:".", 7:"."}
        d3 = {0:".", 1:".", 2:".", 3:"W", 4:"B", 5:".", 6:".", 7:"."} #The game starts with four pieces already on the board in spaces 33, 34, 43, and 44
        d4 = {0:".", 1:".", 2:".", 3:"B", 4:"W", 5:".", 6:".", 7:"."}
        d5 = {0:".", 1:".", 2:".", 3:".", 4:".", 5:".", 6:".", 7:"."}
        d6 = {0:".", 1:".", 2:".", 3:".", 4:".", 5:".", 6:".", 7:"."}
        d7 = {0:".", 1:".", 2:".", 3:".", 4:".", 5:".", 6:".", 7:"."}
        self.boardList = [d0, d1, d2, d3, d4, d5, d6, d7] #This list keeps all the rows organized, so that an index in this list corresponds to a dictionary row

    def __repr__(self):
        #Prints the board with integer labels above each column and to the left of each row
        result = "  "
        for i in range(8):
            result += str(i) + " " #Prints the column labels
        result += "\n"
        for ind,x in enumerate(self.boardList): #Iterates through the list of dictionaries
            result += str(ind) + " " #Adds the row label
            for n in sorted(x):
                result += str(x[n]) + " " #Prints the values in the row (the current dictionary)
            result += "\n"
        return result #Returns the fully formatted board

    def is_valid(self, row, col, color):
        #Checks if a player's move is valid on the current board
        assert((row in [0,1,2,3,4,5,6,7]) and (col in [0,1,2,3,4,5,6,7]) and (color == "B" or color == "W")) #precondition
        
        if self.boardList[row][col] != ".":
            return False #If the space input is not empty, the move is automatically not valid
        
        valid = False
        if color == "B":
            other = "W"
        else:
            other = "B"

        #A valid move must flip at least one piece. The following loops check to make sure at least one piece will be flipped.
        done_row_left = False #Represents if the row to the left of the space is done being checked
        l = 1
        #Checks if any changes will be made in the row to the left of the new piece
        while l <= col and done_row_left == False: #Will iterate through subtracting l from the column coordinate to check all spaces to the left of the new piece
            if self.boardList[row][col - l] == other: #As long as the current piece is the other color a change still might occur
                done_row_left = False
            elif (self.boardList[row][col - l] == color) and l != 1: #Once the current player's color is reached, after a series of the other color, a change will occur, making the move valid 
                valid = True
            else:
                done_row_left = True #If the loop reaches an empty space before a space of the current player's color, no change in this direction will occur
            l += 1

        done_row_right = False #Represents if the row to the right of the space is done being checked
        r = 1
        #Checks if any changes will be made in the row to the right of the new piece (uses essentially the same process as the above loop, just adding the iterating variable instead of subtracting it)
        while r <= (7 - col) and done_row_right == False:
            if self.boardList[row][col + r] == other:
                done_row_right = False
            elif (self.boardList[row][col + r] == color) and r != 1:
                valid = True
            else:
                done_row_right = True
            r += 1

        done_column_up = False #Represents if the column above the space is done being checked
        u = 1
        #Checks if any changes will be made in the column above the new piece (uses essentially the same process as the above loops, just subtracting the iterating variable from row instead of column)
        while u <= row and done_column_up == False:
            if self.boardList[row - u][col] == other:
                done_column_up = False
            elif (self.boardList[row - u][col] == color) and u != 1:
                valid = True
            else:
                done_column_up = True
            u += 1

        done_column_down = False #Represents if the column below the space is done being checked
        d = 1
        #Checks if any changes will be made in the column below the new piece (uses essentially the same process as the above loops, just adding the iterating variable to row instead of subtracting it)
        while d <= (7 - row) and done_column_down == False:
            if self.boardList[row + d][col] == other:
                done_column_down = False
            elif (self.boardList[row + d][col] == color) and d != 1:
                valid = True
            else:
                done_column_down = True
            d += 1

        done_diagonal_lu = False #Represents if the diagonal to the left and up from the space is done being checked
        dlu = 1
        #Checks if any changes will be made on the diagonal to the left and up from the new piece (uses mostly the same process as the above loops)
        while (dlu <= row) and (dlu <= col) and done_diagonal_lu == False:
            if self.boardList[row - dlu][col - dlu] == other: #Changes both the row and column coordinates by one each time
                done_diagonal_lu = False
            elif (self.boardList[row - dlu][col - dlu] == color) and dlu != 1:
                valid = True
            else:
                done_diagonal_lu = True
            dlu += 1

        done_diagonal_ld = False #Represents if the diagonal to the left and down from the space is done being checked
        dld = 1
        #Checks if any changes will be made on the diagonal to the left and down from the new piece (uses mostly the same process as the above loop)
        while (dld <= (7 - row)) and (dld <= col) and done_diagonal_ld == False:
            if self.boardList[row + dld][col - dld] == other:
                done_diagonal_ld = False
            elif (self.boardList[row + dld][col - dld] == color) and dld != 1:
                valid = True
            else:
                done_diagonal_ld = True
            dld += 1

        done_diagonal_rd = False #Represents if the diagonal to the right and down from the space is done being checked
        drd = 1
        #Checks if any changes will be made on the diagonal to the right and down from the new piece (uses mostly the same process as the above loop)
        while (drd <= (7 - row)) and (drd <= (7 - col)) and done_diagonal_rd == False:
            if self.boardList[row + drd][col + drd] == other:
                done_diagonal_rd = False
            elif (self.boardList[row + drd][col + drd] == color) and drd != 1:
                valid = True
            else:
                done_diagonal_rd = True
            drd += 1

        done_diagonal_ru = False #Represents if the diagonal to the right and up from the space is done being checked
        dru = 1
        #Checks if any changes will be made on the diagonal to the right and up from the new piece (uses mostly the same process as the above loop)
        while (dru <= row) and (dru <= (7 - col)) and done_diagonal_ru == False:
            if self.boardList[row - dru][col + dru] == other:
                done_diagonal_ru == False
            elif (self.boardList[row - dru][col + dru] == color) and dru != 1:
                valid = True
                done_diagonal_ru = True
            else:
                done_diagonal_ru = True
            dru += 1

        return valid
    
    def board_move(self, row, col, color):
        #Updates the board based on placing a piece of color "color" in the space indicated by "row" and "col" (col being column)
        assert((row in [0,1,2,3,4,5,6,7]) and (col in [0,1,2,3,4,5,6,7]) and (color == "B" or color == "W")) #precondition

        if color == "B":
            other = "W"
        else:
            other = "B"

        #Most of the process used in this method is exactly the same as the method used in is_valid(). The only difference is that where is_valid has valid = True, this method has a mechanism for flipping the pieces.
        done_row_left = False
        l = 1
        #Changes the row to the left of the new piece
        while l <= col and done_row_left == False:
            if self.boardList[row][col - l] == other:
                done_row_left = False
            elif (self.boardList[row][col - l] == color) and l != 1:
                for i in sorted(self.boardList[row])[col - l:(col + 1)]: #Iterates through the row from the existing piece of this player's color to the new piece, changing all the pieces to be this player's color
                    self.boardList[row][i] = color
                    done_row_left = True
            else:
                done_row_left = True
            l += 1

        done_row_right = False
        r = 1
        #Changes the row to the right of the new piece
        while r <= (7 - col) and done_row_right == False:
            if self.boardList[row][col + r] == other:
                done_row_right = False
            elif (self.boardList[row][col + r] == color) and r != 1:
                for i in sorted(self.boardList[row])[col:(col + r + 1)]: #Iterates through the row from the new piece to the existing piece of "color", changing the color of the end pieces and all pieces in between
                    self.boardList[row][i] = color
            else:
                done_row_right = True
            r += 1

        done_column_up = False
        u = 1
        #Changes the column above the new piece
        while u <= row and done_column_up == False:
            if self.boardList[row - u][col] == other:
                done_column_up = False
            elif (self.boardList[row - u][col] == color) and u != 1:
                for i in range((row - u), (row + 1)): #Iterates up the column using the same process as above
                    self.boardList[i][col] = color
            else:
                done_column_up = True
            u += 1

        done_column_down = False
        d = 1
        #Changes the column above the new piece
        while d <= (7 - row) and done_column_down == False:
            #print "got here"
            if self.boardList[row + d][col] == other:
                done_column_down = False
            elif (self.boardList[row + d][col] == color) and d != 1: 
                for i in range(row, (row + d + 1)): #Iterates down the column using the same process as above
                    self.boardList[i][col] = color
            else:
                done_column_down = True
            d += 1

        done_diagonal_lu = False
        dlu = 1
        #Changes the diagonal to the left and up from the new piece
        while (dlu <= row) and (dlu <= col) and done_diagonal_lu == False:
            if self.boardList[row - dlu][col - dlu] == other:
                done_diagonal_lu = False
            elif (self.boardList[row - dlu][col - dlu] == color) and dlu != 1:
                column = col - dlu
                for i in range((row - dlu), (row + 1)): #Iterates across the row
                    self.boardList[i][column] = color
                    column += 1 #Allows the column to change as the row is iterated across
            else:
                done_diagonal_lu = True
            dlu += 1

        done_diagonal_ld = False
        dld = 1
        #Changes the diagonal to the left and down from the new piece
        while (dld <= (7 - row)) and (dld <= col) and done_diagonal_ld == False:
            if self.boardList[row + dld][col - dld] == other:
                done_diagonal_ld = False
            elif (self.boardList[row + dld][col - dld] == color) and dld != 1:
                column = col
                for i in range((row), (row + dld + 1)): #Iterates through the row while changing the column, using a similar process to the above (+ vs - is different to switch the diagonal)
                    self.boardList[i][column] = color
                    column -= 1
            else:
                done_diagonal_ld = True
            dld += 1

        done_diagonal_rd = False
        drd = 1
        #Changes the diagonal to the right and down from the new piece
        while (drd <= (7 - row)) and (drd <= (7 - col)) and done_diagonal_rd == False:
            if self.boardList[row + drd][col + drd] == other:
                done_diagonal_rd = False
            elif (self.boardList[row + drd][col + drd] == color) and drd != 1:
                column = col
                for i in range((row), (row + drd + 1)): #Iterates through the row while changing the column, using a similar process to the above (+ vs - is different to switch the diagonal)
                    self.boardList[i][column] = color
                    column += 1
            else:
                done_diagonal_rd = True
            drd += 1

        done_diagonal_ru = False
        dru = 1
        #Changes the diagonal to the right and up from the new piece
        while (dru <= row) and (dru <= (7 - col)) and done_diagonal_ru == False:
            if self.boardList[row - dru][col + dru] == other:
                done_diagonal_ru == False
            elif (self.boardList[row - dru][col + dru] == color) and dru != 1:
                column = col + dru
                for i in range((row - dru), (row + 1)): #Iterates through the row while changing the column, using a similar process to the above (+ vs - is different to switch the diagonal)
                    self.boardList[i][column] = color
                    column -= 1
                done_diagonal_ru = True
            else:
                done_diagonal_ru = True
            dru += 1

#Super player class that human and computer players inherit from               
class Player:
    def __init__(self, color):
        self.color = color
        if color == "B":
            self.turn = True
        else:
            self.turn = False

#Human player (is a player that takes input from the user to make moves)
class Hum_Player(Player):
    pass #Has the some attributes as a player object, so it doesn't need its own constructor
 
    def player_move(self, game):
        #Allows a user to input a move, then calls board_move() to update the board with the player's move 
        assert(type(game) == type(Game(1)) and self.turn == True) #precondition
        
        coordinate = raw_input("Where would " + self.color + " like to place their piece? Format as two integers, row followed by column") #Gets the coordinate where the player wants to move from the user
        if (len(coordinate) > 0) and (coordinate[0] in ['0','1','2','3','4','5','6','7']) and (coordinate[1] in ['0','1','2','3','4','5','6','7']): #Checks that the player's input is a valid coordinate
            row = int(coordinate[0])
            col = int(coordinate[1])
            if not game.board.is_valid(row, col, self.color): #Checks that the move is valid
                print "That's not a valid move. Try again."
                self.player_move(game) #Gives the player another chance to move if the move was not valid
            else:
                game.board.board_move(row, col, self.color) #If the move is valid, the move will be made
        else: #If the user did not input valid coordinates they will be told as much and given another chance
            print "Please input your coordinate as a row followed by a column with no space or punctuation in between. For example, to move in row 4, column 2, you would type 42"
            self.player_move(game)

#Computer Player (is a player that independently decides what moves to make)
class Comp_Player(Player):
    pass #Has the some attributes as a player object, so it doesn't need its own constructor

    def player_move(self, game):
        #Moves in a corner if possible, or makes the move that will flip the largest number of pieces if not. When multiple moves flip the same number of pieces, it will choose the one that is furthest to the right and down on the board.
        #Since this method primarily makes a move based off the assumption that choosing the optimal move in each turn will result in the optimal strategy over all, it is essentially a greedy algorithm.
        assert(type(game) == type(Game(1)) and self.turn == True) #precondition

        #This block of code tells the computer to move in a corner if it can
        if game.board.is_valid(0,0,self.color): 
            game.board.board_move(0,0,self.color)
        elif game.board.is_valid(0,7,self.color):
            game.board.board_move(0,7,self.color)
        elif game.board.is_valid(7,7,self.color):
            game.board.board_move(7,7,self.color)
        elif game.board.is_valid(7,0,self.color):
            game.board.board_move(7,0,self.color)

        #If no corner is available, the next block of code makes the move that flips the largest number of pieces
        else:
            counts = {} #Keeps track of all valid moves (as keys), and the number of times self.color is on the board after each potential move (as values)
            for ind,row in enumerate(game.board.boardList):
                for col in row: #Nested loops iterate through every space on the board
                    temp_board = Board()
                    temp_board = deepcopy(game.board) #Creates a temporary board that is identical to the current game board to test the results of the moves (without affecting the current game board)
                    if temp_board.is_valid(ind, col, self.color): #Checks if the current space is a valid move
                        temp_board.board_move(ind, col, self.color) #If the current move is valid, it makes the move
                        counts[str(ind) + str(col)] = 0 #Adds the current move to the dictionary of valid moves
                        for i in temp_board.boardList: #This nested loop adds tally of all times self.color appears on the board as a result of the current move, and updates the dictionary of valid moves
                            for n in i:
                                if i[n] == self.color:
                                    counts[str(ind) + str(col)] += 1
            values = []
            for i in counts:
                values += [counts[i]] #Creates a list with integer items representing the number of occurrences of self.color after all potential valid moves
            most = sorted(values)[-1] #This is the highest potential number of occurrences
            for i in counts:
                if counts[i] == most: #Finds the move that created the highest number of occurrences
                    row = int(i[0])
                    col = int(i[1])
            print "The all knowing computer has made the wise and cosidered decision to move in space " + str(row) + str(col) #Tells the user where the computer will move
            game.board.board_move(row, col, self.color) #Makes the move that creates the highest number of occurrences on the actual game board

        
#Maintains the flow of a game, keeping track of both players and the board, as well as ending/restarting the game as necessary
class Game:
    def __init__(self, num):
        assert(num == 0 or num == 1 or num == 2) #precondition
        
        self.board = Board()

        #num represents if the user wants to play with zero, one, or two players
        if num == 0: #If the user selects 0 the computer will play against itself
            self.p_one = Comp_Player("B")
            self.p_two = Comp_Player("W")
        elif num == 1: #If the user selects 1, then player two will be the computer player.
            self.p_one = Hum_Player("B")
            self.p_two = Comp_Player("W")
        else: #If the user selects 2, both players will be human players
            self.p_one = Hum_Player("B")
            self.p_two = Hum_Player("W")

    def game_move(self):
        #Intitiates the correct player_move method based off whose turn it is and if there are valid moves available, and calls end_game() when necessary
        game_over = True
        for i in self.board.boardList: #If there are no empty spaces, the game is over
            for n in i:
                if i[n] == ".":
                    game_over = False
        p1_can_move = False
        p2_can_move = False
        for ind,y in enumerate(self.board.boardList): #Checks that each player has at least one valid move on the board
            for x in y:
                if self.board.is_valid(ind, x, self.p_one.color):
                    p1_can_move = True
                if self.board.is_valid(ind, x, self.p_two.color):
                    p2_can_move = True
        if (not p1_can_move) and (not p2_can_move): #If neither player can move, the game is over
            game_over = True               
        elif self.p_one.turn: #If the game is not over, and it is p_one's turn, and p_one can move, p_one must move, so player_move will be called
            if p1_can_move:
                self.p_one.player_move(self)
            self.p_one.turn = False #After p_one moves, it becomes p_two's turn and not p_one's turn
            self.p_two.turn = True
        elif self.p_two.turn: #If the game is not over, and it is p_two's turn, and p_two can move, p_two must move, so player_move will be called
            if p2_can_move:
                self.p_two.player_move(self)
            self.p_two.turn = False #After p_two moves, it becomes p_one's turn and not p_two's turn
            self.p_one.turn = True
        print self.board #It prints the board after every move
        if game_over == False: #If the game is not over, game_move recurses to continue the game
            self.game_move()
        else: #If the game is over, the end method will be called
            self.end_game()


    def end_game(self):
        #Declares the winner, prints the score, and calls again() to offer the user a chance to play again
        print "Game Over"
        b_score = 0 #Black's score
        w_score = 0 #White's score
        for i in self.board.boardList: #Nested loops check every square and tally up the occurrences of each color
            for n in i:
                if i[n] == "B":
                    b_score += 1
                elif i[n] == "W":
                    w_score += 1
        if b_score > w_score:
            print "Black wins! Black got a score of " + str(b_score) + " and white got a score of " + str(w_score) + "!"
        elif w_score > b_score:
            print "White wins! Black got a score of " + str(b_score) + " and white got a score of " + str(w_score) + "!"
        else:
            print "It's a tie!"
        self.again() #Calls the method to offer the user the chance to play again
            
    def again(self):
        #Offers the user a chance to play again, and ends the game if the user does not want to
        again = raw_input("Would you like to play again? If so type 'y' and if not type 'n'")
        if again == "y":
            start_reversi() #Calls the independent function that starts a new game
        elif again == "n":
            print "Okay, bye! I hope you've enjoyed your time with Hannah's fun world of Reversi. Have a nice day!"
        else: 
            print "Please type either y or n. There are no other options. Don't try any of this tomfoolery with me."
            self.again() #If the user inputs anything other than y or n they will be forced to continue inputing until they input one of these choices




def start_reversi():
    #An independent function that gives basic instructions for the game and generates a new game object with the desired number of players
    print ("Welcome to reversi. The board is an 8x8 grid.\
 When you place a piece in a space, any pieces of the opponent's color that are in a straight line and bounded by the piece just placed and another piece of your color are turned over to your color. (Credit to Wikipedia for this description of the rules)\
 A period represents an empty space. You can only place pieces in empty spaces. Every piece placed MUST change the color of other pieces.\
 Otherwise it will not be a valid move, which the computer will kindly alert you of. When you input coordinates, make sure to notice that the first row and column are 0, not 1. This was made by a computer scientist. Deal with it.\
 I hope you enjoy the game!")
    b = Board()
    print b
    num = raw_input("Would you like to play with 0 players (have the computer play itself), 1 player (you can play against the computer), or 2 players (pass the computer between you and another human)? (Please state answer as integer)")
    if (num == '0') or (num == '1') or (num == '2'):
        g1 = Game(int(num))
        g1.game_move()
    else:
        print "You must input either 0, 1, or 2 (in integer form). Don't try that 'one' nonsense on me. Or any 2.0 foolishness. Or a non 1 or 2 integer, like 42. All we need is a nice 1 or 2."
        return start_reversi()

start_reversi() #A game is automatically started when the module is run
        
