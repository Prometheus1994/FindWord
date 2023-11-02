import nltk
nltk.download()
from nltk.corpus import words
words = words.words()
input_word = "ba_a_a"
solutions = []
for word in words:
    counter = 0
    if len(word) != len(input_word):
        continue
    else:
        for i in range(len(word)):
            if word[i] == input_word[i] or input_word[i] == '_':
                counter += 1
            else:
                break
    if counter == len(input_word):
        solutions.append(word)
