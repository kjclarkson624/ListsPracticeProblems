## Write a Python program to find the list of words that are longer than n from a given list of words.

def long_words(n, str):
    word_list = []
    txt = str.split(" ")
    for word in txt:
        if len(word) > n:
            word_list.append(word)
    return word_list

def main():
    words = "This is a string of words. Most should appear."
    long_words(3, words)

main()