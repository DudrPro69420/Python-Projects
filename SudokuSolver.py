gameBoard = [
    [9, 2, 0, 0, 0, 0, 5, 8, 4],
    [0, 0, 0, 5, 0, 0, 0, 0, 3],
    [0, 8, 3, 0, 9, 2, 0, 0, 0],
    [2, 6, 0, 8, 5, 4, 0, 0, 1],
    [0, 0, 5, 3, 6, 1, 0, 9, 0],
    [1, 0, 0, 0, 0, 9, 0, 0, 0],
    [8, 5, 0, 2, 0, 3, 0, 1, 0],
    [4, 1, 2, 9, 8, 0, 0, 3, 0],
    [3, 9, 0, 0, 0, 6, 8, 0, 0]
    ]


def printBoard(board):
    for i in range(len(board)):
        #This will make horizontal lines and won't make lines on the top.
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - ")

        for j in range(len(board[i])):
            #This will make vertical lines and won't make lines on the left.
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")
    
        
def findEmptySquares(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return i,j #row, col
    return None
    
    
def findValidNumber(board, number, position):
    #check rows
    for i in range(len(board[0])):
        if board[position[0]][i] == number and i != position[0]:
            return False
            
    #check column
    for i in range(len(board)):
        if board[i][position[1]] == number and i != position[1]:
            return False
            
    #check boxes
    boxRow = position[0] // 3
    boxColumn = position[1] // 3
    
    for i in range(boxRow*3, boxRow*3 + 3):
        for j in range(boxColumn*3, boxColumn*3 + 3):
            if board[i][j] == number and (i,j) != position:
                return False
    return True
    
    
def solve(board):
    find = findEmptySquares(board)
    if not find:
        return True
    else:
        row, col = find
        
    for i in range(1,10):
        if findValidNumber(board, i, (row,col)):
            board[row][col] = i
            
            if solve(board):
                return True
            else:
                board[row][col] = 0
    return False
    
printBoard(gameBoard)
solve(gameBoard)
print("")
print("Solving the puzzle...")
print("")
printBoard(gameBoard)
