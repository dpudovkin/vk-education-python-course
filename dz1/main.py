"""The main module"""

from itertools import cycle
import re
import game


def convert_turn_input(input_str):
    """" Convert turn input method """

    arr = input_str.split()
    if len(arr) != 2:
        print('Incorrect turn input')
        return None
    if not re.match('[0-2]', arr[0]) or not re.match('[0-2]', arr[1]):
        print('Incorrect turn input')
        return None
    return [int(arr[0]), int(arr[1])]


def start():
    """" Start method """

    print('Input players name...')
    player_a, player_b = input(), input()

    if player_a == player_b:
        player_a = f"{player_a}_1"
        player_b = f"{player_b}_2"

    player_pool = cycle([player_a, player_b])

    tic_tac = game.TicTacGame(player_a, player_b)
    print("Each player's turn is two numbers - the coordinates of the board. ",
          "From 0 to 2. Example: 0 2")
    tic_tac.start()

    while tic_tac.get_winner() is None:
        tic_tac.show_board()
        current_player = next(player_pool)
        print(f'{current_player} is your turn:', end="")
        args = convert_turn_input(input())
        if args is not None:
            err = tic_tac.turn(current_player, args[0], args[1])
            if err is None:
                next(player_pool)
                continue
        else:
            next(player_pool)

    print(f"Game over. {tic_tac.get_winner()} win!")


if __name__ == '__main__':
    start()
