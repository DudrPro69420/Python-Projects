empty = 0
mine = 10 #💣
unknown = -1
flag = -2
score = 0
gameGoingOn = True
mines = []
unknowns = []

grid = [
    [0,0,0,10,0,0,0,10,0],
    [0,10,0,0,0,0,10,0,0],
    [0,0,0,0,0,10,0,0,0],
    [0,0,0,10,0,0,0,10,0],
    [0,10,0,0,0,0,0,0,0],
    [0,0,0,0,0,10,0,0,0],
    [0,0,0,10,0,0,0,0,10],
    [0,10,0,0,0,0,0,0,0],
    [10,0,0,0,0,0,0,10,0]
]

playerGrid=[
    [-1,-1,-1,-1,-1,-1,-1,-1,-1],
    [-1,-1,-1,-1,-1,-1,-1,-1,-1],
    [-1,-1,-1,-1,-1,-1,-1,-1,-1],
    [-1,-1,-1,-1,-1,-1,-1,-1,-1],
    [-1,-1,-1,-1,-1,-1,-1,-1,-1],
    [-1,-1,-1,-1,-1,-1,-1,-1,-1],
    [-1,-1,-1,-1,-1,-1,-1,-1,-1],
    [-1,-1,-1,-1,-1,-1,-1,-1,-1],
    [-1,-1,-1,-1,-1,-1,-1,-1,-1]
]
 
#Counts for all the mines adjacent to the cell.
def countMines(row, column):
    checkHere = ((-1,-1), (0,-1), (1,-1), (-1, 0), (1, 0), (-1,1), (0,1), (1,1))
    count = 0
    for offset in checkHere:
        offsetRow = row + offset[0]
        offsetCol = column + offset[1]
        if offsetRow >= 0 and offsetRow <= 8 and offsetCol >= 0 and offsetCol <= 8:
            if grid[offsetRow][offsetCol] == mine:
                count = count + 1
    return count

#removes a flag
def removeFlag(row, column):
    if playerGrid[row][column] == flag:
        playerGrid[row][column] = unknown
    else:
        print("That spot is not flagged.")

#Sets a flag.
def setFlag(row, column):
    if playerGrid[row][column] == unknown:
        playerGrid[row][column] = flag

#Checks for all the mines location and appends them in the mines list.
def mineLocation():
    global mines
    for row in range(len(grid)):
        for column in range(len(grid[row])):
            if grid[row][column] == mine:
                mines.append([row,column])
    

#Checks for all the unknown locations and appends them in the unknowns list.
def unknownLocations():
    global unknowns
    for row in range(len(playerGrid)):
        for column in range(len(playerGrid[row])):
            if playerGrid[row][column] == unknown:
                unknowns.append([row,column])

def click(row,column):
    global gameGoingOn
    global score
    global unknowns 

    #Checks if the spot is a mine or not.
    if grid[row][column] == mine and playerGrid[row][column] != flag:
        print("Boom you dead Nice.")
        gameGoingOn = False
        printBoard(grid)
    
    #checks if the spot is flagged and asks for unflagging it. 
    elif playerGrid[row][column] == flag:
        check=input("That spot is flagged, do you want to unflag that spot? Type Y or N: ")
        if check == "y":
            removeFlag(row,column)
        elif check.lower() == "n":
            print("Ok, not unflagging it.")
        else:
            print("Invalid input, not unflagging the spot.")


    #Checks if the spot is unknown
    elif playerGrid[row][column] == unknown:
        #counts for the number of mines near it
        playerGrid[row][column] = countMines(row,column)

        cells = [(row,column)]
        #checks in these cordinates respective to the cell.
        checkHere = ((-1,-1), (0,-1), (1,-1), (-1, 0), (1, 0), (-1,1), (0,1), (1,1))
        
        while len(cells)>0:
            cell = cells.pop()
            score = score + int(countMines(row,column))

            for offset in checkHere:
                offsetRow =  offset[0] + cell[0]
                offsetCol = offset[1] + cell[1]

                #checks if the rows are in range of the board or not.
                if (offsetRow >= 0 and offsetRow <=8) and (offsetCol >= 0 and offsetCol <=8 ):
                    
                    #Checks if the offset row and cols are unknown and empty and then put the score their by counting the number of mines adjacent to the block.
                    if (playerGrid[offsetRow][offsetCol] == unknown) and (grid[offsetRow][offsetCol] == empty):

                        playerGrid[offsetRow][offsetCol] = countMines(offsetRow,offsetCol)
                        score = score + int(countMines(offsetRow, offsetCol))
                
                        #Checks if the offset rows and cols are in cells (ie if they've been checked or not) if they've been checked then the code moves on else it checks them.
                        if countMines(offsetRow,offsetCol) == empty and (offsetRow,offsetCol) not in cells:
                            cells.append((offsetRow,offsetCol))
                        else:
                            playerGrid[offsetRow][offsetCol] = countMines(offsetRow, offsetCol)

                        unknowns.clear()
                        unknownLocations()
                        
                        #checks if the game is over.
                        if mines == unknowns:
                            print("Nicr you won the game.")
                            gameGoingOn = False
                            printBoard(playerGrid)


def printBoard(board):
    symbols = {-2: "F", -1: ".", 10: "💣"}
    for row in range(len(board)):
        for column in range(len(board[row])):
            value = board[row][column]
            if value in symbols:
                symbol = symbols[value]
            else:
                symbol = value
            print(symbol, end=" ")
        print(" ")

def playGame():
    print("Welcome to MineSweeper, this is the board")
    print(" ")
    mineLocation()
    while gameGoingOn:
        printBoard(playerGrid)
        print(" ")
        check=input(("Do you want to set a flag or click or unflag, reply with F or C or U: "))
        try:
            row = int(input("Enter the row: "))
            column = int(input("Enter the column: "))
        
            if check.lower() == "f":
                setFlag(row,column)
            elif check.lower() == "c":
                click(row,column)
            elif check.lower() == "u":
                removeFlag(row,column)
            else:
                print("Invalid input to, please enter the values as either F or C.")
        except Exception as e:
            print("Invalid input, enter numbers only for row and column.")
        
        print(" ")
    
    print("Thanks for playing the game, your score was {}".format(score))
        
playGame()
