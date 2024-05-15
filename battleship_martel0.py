"""
Author: Jacob Martel, martel0@purdue.edu
Assignment: 12.1 - Battleship
Date: 11/17/2023

Description:
    This program will be our final project implementing a game of space battleship. Where the user has to sink our ships and try to get the highest score.
"""

#Imported Modules
import random as r
#import numpy as np


#menu function. Prints the title screen
def title():
    print("\n                   ~ Welcome to Battleship! ~                   ")
    print("\nChatGPT has gone rogue and commandeered a space strike fleet.")
    print("It's on a mission to take over the world.  We've located the")
    print("stolen ships, but we need your superior intelligence to help")
    print("destroy them before it's too late.\n")

#menu screen
def menu():
    print("Menu:")
    print("  1 : Instructions")
    print("  2 : View Example Map")
    print("  3 : New Game")
    print("  4 : Hall of Fame")
    print("  5 : Quit")

#Instruction screen
def instructions():
    print("\nInstructions:\n")
    print("Ships are positioned at fixed locations in a 10-by-12 grid. The")
    print("rows of the grid are labeled 0 through 9, and the colums are labeled A through L.")
    print("Use menu option '2' to see and example.")
    print("Target the ships by entering the row and column of the location you wish to shoot.")
    print("A ship is destroyed when all of the spaces it fills have been hit.")
    print("Try to destry the fleet with as few shots as possible.")
    print("The feet consists of the following 5 ships:\n")
    print("Size : Type")
    print("   5 : Mothership")
    print("   4 : Battleship")
    print("   3 : Destroyer")
    print("   3 : Stealth Ship")
    print("   2 : Patrol Ship\n")

#for the patrol ship
def place_patrol(board):
    
    #picks either vertical or horizontal
    orientation = r.choice(['vertical','horizontal'])
    #if vertical
    if orientation == 'vertical':
        #places the first P randomly
        row = r.randint(0,8)
        col = r.randint(1,10)
        board[row][col] = 'P'
        #has constraints depending on where the p is
        if row == 0:
            board[row + 1][col] = 'P'
        elif row == 9:
            board[row - 1][col] = 'P'
        else:
            a = r.choice([-1,1])
            board[row + int(a)][col] = 'P'
    if orientation == 'horizontal':
        #places the first P randomly
        row = r.randint(0,8)
        col = r.randint(1,10)
        board[row][col] = 'P'
        #has constraints depending on where the p is
        if col ==1:
            board[row][col + 1] ='P'
        elif col == 12:
            board[row][col-1] = 'P'
        else:
            a = r.choice([-1,1])
            board[row][col + int(a)] = 'P'
        return board
    
#Places the Stealth Ship on Board
def place_stealth(board):
    orientation = r.choice(['vertical', 'horizontal'])

    if orientation == 'vertical':
        row = r.randint(0, 7)
        col = r.randint(1, 10)

        while any(
            row + i < 0 or row + i > 9 or board[row + i][col] == 'P'
            for i in range(-1, 2)
        ):
            row = r.randint(0, 7)

        board[row][col] = 'S'
        board[row + 1][col] = 'S'
        board[row - 1][col] = 'S'

    if orientation == 'horizontal':
        row = r.randint(0, 9)
        col = r.randint(1, 8)

        while any(
            col + i < 1 or col + i > 10 or board[row][col + i] == 'P'
            for i in range(-1, 2)
        ):
            col = r.randint(1, 8)

        board[row][col] = 'S'
        board[row][col + 1] = 'S'
        board[row][col - 1] = 'S'

    return board

def destroyer_placement(board, row, col):
    return (
        0 <= row < len(board) and
        0 <= col < len(board[0]) and
        board[row][col] != 'S' and
        board[row][col] != 'P'
    )

