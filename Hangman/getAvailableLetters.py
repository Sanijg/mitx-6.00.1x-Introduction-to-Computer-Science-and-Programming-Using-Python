def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    b=""
    temp="abcdefghijklmnopqrstuvwxyz"
    for char in lettersGuessed:
       if char in temp:
            for i in temp:
                if i!=char:
                    b+=i
       temp=b
       b=""
    return temp