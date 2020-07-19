#dictionary that holds all the numbers used in each box. Populated for visual purposes in branch GangWolf2-first-solver
#Each key is the top left corner of each box in a standard 9x9 Sudoku board
    (0, 0): [],
    (0, 3): [],
    (0, 6): [],
    (3, 0): [],
    (3, 3): [],
    (3, 6): [],
    (6, 0): [],
    (6, 3): [],
    (6, 6): []
}
#initializes the usedNums dictionary with the default values found in each box, row, column
#row = len(board), col = len(board), board = N x N array of arrays.
#Assumes that board is of standard size 9 x 9, otherwise will not work
#Could possibly be used to populate values for all rows and columns, but I fear KeyErrors with repeating values for boxes and rows
def initDict(board):
    for i in range(0, 9):
        for j in range(0, 9):
            if board[i][j] != 0:
                #finds the closest top left corner of the current box
                #top left corner of every box is consistent point every other cell in box can reach
                k = i - (i % 3)
                l = j - (j % 3)

                #since each value of key is array, we can use built-in array methods to update dict value
                usedNums[(k, l)].append(board[i][j])

    #calls solver method when finished
    solve(board)

#finds the working solution for each empty cell, utilizing backtracking
#board = array of arrays found in main.py
def solve(board):

    #holds the most-recently occuring empty cell in board
    curSquare = findEmpty(board)

    #if there are no empty spaces left, solve has found solution to the board
    if not curSquare:
        print("\nThe board has been solved")
        return True

    #findEmpty(board) returns a tuple of ints, which are assigned here as row and column values
    else:
        row, col = curSquare

    #tests values 1-9 in each box for a valid solution
    for i in range(1,10):

        #print("\nCurrent value of i: " + str(i))
        #print("Currently at position: " + str((row,col)))

        #sets cell to the i value currently valid at this position
        if checkRowCol(board, (row,col), i):
            board[row][col] = i
            #since board has not been completed, will call solve again to find the solution for the next empty cell
            #This instance of solve has not yet completed, as the number chosen may need to change in the future
            #everytime a valid number is picked using solve, it must wait for its recursive call of solve to resolve
            #before it can return True (number chosen is the correct one and valid for the position)
            if solve(board):
                return True
            #if solution is not found, resets the value of the cell to 0
            #Removes previous value that was added into the dictionary at the selected box coordinate
            board[row][col] = 0
            r = row - (row % 3)
            c = col - (col % 3)
            usedNums[(r,c)].remove(i)

    return False

#Searches for next empty cell in the Sudoku board
#board = array of arrays in main.py
#Assumes that board is of standard size 9 x 9, otherwise will not work
def findEmpty(board): 
    for i in range(0,9):
        for j in range (0,9):
            if board[i][j] == 0:
                #print("Empty space found at (" + str(i) + "," + str(j) + ")")
                return (i,j) #returns the row, column values where empty space found
    #if there are no empty spaces, return None
    return None

#draws Sudoku board in console for visualization purposes
def drawBoard(board):
    for i in range(0,9):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(0,9):
            if j % 3 == 0 and j != 0:
                print("|", end="")
            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")

#checks the row and column of the current empty space to determine if a selected solution is valid
#board = array of array in main, cell (row,col) tuple from findEmpty, numChosen = i from findEmpty
def checkRowCol(board, cell, numChosen):
    #checks row if numChosen equal to any row values
    for i in range(0,9):
        if board[cell[0]][i] == numChosen:
            #print("ILLEGAL: Same number in row")
            return False
    #checks column of current cell to see if numChosen = any current values in the column
    for j in range(0,9):
        if board[j][cell[1]] == numChosen:
            #print("ILLEGAL: Same number in column")
            return False

    #checks box to make sure number has not already been chosen
    #finds the closest top left corner to the current box so it can check against keys in dictionary above
    row = cell[0] - (cell[0] % 3)
    col = cell[1] - (cell[1] % 3)

    #checks if chosen number is in list of values mapped to current box and returns False if found
    if numChosen in usedNums[(row, col)]:
        #print("ILLEGAL: Same number in box")
        return False
    #if the chosen number is not found in the list of values, then it is appended to the value list and returns True
    usedNums[(row, col)].append(numChosen)
    return True




