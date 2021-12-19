import random 
from words import wordList

guessed = False
fakeWord = []
tries = 6
wordLocations = []

#this will return a word from word.py
def getWord():
    word = random.choice(wordList)
    if len(word)>8:
        getWord()

    return word.upper()


def play(word):
    global guessed
    global fakeWord
    global tries
    global wordLocations

    for i in range(len(word)):
        fakeWord.append("_")

    gussedLetters = [word[0], word[-1]]

    print("Starting hangman!")
    print(displayHangman(tries))
    print("Guess the word!")

    fakeWord[0] = word[0]
    fakeWord[-1] = word[-1]
    
    for i in range(len(fakeWord)):
        print(fakeWord[i], end = "")
    print("")

    while not guessed and tries > 0:
        guess = input("Guess a letter: ").upper()
        howMany = word.count(guess)

        if len(guess)>1:
            print("please enter only 1 letter.")

        elif guess in gussedLetters and howMany <= 1:
            print("You've already used that letter.")
            
        elif guess not in word:
            print("This letter is not in the word.")
            gussedLetters.append(guess)
            tries = tries - 1 
            print(displayHangman(tries))

        else:
            print("You've correctly guessed one letter. Nicr")
            gussedLetters.append(guess)
            tries = tries - 1

            print(displayHangman(tries))

            whereWord = word.find(guess)

            if whereWord in wordLocations:
                newWordLocation = findTheWord(whereWord, guess, word)
                wordLocations.append(newWordLocation)
                editWordLocation = newWordLocation

            else:
                editWordLocation = whereWord
                wordLocations.append(whereWord)

            if editWordLocation == None:
                print("You've already guessed that letter")
            else:
                fakeWord[editWordLocation] = guess
                for i in range(len(fakeWord)):
                    print(fakeWord[i], end = "")
                print("")

        if "_" not in fakeWord:
            guessed = True
            displayResult(guessed, word)

        if tries == 0:
            displayResult(False, word)

def findTheWord(whereWord, guess, word):
    global wordLocations

    whereNextWord = word.find(guess, whereWord+1)

    if whereNextWord in wordLocations:
        findTheWord(whereNextWord, guess, word)
    
    return whereNextWord


def displayResult(winOrLose, word):
    if winOrLose:
        print("You won!")
        exit()
    else:
        print("You lost")
        print("The correct word was {}".format(word))
        exit()


def displayHangman(tries):
    stages = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # initial empty state
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[tries]

play(getWord())