#Placing the Destroyer function
def place_destroyer(board):
    orientation = r.choice(['up', 'down', 'left', 'right'])

    # If up is chosen
    if orientation == 'up':
        while True:
            row = r.randint(1, 7)
            col = r.randint(1, 9)
            if all([
                destroyer_placement(board, row, col),
                destroyer_placement(board, row + 1, col + 1),
                destroyer_placement(board, row + 1, col - 1),
            ]):
                break

        board[row][col] = 'D'
        board[row + 1][col + 1] = 'D'
        board[row + 1][col - 1] = 'D'

    # If down is chosen
    if orientation == 'down':
        while True:
            row = r.randint(0, 6)
            col = r.randint(0, 9)
            if all([
                destroyer_placement(board, row, col),
                destroyer_placement(board, row - 1, col + 1),
                destroyer_placement(board, row - 1, col - 1),
            ]):
                break

        board[row][col] = 'D'
        board[row - 1][col + 1] = 'D'
        board[row - 1][col - 1] = 'D'

    # Left orientation
    if orientation == 'left':
        while True:
            row = r.randint(0, 6)
            col = r.randint(1, 9)
            if all([
                destroyer_placement(board, row, col),
                destroyer_placement(board, row - 1, col + 1),
                destroyer_placement(board, row + 1, col + 1),
            ]):
                break

        board[row][col] = 'D'
        board[row - 1][col + 1] = 'D'
        board[row + 1][col + 1] = 'D'

    # Right orientation
    if orientation == 'right':
        while True:
            row = r.randint(0, 6)
            col = r.randint(0, 8)
            if all([
                destroyer_placement(board, row, col),
                destroyer_placement(board, row - 1, col - 1),
                destroyer_placement(board, row + 1, col - 1),
            ]):
                break

        board[row][col] = 'D'
        board[row - 1][col - 1] = 'D'
        board[row + 1][col - 1] = 'D'
#placing the mothership
def place_mothership(board):
    row= r.randint(1,8)
    col = r.randint(1,10)
    #check the surrounding conditions
    while any([board[row][col] == 'S' or board[row][col] == 'P' or board[row][col] == 'D',
               (row - 1) < 1,
               (row + 1) > 8,
               (col - 1) < 1,
               (col + 1)> 10,
               board[row -1][col - 1] == 'S' or board[row - 1][col - 1] == 'P' or board[row - 1][col - 1] == 'D',
               board[row -1][col + 1] == 'S' or board[row - 1][col + 1] == 'P' or board[row - 1][col + 1] == 'D',
               board[row +1][col - 1] == 'S' or board[row + 1][col - 1] == 'P' or board[row + 1][col - 1] == 'D',
               board[row +1][col + 1] == 'S' or board[row + 1][col + 1] == 'P' or board[row + 1][col + 1] == 'D'
                  ]):
            row= r.randint(1,8)
            col = r.randint(1,10)
     #print the mothership
    board[row][col] = 'M'
    board[row - 1][col - 1] = 'M'
    board[row -1][col +1] ='M'
    board[row +1][col -1] ='M'
    board[row + 1][col + 1] = 'M'

#placeing the battleship
def place_battleship(board):
    row = r.randint(2,9)
    col = r.randint(0,10)
    #check the surrounding conditions
    while any([board[row][col] == 'S' or board[row][col] == 'P' or board[row][col] == 'D' or board[row][col] == 'M',
               (row - 1) < 2,
               (row + 1) > 10,
               (col -1 ) < 1,
               (col + 1) > 12,
               board[row -1][col] == 'S' or board[row - 1][col] == 'P' or board[row - 1][col] == 'D' or board[row - 1][col] == 'M',
               board[row][col + 1] == 'S' or board[row][col + 1] == 'P' or board[row][col + 1] == 'D' or board[row][col + 1] == 'M',
               board[row - 1][col + 1] == 'S' or board[row - 1][col + 1] == 'P' or board[row - 1][col + 1] == 'D' or board[row - 1][col + 1] == 'M'
               ]):
        row = r.randint(2,9)
        col = r.randint(0,10)
    #place Ship
    board[row][col] = "B"
    board[row - 1][col] = 'B'
    board[row][col + 1] ='B'
    board[row - 1][col + 1] ='B'
#making the grid

