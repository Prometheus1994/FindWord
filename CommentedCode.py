# Import the nltk library
import nltk

# Download the required data (uncomment the line below and run it in your local environment if needed)
# nltk.download()

# Import the word list from the nltk corpus
from nltk.corpus import words as nltk_words

# Get the list of words from nltk
word_list = nltk_words.words()

# Define the input word with missing letters represented by underscores
input_word = "ba_a_a"

# Initialize an empty list to store solutions
solutions = []

# Iterate through each word in the word list
for word in word_list:
    # Initialize a counter to keep track of matching characters
    counter = 0
    
    # Check if the word's length matches the input word's length
    if len(word) != len(input_word):
        continue  # Skip to the next word if the lengths do not match
    else:
        # Iterate through each character in the word and input word
        for i in range(len(word)):
            if word[i] == input_word[i] or input_word[i] == '_':
                counter += 1
            else:
                break  # Break the loop if a character doesn't match or is not a placeholder
    
    # If the counter equals the length of the input word, all characters match
    if counter == len(input_word):
        solutions.append(word)  # Add the word to the list of solutions

# Print the list of solutions
print(solutions)
