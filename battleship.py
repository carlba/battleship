# -*- coding: utf-8 -*-
import sys
from random import randint




def create_board(amount):
    board = []
    for x in range(5):
        board.append(["O"] * 5)
    return board

def print_board(board):
    for row in board:
        print " ".join(row)


def create_ship(row,col):
    ship = [row,col]
    return ship

def create_ship_list(amount, board_row_size, board_col_size):
    ships = []
    for ship_number in range(amount):
        ship = create_ship(randint(0, board_row_size), randint(0, board_col_size))
        ships.append(ship)
    return ships

def validate_ships(ship_list,guess_row,guess_col):
    hit= None
    for ship in ship_list:
        if guess_row == ship[0] and guess_col == ship[1]:
            hit = ship
    return hit

def get_hits_on_board(board):
    hits=[]

    for i, row in enumerate(board):
        for j,col in enumerate(row):
            if col == "✔":
                hits.append([i,j])
    return hits


def validate_guess(guess_row, guess_col):
    return (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4)


def mark_position_on_board(board,row,col,char):
    board[row][col] = char


def main():

    amount_of_ships =2
    cheat = True


    board = create_board(5)

    board_row_size = len(board) - 1
    board_col_size = len(board[0]) - 1

    ship_list = create_ship_list(amount_of_ships, board_row_size, board_col_size)

    if cheat:
        print "The ships are at: %s" % repr(ship_list)

    range_list=range(1000)

    print "Let's play Battleship!"
    print_board(board)

    for turn in range_list:

        guess_row = int(raw_input("Guess Row:")) -1
        guess_col = int(raw_input("Guess Col:")) -1

        ship = validate_ships(ship_list,guess_row,guess_col)


        if ship:
            board[guess_row][guess_col] = "✔"

            if len(get_hits_on_board(board)) == amount_of_ships:
                print "You won! All my ships are gone!"
                break
            else:
                print "Congratulations! You sunk one of my battleship!"
        else:
            if validate_guess(guess_row, guess_col):
                print "Oops, that's not even in the ocean."
            elif(board[guess_row][guess_col] == "X"):
                print "You guessed that one already."
                print range_list[:1]
                range_list.append(range_list[-1]+1)
            elif(board[guess_row][guess_col] == ""):
                print "You entered an empty guess"
            else:
                print "You missed my battleship!"
                board[guess_row][guess_col] = "X"
                if turn == 3:
                    print "Game Over"
            print turn+1
        print_board(board)


if __name__ == '__main__':
    main()


