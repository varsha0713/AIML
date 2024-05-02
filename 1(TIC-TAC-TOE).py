board=[" " for x in range (9)]
def print_board():
    row1="|{}|{}|{}|".format(board[0],board[1],board[2])
    row2="|{}|{}|{}|".format(board[3],board[4],board[5])
    row3="|{}|{}|{}|".format(board[6],board[7],board[8])
    print()
    print(row1)
    print(row2)
    print(row3)
    print()
def player_move(icon):
    if icon=="X":
        number=1
    elif icon=="O":
        number=2
    print("Your turn player{}".format(number))
    choice=int(input("enter your move(1-9):").strip())
    if board[choice-1]==" ":
        board[choice-1]=icon
    else:
        print()
        print("that space is taken!")
def is_victory(icon):
    if(board[0]==icon and board[1]==icon and board[2]==icon) or\
    (board[3]==icon and board[4]==icon and board[5]==icon) or\
    (board[6]==icon and board[7]==icon and board[8]==icon) or\
    (board[0]==icon and board[3]==icon and board[6]==icon) or\
    (board[1]==icon and board[4]==icon and board[7]==icon) or\
    (board[2]==icon and board[5]==icon and board[8]==icon) or\
    (board[0]==icon and board[4]==icon and board[8]==icon) or\
    (board[2]==icon and board[4]==icon and board[6]==icon):
        return True
    else:
        return False
    
def is_draw():
    if " " not in board:
        return True
    else:
        return False
while True:
        print_board()
        player_move("X")
        print_board()
        if is_victory("X"):
            print("X wins ! congrats")
            break
        elif is_draw():
            print("Its draw!")
            break
        player_move("O")
        if is_victory("O"):
            print_board()
            print("O wins! congrats")
            break
        elif is_draw():
            print("Its a draw")
            break


OUTPUT:

| | | |
| | | |
| | | |

Your turn player1
enter your move(1-9):2

| |X| |
| | | |
| | | |

Your turn player2
enter your move(1-9):3

| |X|O|
| | | |
| | | |

Your turn player1
enter your move(1-9):1

|X|X|O|
| | | |
| | | |

Your turn player2
enter your move(1-9):6

|X|X|O|
| | |O|
| | | |

Your turn player1
enter your move(1-9):9

|X|X|O|
| | |O|
| | |X|

Your turn player2
enter your move(1-9):5

|X|X|O|
| |O|O|
| | |X|

Your turn player1
enter your move(1-9):4

|X|X|O|
|X|O|O|
| | |X|

Your turn player2
enter your move(1-9):6

that space is taken!

|X|X|O|
|X|O|O|
| | |X|

Your turn player1
enter your move(1-9):8

|X|X|O|
|X|O|O|
| |X|X|

Your turn player2
enter your move(1-9):7

|X|X|O|
|X|O|O|
|O|X|X|

O wins! congrats
