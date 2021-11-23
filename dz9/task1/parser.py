import requests
from bs4 import BeautifulSoup
from collections import Counter


def frequent_word(text, word_number):
    wordlist = []
    source_code = text
    soup = BeautifulSoup(source_code, 'html.parser')

    for each_text in soup.findAll('div'):
        content = each_text.text
        words = content.lower().split()

        for each_word in words:
            wordlist.append(each_word)

    word_count = clean_wordlist(wordlist)
    c = Counter(word_count)
    top = c.most_common(word_number)

    word_dict ={}
    for elem in top:
        word_dict[elem[0]]=elem[1]

    return word_dict


def clean_wordlist(wordlist):
    clean_list = []
    for word in wordlist:
        symbols = "!@#$%^&*()_-+={[}]|\;:\"<>?/., "

        for i in range(len(symbols)):
            word = word.replace(symbols[i], '')

        if len(word) > 0:
            clean_list.append(word)
    return word_dictionary(clean_list)


def word_dictionary(clean_list):
    word_count = {}
    for word in clean_list:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count