def make_grid():
    #the default grid
    board = [[ "~","~",'~','~','~',"~","~",'~','~','~','~','~'],
             [ "~","~",'~','~','~',"~","~",'~','~','~','~','~'],["~","~",'~','~','~',"~","~",'~','~','~','~','~'],
             [ "~","~",'~','~','~',"~","~",'~','~','~','~','~'],["~","~",'~','~','~',"~","~",'~','~','~','~','~'],
             [ "~","~",'~','~','~',"~","~",'~','~','~','~','~'],["~","~",'~','~','~',"~","~",'~','~','~','~','~'],
             [ "~","~",'~','~','~',"~","~",'~','~','~','~','~'],["~","~",'~','~','~',"~","~",'~','~','~','~','~'],
             [ "~","~",'~','~','~',"~","~",'~','~','~','~','~']]
    #adding the Patrol Ship
    place_patrol(board)
    place_stealth(board)
    place_destroyer(board)
    place_mothership(board)
    place_battleship(board)
    
    return board

def print_grid(board):
    print("\n   A  B  C  D  E  F  G  H  I  J  K  L")
    for i, row in enumerate(board):
        print(f"{i} ", end="")
        for cell in row:
            print(f" {cell} ", end="")
        print()
    print()
#this function will take the current board and users decision as an input
def player_input(decision):
    error_message = ""
    row = 0
    upper_letter = ''

    if not decision:
        error_message = 'Please enter a location in the form "6G".\n'
        print(error_message)
        return None

    if len(decision) != 2:
        error_message = "Please enter exactly two characters.\n"
    elif not decision[0].isdigit():
        error_message = 'Please enter a location in the form "6G".\n'
    else:
        try:
            row = int(decision[0])
            upper_letter = decision[1].upper()
            if upper_letter not in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L']:
                error_message = 'Please enter a location in the form "6G".\n'
        except ValueError:
            error_message = 'Please enter a location in the form "6G".\n'

    if error_message:
        print(error_message)
        return None

    return [row, upper_letter]
#this function will take a list of the user input and map it to the grid
def collision(target, random_grid, default_grid):
    if target is None or target == 'q':
        return default_grid

    col_dict = {'A': 0, 'B': 1, 'C': 2, 'D': 3, "E": 4, 'F': 5, 'G': 6, "H": 7, 'I': 8, 'J': 9, 'K': 10, 'L': 11}

    row_value = target[0]
    col_value = col_dict[target[1]]

    # If a ship is hit
    if random_grid[row_value][col_value] in ["P", "S", "D", 'B', 'M']:
        default_grid[row_value][col_value] = 'x'
    else:
        # miss
        default_grid[row_value][col_value] = 'o'

    return default_grid

#function keeps track of whats been hit and returns it
def collision_counter(target, random_grid, default_grid):
    col_dict = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9, 'K': 10, 'L': 11}

    row_value = target[0]
    col_value = col_dict[target[1]]

    if random_grid[row_value][col_value] in ["P", "S", "D", 'B', 'M']:
        default_grid[row_value][col_value] = 'x'  
        return random_grid[row_value][col_value]
    else:
        default_grid[row_value][col_value] = 'o'  
        return 'o'


def accuracy_message(accuracy):
    
    with open('battleship_hof.txt','r') as txt:
        text = txt.readlines()
        
        existing = [line.strip().split(',') for line in text[1:]]

        if len(existing) < 10 or accuracy > float(existing[-1][0]):
            print("Congratulations, you have achieved a targeting accuracy of")
            print(f'{accuracy}% and earned a spot in the Hall of Fame.')
            player = input("Enter your name: ")
            existing.append([f'{accuracy:.2f}', player])

        existing = [[float(item) if isinstance(item, str) and item.replace('.', '').isdigit() else item for item in record] for record in existing]
        existing.sort(reverse=True)

        with open('battleship_hof.txt', 'w') as txt:
            txt.write("misses,name\n")
            for record in existing[:10]:
                txt.write(','.join(map(str,record)) + '\n')
            txt.close()
def print_hof(num_players=10):
    top_players = []
    with open('battleship_hof.txt', 'r') as txt:
        next(txt)
        for line in txt:
            data = line.strip().split(',')
            if data:
                score, name = data
                top_players.append((float(score), name))

    top_players.sort(reverse=True)
    top_players = top_players[:num_players]

    print("\nHall of Fame:")
    print("+------+-------------+----------+")
    print("| Rank | Player Name | Accuracy |")
    print("+------+-------------+----------+")

    for rank, (accuracy, name) in enumerate(top_players, start=1):
        # Adjusted widths for better alignment
        print(f"| {rank:^4} | {name[:11]:^11}| {accuracy:7.2f}% |")
    print("+------+-------------+----------+\n")
