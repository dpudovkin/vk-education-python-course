"""The main module"""

from itertools import cycle
import game


def convert_turn_input(input_str):
    """" Convert turn input method """

    arr = input_str.split()
    if len(arr) != 2:
        print('Incorrect turn input')
        return None
    if not arr[0].isdigit() or not arr[1].isdigit():
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
    print("Each player's turn is two numbers - the coordinates of the board")
    tic_tac.start()

    while tic_tac.get_winner() is None:
        current_player = next(player_pool)
        print(f'{current_player} is your turn:', end="")
        args = convert_turn_input(input())
        if args is not None:
            tic_tac.turn(current_player, args[0], args[1])
            tic_tac.show_board()

    print(f"Game over. {tic_tac.get_winner()} win!")


if __name__ == '__main__':
    start()
