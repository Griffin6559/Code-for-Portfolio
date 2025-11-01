from time import sleep
import random
import os

def main():
    os.system('clear')
    player_name=input("Player name: ")
    os.system('clear')
    intro()

    board = [[1, 0, 0],
             [2, 0, 0],
             [3, 0, 0],
             [4, 0, 0],
             [5, 0, 0],
             [6, 0, 0],
             [7, 0, 0]]

    mouse_location= random.randint(0,6)
    mouse_specific_position=random.randint(1,2)
    show(board)


    while True:
        print()
        print("Where is the mouse?")
        print()
        row = int(input("Type where you think the mouse is: "))-1

        if stop_mouse(row,mouse_location,board)==2:
            print()
            show(board)
            print()
            print("Not there!")
        if stop_mouse(row,mouse_location,board)==0:
            guess_col= int(input(f"You can hear the mouse skittering about in row {row +1}! \nWhich column do you think the mouse is in?"))
            find_specific_position(guess_col,board,row,mouse_specific_position)
            if find_specific_position(guess_col,board,row,mouse_specific_position) ==4:
                guess_col= int(input("Not there! Which other column do you think the mouse is in?"))
                find_specific_position(guess_col,board,row,mouse_specific_position)
                print()
                show(board)
            if find_specific_position(guess_col,board,row,mouse_specific_position) ==1:
                mouse_appearance(board,mouse_location,mouse_specific_position)
                os.system('clear')
                show(board)
                print()
                print(f"Congratulations {player_name}! \nYou found the mouse!")
                break




def intro():
    start=input("Are you ready to start? \n (type 'yes' to start) \n")
    if start=="yes":
        print("Try to find the mouse!")
        sleep(2)
        os.system('clear')
        print("Let the game begin!")
        sleep(2)


def show(board):
    os.system('clear')
    for row in [0,1,2,3,4,5,6]:
        print()
        for col in[0,1,2]:
            if board[row][col]==0:
                print("🟫", end="")
            if board[row][col]=="x":
                print("🟥", end="")
            if board [row][col] !=0 and board[row][col] !="x" and board[row][col]!="m":
                print(board[row][0], end ="")

    return True


def stop_mouse(row,mouse_location,board):
    if row== mouse_location:
        return 0
    if row != mouse_location:
        for col in [1,2]:
            board[row][col]="x"
        return 2

def find_specific_position(guess_col,board,row,mouse_specific_position):
    if guess_col == mouse_specific_position:
        return 1
    if guess_col != mouse_specific_position:
        board[row][guess_col]="x"
        return 4


def mouse_appearance(board,mouse_location,mouse_specific_position):
    board[mouse_location][mouse_specific_position]="m"
    for row in [0,1,2,3,4,5,6]:
        print()
        for col in[0,1,2]:
            if board[row][col]=="m":
                print("🐭", end="")



main()
