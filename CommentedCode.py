# Import necessary libraries
import nltk

# Uncomment the line below to download the 'words' resource
# nltk.download('words')

from flask import Flask, render_template, request
from nltk.corpus import words as nltk_words

# Create a Flask application with a static URL path
app = Flask(__name__, static_url_path='/static')

# Define the home route
@app.route('/')
def index():
    return render_template('index.html')

# Define the find_words route for handling word search
@app.route('/find_words', methods=['POST'])
def find_words():
    # Load the words from NLTK
    word_list = nltk_words.words()
    
    # Get the input word from the form
    input_word = request.form['word']
    
    # Initialize an empty list to store solutions
    solutions = []
    
    # Iterate over each word in the word list
    for word in word_list:
        counter = 0
        
        # Check if the length of the word matches the input word
        if len(word) != len(input_word):
            continue
        else:
            # Compare each character in the word and input_word
            for i in range(len(word)):
                if word[i] == input_word[i] or input_word[i] == '_':
                    counter += 1
                else:
                    break
        
        # If the counter matches the length of the input word, add it to solutions
        if counter == len(input_word):
            solutions.append(word)
    
    # Render the template with the solutions
    return render_template('index.html', solutions=solutions)

# Run the Flask application in debug mode
if __name__ == '__main__':
    app.run(debug=True)
