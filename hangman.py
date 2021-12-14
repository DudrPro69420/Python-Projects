import random 
from words import wordList

#it requires words.py file.

def getWord():
    word = random.choice(wordList)
    return word.upper()


def play(word):
    fakeWord = []
    for i in range(len(word)):
        fakeWord.append("_")

    guessed = False
    gussedLetters = [word[0], word[-1]]
    tries = 6
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

        elif guess in gussedLetters and howMany > 1:
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
            fakeWord[whereWord] = guess
            for i in range(len(fakeWord)):
                print(fakeWord[i], end = "")
            print("")

        if "_" not in fakeWord:
            guess = True
            displayResult(guess, word)

        if tries == 0:
            displayResult(False, word)


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