#main function
def main():
    # Prints the Menu
    title()
    menu()
    decision = input("What would you like to do? ")
    while decision:
        # Prints the instructions
        if decision == '1':
            instructions()
            menu()
            decision = input("What would you like to do? ")

        # Views an example of the map
        elif decision == '2':
            grid = make_grid()
            print_grid(grid)
            menu()
            decision = input("What would you like to do? ")

        # User plays the game
        elif decision == '3':
            m_count = 0
            p_count = 0
            b_count = 0
            d_count = 0
            s_count = 0
            hit = 0
            shot_count = 0
            grid = make_grid()
            used_list = []
            default = [
                ["~", "~", '~', '~', '~', "~", "~", '~', '~', '~', '~', '~'],
                ["~", "~", '~', '~', '~', "~", "~", '~', '~', '~', '~', '~'],
                ["~", "~", '~', '~', '~', "~", "~", '~', '~', '~', '~', '~'],
                ["~", "~", '~', '~', '~', "~", "~", '~', '~', '~', '~', '~'],
                ["~", "~", '~', '~', '~', "~", "~", '~', '~', '~', '~', '~'],
                ["~", "~", '~', '~', '~', "~", "~", '~', '~', '~', '~', '~'],
                ["~", "~", '~', '~', '~', "~", "~", '~', '~', '~', '~', '~'],
                ["~", "~", '~', '~', '~', "~", "~", '~', '~', '~', '~', '~'],
                ["~", "~", '~', '~', '~', "~", "~", '~', '~', '~', '~', '~'],
                ["~", "~", '~', '~', '~', "~", "~", '~', '~', '~', '~', '~']
            ]
            
            print_grid(default)

            target = None
            while hit < 17 and target != 'q':

                target = input("Where should we target next (q to quit)? ")

                # Break if 'q' entered
                if target == 'q':
                    break

                # When player input returns None
                target_list = player_input(target)
                if target_list is None:
                    continue

                # Checks if it's been used
                if target in used_list:
                    print("\nYou've already targeted that location\n")
                    print_grid(updated_graph)
                    continue
                else:
                    # Calls the collision function to update for hits or misses
                    updated_graph = collision(target_list, grid, default)

                    # Checks if you hit
                    ship_counter = collision_counter(target_list, grid, default)
                    if ship_counter != 'o':
                        print("\nIT'S A HIT!")
                        hit += 1
                        print_grid(updated_graph)

                        # Notify when a ship is sunk
                        if ship_counter == 'P':
                            p_count += 1
                            if p_count == 2:
                                print("The enemy's Patrol Ship has been destroyed.\n")
                        elif ship_counter == 'S':
                            s_count += 1
                            if s_count == 3:
                                print("The enemy's Stealth Ship has been destroyed.\n")
                        elif ship_counter == 'B':
                            b_count += 1
                            if b_count == 4:
                                print("The enemy's Battleship has been destroyed.\n")
                        elif ship_counter == 'D':
                            d_count += 1
                            if d_count == 3:
                                print("The enemy's Destroyer has been destroyed.\n")
                        elif ship_counter == 'M':
                            m_count += 1
                            if m_count == 5:
                                print("The enemy's MotherShip has been destroyed.\n")

                        # Check if all ships have been destroyed
                        if hit == 17:
                            print("You've destroyed the enemy fleet!")
                            print("Humanity has been saved from the threat of AI.\n")
                            print("For now ...\n")
                            # Accuracy message
                            accuracy_message(accuracy)
                            print_hof()
                    else:
                        # Miss
                        print("\nmiss")
                        print_grid(updated_graph)

                    # Update shot count and used list
                    shot_count += 1
                    used_list.append(target)

            if shot_count == 0:
                return None
            else:
                accuracy = round((hit / shot_count) * 100, 2)

            print("\n")
            menu()
            decision = input("What would you like to do? ")

        # Prints the hall of Fame
        elif decision == '4':
            print_hof()
            menu()
            decision = input("What would you like to do? ")

        # Quit the game
        elif decision == '5':
            print("\nGoodbye")
            break
        else:
            print("\nInvalid selection.  Please choose a number from the menu.\n")
            menu()
            decision = input("What would you like to do? ")

if __name__ == "__main__":
    main()