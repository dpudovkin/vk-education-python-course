"""" main module """


def levenshtein_distance(str1, str2):
    """ function that calculates the levenshtein distance """

    dynamic = [[0 for i in range(len(str2) + 1)] for j in range(len(str1) + 1)]
    for i in range(len(str1) + 1):
        dynamic[i][0] = i
    for j in range(len(str2) + 1):
        dynamic[0][j] = j

    for i in range(1, len(str1) + 1):
        for j in range(1, len(str2) + 1):
            diff = 0 if str1[i - 1] == str2[j - 1] else 1
            dynamic[i][j] = min(dynamic[i][j - 1] + 1, dynamic[i - 1][j] + 1,
                                dynamic[i - 1][j - 1] + diff)

    return dynamic[len(str1)][len(str2)]


def main():
    """ main function """
    str1, str2 = input(), input()
    print(levenshtein_distance(str1, str2))


if __name__ == '__main__':
    main()
