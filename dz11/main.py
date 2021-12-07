
def levenshtein_distance(str1, str2):
    d = [[0 for i in range(len(str2)+1)] for j in range(len(str1)+1)]
    for i in range(len(str1)+1):
        d[i][0] = i
    for j in range(len(str2)+1):
        d[0][j] = j

    for i in range(1, len(str1)+1):
        for j in range(1, len(str2)+1):
            diff = 0 if str1[i-1] == str2[j-1] else 1
            d[i][j] = min(d[i][j - 1] + 1, d[i - 1][j] + 1, d[i - 1][j - 1] + diff)

    return d[len(str1)][len(str2)]


def main():
    str1, str2 = input(), input()
    print(levenshtein_distance(str1, str2))


if __name__ == '__main__':
    main()
