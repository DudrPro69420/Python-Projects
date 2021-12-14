board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]
player="X"
GameIsGoing = True
winner = None
gameTied = False

#View the board.
def displayBoard():
    print(board[0] + "|" + board[1] + "|" + board[2])
    print(board[3] + "|" + board[4] + "|" + board[5])
    print(board[6] + "|" + board[7] + "|" + board[8])


def playGame():
    global winner
    displayBoard()
    while GameIsGoing:
        drawMark(player)
        displayBoard()
        checkIfGameEnd()
        flipPlayer()

    #If game ended.
    '''if winner == "X" or winner == "O":
        print("{} won.".format(winner))'''


#Used to draw X or O mark in the board.
def drawMark(currentPlayer):
    try:
        position = int(input("Enter a number between 1 to 9: "))
        position = position - 1
    except Exception as e:
        print("Enter numbers only.")

    try:
        if board[position] == "-":
            board[position] = currentPlayer
        else:
            print("That position is already taken.")
    except Exception as e:
        print("The number was too big/small.")


#Used to flip player from X to O and vice versa.
def flipPlayer():
    global player
    if player=="X":
        player="O"
    else:
        player="X"


def displayWinner(gameWinner):
    if gameWinner == "X" or gameWinner == "O":
        print("{} won.".format(gameWinner))
        exit()
    


#Check if game ended.
def checkIfGameEnd():
    checkIfWin()
    checkIfTie()


def checkRows():
    global GameIsGoing
    global winner

    if board[0] == board[1] == board[2] != "-":
        GameIsGoing = False
        winner = board[0]
        displayWinner(winner)

    elif board[3] == board[4] == board[5] != "-":
        GameIsGoing = False
        winner = board[3]
        displayWinner(winner)

    elif board[6] == board[7] == board[8] != "-":
        GameIsGoing = False
        winner = board[6]
        displayWinner(winner)

    else:
        return None


def checkColumns():
    global winner
    global GameIsGoing

    if board[0] == board[3] == board[6] != "-":
        GameIsGoing = False
        winner = board[0]
        displayWinner(winner)

    elif board[1] == board[4] == board[7] != "-":
        GameIsGoing = False
        winner = board[1]
        displayWinner(winner)

    elif board[2] == board[5] == board[8] != "-":
        GameIsGoing = False
        winner = board[2]
        displayWinner(winner)

    else:
        return None

def checkDiagonals():
    if board[0] == board[4] == board[8] != "-":
        GameIsGoing = False
        winner = board[0]
        displayWinner(winner)
    
    elif board[2] == board[4] == board[6] != "-":
        GameIsGoing = False
        winner = board[2]
        displayWinner(winner)

    else:
        return None


#Check if someone won.
def checkIfWin():
    global winner
    #check rows
    winner = checkRows()

    #check column  
    winner = checkColumns()

    #check diagonals 
    winner = checkDiagonals()


#Check if game tied.
def checkIfTie():
    global gameTied
    tieCheck = board.count("-")
    if tieCheck == 0 and winner == None:
        print("The game tied.")
        exit()




playGame()
