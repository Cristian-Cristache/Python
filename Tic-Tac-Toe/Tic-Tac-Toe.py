import random
import sys

# Begins or closes the game after init.

def begin():
    
    FREE_SQUARES = SQUARE[:]
    
    name = input("Enter your name: ")
    answer = input("Hello, " + name + ". Welcome to Tic-Tac-Toe!\nAre you ready to begin the game? (y|n): ")
    answer = answer.upper()
    if answer == "N":
        print("You have closed the game. Have a nice day!")
        sys.exit()
    elif answer == "Y":
        list_of_free_squares(FREE_SQUARES, 0)
    else:
        answer = input("You have entered an invalid answer. Press \"Enter\" to continue.")
        begin()

# Creates a list of available squares after every move.
    
def list_of_free_squares(FREE_SQUARES, counter):
    
    if len(FREE_SQUARES) > 0:
        FREE_SQUARES = SQUARE[:]
        try:
            for i in range(len(FREE_SQUARES)):
                FREE_SQUARES.remove("X")
                FREE_SQUARES.remove("O")
        except ValueError:
            #print(FREE_SQUARES)  #Testing purposes
            victory_for(FREE_SQUARES, counter)
        except:
            print("An unknown error occurred.")
    else:
        victory_for(FREE_SQUARES, counter)

# The AI will randomly select an integer from the list of available squares.
# It will only use X's.
    
def draw_move(FREE_SQUARES, counter):
    
    cpu_move = random.choice(FREE_SQUARES)
        
    if SQUARE[cpu_move - 1] != "O" and SQUARE[cpu_move - 1] != "X":
        SQUARE[cpu_move - 1] = "X"
           
    display_board()
    list_of_free_squares(FREE_SQUARES, counter)

# The player will be asked to enter the desired square. If the value is incorrect, it will try again.
# You will only use O's.

def enter_move(FREE_SQUARES, counter):
    
    try:
        player_move = int(input("Please enter a number: "))
        if player_move < 1 or player_move > 9:
            print("The number you have entered is out of range. Please try again.")
            enter_move(FREE_SQUARES, counter)
        elif player_move not in FREE_SQUARES:
            print("That square has already been used. Please try again.")
            enter_move(FREE_SQUARES, counter)
    except ValueError:
        print("Letters or symbols are not allowed. Please try again.")
        enter_move(FREE_SQUARES, counter)
        
    SQUARE[player_move - 1] = "O"
    list_of_free_squares(FREE_SQUARES, counter)
    
# Defines the outcome of the game: Lose, Win or Tie. Otherwise it will continue.
# The AI will always make the first move.
                                    
def victory_for(FREE_SQUARES, counter):
        
    if SQUARE[0] == SQUARE[4] == SQUARE[8] == "X" or SQUARE[2] == SQUARE[4] == SQUARE[6] == "X" \
    or SQUARE[0] == SQUARE[3] == SQUARE[6] == "X" or SQUARE[1] == SQUARE[4] == SQUARE[7] == "X" \
    or SQUARE[2] == SQUARE[5] == SQUARE[8] == "X" or SQUARE[0] == SQUARE[1] == SQUARE[2] == "X" \
    or SQUARE[3] == SQUARE[4] == SQUARE[5] == "X" or SQUARE[6] == SQUARE[7] == SQUARE[8] == "X": 
        counter = -1
        display_board()
        print("You have lost. Better luck next time.")
        
    elif SQUARE[0] == SQUARE[4] == SQUARE[8] == "O" or SQUARE[2] == SQUARE[4] == SQUARE[6] == "O" \
    or SQUARE[0] == SQUARE[3] == SQUARE[6] == "O" or SQUARE[1] == SQUARE[4] == SQUARE[7] == "O" \
    or SQUARE[2] == SQUARE[5] == SQUARE[8] == "O" or SQUARE[0] == SQUARE[1] == SQUARE[2] == "O" \
    or SQUARE[3] == SQUARE[4] == SQUARE[5] == "O" or SQUARE[6] == SQUARE[7] == SQUARE[8] == "O":
        counter = -1
        display_board()
        print("Congratulations! You have won.")
    elif len(FREE_SQUARES) == 0:
        counter = -1
        display_board()
        print("The game has ended in a tie.")
        
    if counter % 2 == 0 and counter >= 0:
        counter += 1
        draw_move(FREE_SQUARES, counter) 
    elif counter % 2 != 0 and counter >= 0:
        counter += 1
        enter_move(FREE_SQUARES, counter)
    else:
        end()

# You can start another round, if you wish to continue, or exit.

def end():
        
    answer = input("Would you like to continue? (y|n): ")
    answer = answer.upper()
    if answer == "N":
        print("You have closed the game. Have a nice day!")
        sys.exit()
    elif answer == "Y":
        for i in range(len(SQUARE)):
            SQUARE[i] = i + 1
        begin()
    else:
        answer = input("You have entered an invalid answer. Press \"Enter\" to continue.")
        end()       

# Generates the board display during each round.

def display_board():

    print("+" + ("-" * 7 + "+") * 3)
    print("|" + (" " * 7 + "|") * 3)
    
    for d in range(len(SQUARE)):
        x = int(d + 1)
        
        if x % 3 == 1:
            print("|" + " " * 3 + str(SQUARE[d]) + " " * 3 + "|", end="")
        
        elif x % 3 == 0 and x < 9:
            print(" " * 3 + str(SQUARE[d]) + " " * 3 + "|", end="\n")
            print("|" + (" " * 7 + "|") * 3)
            print("+" + ("-" * 7 + "+") * 3)
            print("|" + (" " * 7 + "|") * 3)
            
        elif x % 9 == 0:
            print(" " * 3 + str(SQUARE[d]) + " " * 3 + "|", end="\n")
            print("|" + (" " * 7 + "|") * 3)
            print("+" + ("-" * 7 + "+") * 3)
        
        else:
            print(" " * 3 + str(SQUARE[d]) + " " * 3 + "|", end="")

# Main body.

SQUARE = [1, 2, 3, 4, 5, 6, 7, 8, 9]
display_board()    
begin()



  

    