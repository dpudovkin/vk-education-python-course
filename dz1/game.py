"""The game module contains TicTacGame class"""


class TicTacGame:
    """The TicTacGame object contains game logic"""

    def __init__(self, player_a, player_b):
        self.empty_sign = "_"
        self.dim = 3

        self.board = [[self.empty_sign for _ in range(self.dim)] for _ in range(self.dim)]
        self.signs = {player_a: 'X', player_b: 'O'}
        self.player_b = player_b
        self.player_a = player_a
        self.numbers = {"O": 2, "X": 3, self.empty_sign: 1}

    def turn(self, player, x_index, y_index):

        """" Next turn method """

        if self.board[x_index][y_index] != self.empty_sign:
            print("This cell is occupied")
            return None
        if x_index not in range(self.dim) or y_index not in range(self.dim):
            print("Incorrect cell index")
            return None
        
        self.board[x_index][y_index] = self.signs.get(player, self.empty_sign)
        return 0

    def start(self, msg=True):

        """" Start game method """

        self.board = [[self.empty_sign for _ in range(self.dim)] for _ in range(self.dim)]
        if msg:
            print(f"{self.player_a} is {self.signs[self.player_a]}")
            print(f"{self.player_b} is {self.signs[self.player_b]}\n")

    def show_board(self):

        """" Show board method """

        print('Board:')
        for row in self.board:
            for val in row:
                print(f"{val} ", end="")
            print()

    def get_winner(self):

        """" Get winner method """

        def multiply_array(array):
            result = 1
            for val in array:
                result *= self.numbers[val]
            return result

        m_list = []
        m_list.extend(map(multiply_array, self.board))
        m_list.extend(map(lambda i: multiply_array([self.board[j][i] for j in range(3)]), range(3)))
        m_list.append(multiply_array([self.board[j][j] for j in range(self.dim)]))
        m_list.append(multiply_array([self.board[2 - j][j] for j in range(self.dim)]))

        number_a = self.numbers[self.signs[self.player_a]]
        number_b = self.numbers[self.signs[self.player_b]]
        player_a = list(filter(lambda val: (val % pow(number_a, self.dim)) == 0, m_list))
        player_b = list(filter(lambda val: (val % pow(number_b, self.dim)) == 0, m_list))

        if player_a:
            return self.player_a
        if player_b:
            return self.player_b

        if not any(self.empty_sign in sublist for sublist in self.board):
            return f"{self.player_a} and {self.player_b}"

        return None
