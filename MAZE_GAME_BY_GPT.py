#THIS IS THE CODE TO MAKE A MAZE GAME

import random

#step 1 - create a function which defines the maze
def create_maze():
    maze = [
        [1, 0, 1, 1, 1],
        [1, 1, 1, 0, 1],
        [1, 0, 1, 1, 0],
        [1, 1, 0, 1, 1],
        [1, 1, 1, 1, 1]
    ]
    return maze

#step 2 - create a function which will print out the maze
def print_maze(maze, player_row, player_col):
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if i == player_row and j == player_col:
                print("P", end=" ")  # Player's position
            elif maze[i][j] == 1:
                print("#", end=" ")  # Wall
            else:
                print(" ", end=" ")  # Open path
        print()

#step 3 - function to move players
def move_player(maze, player_row, player_col, move):
    new_row, new_col = player_row, player_col

    if move == "W":
        new_row -= 1
    elif move == "S":
        new_row += 1
    elif move == "A":
        new_col -= 1
    elif move == "D":
        new_col += 1

    if 0 <= new_row < len(maze) and 0 <= new_col < len(maze[0]) and maze[new_row][new_col] == 0:
        return new_row, new_col
    else:
        return player_row, player_col

#step 4 - Main function which will start the game
def play_game():
    maze = create_maze()
    player_row, player_col = 0, 0

    print("Welcome to Number Maze!")
    print("Find the path to the exit (P) using W (Up), S (Down), A (Left), D (Right).")
    
    while True:
        print_maze(maze, player_row, player_col)
        move = input("Enter your move (W/S/A/D): ").upper()
        player_row, player_col = move_player(maze, player_row, player_col, move)
        
        if player_row == len(maze) - 1 and player_col == len(maze[0]) - 1:
            print("Congratulations! You've reached the exit!")
            break

#calling the function to run only when this actual file is running and not when it is imported somewhere else's code
if __name__ == "__main__":
    play_game()
