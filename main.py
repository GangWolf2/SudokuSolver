#7/19/20
#Wulfgang Rankenburg
#Based off of Tech From Tim Sudoku solution finder, different implementation
#Given a standard 9x9 Sudoku board, this program utilizes backtracking to find a valid solution
#To any solvable 9x9 sudoku board, otherwise it returns the original board if unsolvable

from solution import *
import time
def main():

    board = [
        #0,0    0,3     0,6
        [4,0,0,0,0,2,8,3,0],
        [0,8,0,1,0,4,0,0,2],
        [7,0,6,0,8,0,5,0,0],
        #3,0    3,3     3,6
        [1,0,0,0,0,7,0,5,0],
        [2,7,0,5,0,0,0,1,9],
        [0,3,0,9,4,0,2,0,6],
        #6,0    6,3    6,6
        [0,0,8,0,9,0,7,0,5],
        [3,0,0,8,0,6,0,9,0],
        [0,4,2,7,0,0,0,0,3]
    ]
    
    board2 = [
        [0,0,5,0,1,0,6,0,0],
        [3,9,0,7,0,0,0,1,0],
        [4,0,7,9,0,0,0,2,8],
        [9,7,0,8,0,0,0,4,0],
        [5,0,0,2,0,6,0,0,1],
        [0,8,0,0,0,1,0,7,3],
        [2,6,0,0,0,8,7,0,4],
        [0,5,0,0,0,7,0,3,9],
        [0,0,8,0,4,0,1,0,0]
    ]

    board3 = [
        [0,7,0,0,0,0,4,0,0],
        [0,0,0,4,0,0,5,0,3],
        [0,4,0,0,0,0,0,0,0],
        [0,2,0,0,0,3,0,0,4],
        [0,0,4,0,0,0,9,0,0],
        [0,0,0,0,5,0,0,6,0],
        [0,3,2,0,9,1,0,7,8],
        [6,8,0,0,0,2,1,0,0],
        [0,0,0,8,0,6,0,0,0]
    ]
    
    start_time = time.time()
    drawBoard(board)
    solve(board)
    drawBoard(board)
    print("Finished in --- %s seconds ---" % (time.time() - start_time))

main()
