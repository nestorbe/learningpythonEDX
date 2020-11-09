# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string
import os

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()
#secretWord = chooseWord(wordlist)
secretWord = input("Please type the secret word: ")
os.system('cls' if os.name == 'nt' else 'clear')

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    listCheck = []
    list_of_word = list(secretWord)

    for letter in list_of_word:
        if letter in lettersGuessed:
            listCheck.append(letter)

    listCheck.sort()
    list_of_word.sort()

    if listCheck == list_of_word:
        return True
    else:
        return False


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    string_return = ""
    list_of_word = list(secretWord)

    for letter in list_of_word:
        if letter in lettersGuessed:
            string_return += letter + " "
        else:
            string_return += "_ "

    return string_return



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    available_list = list(string.ascii_lowercase)
    available_letters = ""

    for letter in lettersGuessed:
        if letter in available_list:
            available_list.remove(letter)

    for letter in available_list:
        available_letters += letter

    return available_letters
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    available_letters = string.ascii_lowercase
    guesses = 8
    list_of_secretWord = list(secretWord)
    lettersGuessed = []

    def welcome_message(secretWord):

        print("Welcome to the game Hangman!")
        print("I am thinking of a word that is " + str(len(secretWord)) + " letters long.")

    welcome_message(secretWord)

    while isWordGuessed(secretWord, lettersGuessed) == False and guesses > 0:

        print("--------------------------------")
        print("You have " + str(guesses) + " guesses left.")
        print("Available letters: " + available_letters)
        letter_guessed = input("Please guess a letter: ")
        letter_guessed_lc = letter_guessed.lower()

        if len(letter_guessed_lc) > 1:
            print("You can only try one letter at a time!")
            continue

        if letter_guessed_lc in getGuessedWord(secretWord, lettersGuessed):
            print("Oops! You've already guessed that letter: " + getGuessedWord(secretWord,lettersGuessed))
            continue

        if letter_guessed_lc in lettersGuessed:
            print("Oops! You've already guessed that letter: " + getGuessedWord(secretWord, lettersGuessed))
            continue

        lettersGuessed.append(letter_guessed_lc)
        available_letters = getAvailableLetters(lettersGuessed)

        if letter_guessed_lc in list_of_secretWord:
            print("Good Guess: " + getGuessedWord(secretWord, lettersGuessed))

        else:
            print("Oops! That letter is not in my word: " + getGuessedWord(secretWord, lettersGuessed))
            guesses -= 1


        if isWordGuessed(secretWord, lettersGuessed) == True:
            print("--------------")
            print("Congratulations you won!")

        elif guesses == 0:
            print("--------------")
            print("Sorry, you ran out of guesses. The word was: " + secretWord + ".")

        else:
            continue






# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

#secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
