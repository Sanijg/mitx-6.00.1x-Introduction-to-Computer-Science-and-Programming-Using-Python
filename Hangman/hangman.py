from getGuessedWord import *
from isWordGuessed import *
from getAvailableLetters import *
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
    # FILL IN YOUR CODE HERE...
    print("Welcome to the game, Hangman!\nI am thinking of a word that is", len(secretWord), "letters long.")
    attempt=8
    lettersGuessed=[]
    
    while attempt>0:
        print("------------------")
        print("You have", attempt," guesses left")
        print("Available letters:",getAvailableLetters(lettersGuessed))
        guess= str(input("please guess a letter: "))
        guess= guess.lower()
        if guess in lettersGuessed:
            print("Oops! You've already guessed that letter:", getGuessedWord(secretWord,lettersGuessed))
            continue
        else:
            lettersGuessed.append(guess)
        if guess in secretWord:
            print("Good guess:", getGuessedWord(secretWord,lettersGuessed))
        else:
            attempt-=1
            print("Oops! That letter is not in my word:", getGuessedWord(secretWord,lettersGuessed))
        if isWordGuessed(secretWord, lettersGuessed):
            print("----------------")
            print("Congratulations, You won!")
            break
    if attempt==0:
      print("--------------------")
      print("Sorry, you ran out of guesses. The word was ",secretWord)
hangman("csea")