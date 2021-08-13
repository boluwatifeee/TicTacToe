import random


# Create a display board
def display_board(board):
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')


# Create function for player to select a marker
def player_input():
    marker = ''

    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1: Do you want to be X or O? ').upper()

    if marker == 'X':
        return 'X', 'O'
    else:
        return 'O', 'X'


def place_marker(board, marker, spot):
    board[spot] = marker


def win_check(board, mark):
    if board[1] == board[2] == board[3] == mark:  # Last row
        return True
    if board[4] == board[5] == board[6] == mark:  # Second row
        return True
    if board[7] == board[8] == board[9] == mark:  # First row
        return True
    if board[1] == board[4] == board[7] == mark:  # First column
        return True
    if board[2] == board[5] == board[8] == mark:  # Middle column
        return True
    if board[3] == board[6] == board[9] == mark:  # Third column
        return True
    if board[1] == board[5] == board[9] == mark:  # Diagonal 1
        return True
    if board[3] == board[5] == board[7] == mark:  # Diagonal 2
        return True
    return False


def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'


def space_check(board, spot):
    return board[spot] == ' '


def full_board_check(board):
    for i in range(1, 10):
        if space_check(board, i):
            return False
    return True


def player_choice(board):
    spot = 0

    while spot not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board,spot):
        spot = int(input('Choose your next spot: (1-9) '))

    return spot


def replay():
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')


print('Welcome to Tic Tac Toe!')

while True:
    # Clear
    new_board = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' will go first.')

    play_game = input('Are you ready to play? Enter Yes or No.')

    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False
        print('Game over')

    while game_on:
        if turn == 'Player 1':
            # Player1's turn.

            display_board(new_board)
            spot = player_choice(new_board)
            place_marker(new_board, player1_marker, spot)

            if win_check(new_board, player1_marker):
                display_board(new_board)
                print('Congratulations! You have won the game!')
                game_on = False
            else:
                if full_board_check(new_board):
                    display_board(new_board)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 2'

        else:
            # Player2's turn.

            display_board(new_board)
            spot = player_choice(new_board)
            place_marker(new_board, player2_marker, spot)

            if win_check(new_board, player2_marker):
                display_board(new_board)
                print('Player 2 has won!')
                game_on = False
            else:
                if full_board_check(new_board):
                    display_board(new_board)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 1'

    if not replay():
        break
