#7/19/20
#Wulfgang Rankenburg
#Based off of Tech From Tim Sudoku soultion finder, different implementation
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
    
    start_time = time.time()
    drawBoard(board)
    solve(board)
    drawBoard(board)
    print("Finished in --- %s seconds ---" % (time.time() - start_time))

main()
