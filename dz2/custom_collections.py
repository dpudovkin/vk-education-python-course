"""" Module of custom collections """


class CustomList(list):
    """" Class of custom list """

    @staticmethod
    def __align_lists(list_a, list_b):
        max_length = max(len(list_a), len(list_b))
        a_list, b_list = list_a.copy(), list_b.copy()
        a_list.extend([0] * (max_length - len(list_a)))
        b_list.extend([0] * (max_length - len(list_b)))
        return a_list, b_list, max_length

    def __add__(self, other):
        result = self.__align_lists(self, other)
        return CustomList([result[0][i] + result[1][i] for i in range(result[2])])

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        result = self.__align_lists(self, other)
        return CustomList([result[0][i] - result[1][i] for i in range(result[2])])

    def __rsub__(self, other):
        result = self.__align_lists(other, self)
        return CustomList([result[0][i] - result[1][i] for i in range(result[2])])

    def __eq__(self, other):
        return sum(self) == sum(other)

    def __ne__(self, other):
        return sum(self) != sum(other)

    def __lt__(self, other):
        return sum(self) < sum(other)

    def __gt__(self, other):
        return sum(self) > sum(other)

    def __le__(self, other):
        return sum(self) <= sum(other)

    def __ge__(self, other):
        return sum(self) >= sum(other)
