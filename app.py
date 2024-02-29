import nltk

nltk.download('words')

from flask import Flask, render_template, request
from nltk.corpus import words as nltk_words

app = Flask(__name__, static_url_path='/static')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/find_words', methods=['POST'])
def find_words():
    word_list = nltk_words.words()
    input_word = request.form['word']
    solutions = []
    for word in word_list:
        counter = 0
        if len(word) != len(input_word):
            continue
        else:
            for i in range(len(word)):
                if word[i].lower() == input_word[i].lower() or input_word[i] == '_':
                    counter += 1
                else:
                    break
        if counter == len(input_word):
            solutions.append(word)
    return render_template('index.html', solutions=solutions)


if __name__ == '__main__':
    app.run(debug=True)
