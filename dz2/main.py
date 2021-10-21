"""" Main module """

from custom_collections import CustomList


def main():
    """ Main function """
    list_a = CustomList([-1, 3, 10])
    list_b = CustomList([1, 2, 7])
    print(list_a == list_b)
    print(list_a != list_b)
    print(list_a > list_b)
    print(list_a < list_b)
    print(list_a >= list_b)
    print(list_a <= list_b)


if __name__ == '__main__':
    main()
