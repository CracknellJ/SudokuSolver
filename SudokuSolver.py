import os
from copy import copy
from copy import deepcopy
from itertools import product
from timeit import default_timer as timer

def Read_Puzzle():
    sudokuGrid = [] 
    with open("sudoku_puzzle.txt", "r") as f:
    #with open("sudoku_row_test.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            sudokuGrid.append([int(x) for x in line.split(" ")])
        return sudokuGrid

def Write_Solution_To_File(sudokuGrid):
    with open("sudoku_solution.txt", "w") as f:
    #with open("sudoku_row_solution.txt", "w") as f:
        for item in sudokuGrid:
            f.write("%s\n" % item)

def Find_Empty_Cell(sudokuGrid):
    for i in range(len(sudokuGrid)):
        for j in range(len(sudokuGrid[0])): #length of the row
            if sudokuGrid[i][j] == 0:
                return(i, j)
    #nothing found
    return False

def Is_Board_Valid(sudokuGrid, number, position):
    #check row
    for i in range(len(sudokuGrid[0])):
        if sudokuGrid[position[0]][i] == number and position[1] != i: #ignore the position we just inserted to
            return False
    #check column
    for i in range(len(sudokuGrid)):
        if sudokuGrid[i][position[1]] == number and position[0] != i: #ignore the position we just inserted to
            return False 
    #check 3x3 box
    #boxes range from 0,0 to 2,2 from top left to bottom right
    box_x = position[1] // 3
    box_y = position[0] // 3 

    #using box location and operations to find starting point of box
    #e.g (2,0) gives us top right box -> i in range(6,9) - columns
    #                                 -> j in range(0,3) - rows
    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if sudokuGrid[i][j] == number and (i,j) != position:
                #found duplicate
                return False  
    #valid grid
    return True
    
def Solve_Sudoku(sudokuGrid):
    emptyCell = Find_Empty_Cell(sudokuGrid)
    if not emptyCell:
        #if no cell can be found, we're done
        return True
    else:
        row, column = emptyCell
    
    for number in range(1,10):
        #roll each possible number into the empty cell
        if Is_Board_Valid(sudokuGrid, number, (row, column)):
            #if adding the number results into a valid board, add to the grid
            sudokuGrid[row][column] = number

            #call solve again to move onto the next empty cell
            if Solve_Sudoku(sudokuGrid):
                return True

            #if no numbers result in a valid board, Solve_Sudoku isnt true so we return false below
            #this line backtracks and empties the cell to try a different value
            sudokuGrid[row][column] = 0

    #see above comment
    return False


sudokuGrid = Read_Puzzle()

startTime = timer()
Solve_Sudoku(sudokuGrid)
endTime = timer()

timeElapsedMs = (endTime - startTime) * 1000 
Write_Solution_To_File(sudokuGrid)
print("Time elapsed in ms: %a" % timeElapsedMs  )

# #simple brute force solver

# #implement dancing links version, compare all 3

