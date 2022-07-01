# Solve a Sudoku Board

# Use backtracking algorithm
# 1. Pick an empty space
# 2. Try all numbers
# 3. See if it is valid sudoku board
# 4. Backtrack if invalid 
# Extra: see runtime speed

example_board = [
    [3, 9, 0,   0, 5, 0,   0, 0, 0],
    [0, 0, 0,   2, 0, 0,   0, 0, 5],
    [0, 0, 0,   7, 1, 9,   0, 8, 0],

    [0, 5, 0,   0, 6, 8,   0, 0, 0],
    [2, 0, 6,   0, 0, 3,   0, 0, 0],
    [0, 0, 0,   0, 0, 0,   0, 0, 4],

    [5, 0, 0,   0, 0, 0,   0, 0, 0],
    [6, 7, 0,   1, 0, 5,   0, 4, 0],
    [1, 0, 9,   0, 0, 0,   2, 0, 0]
]


def solve(board):
    empty_spot = pick_empty(board)
    if (not empty_spot):
        return True
    else:
        row, col = empty_spot
    
    for number in range(1,10):
        if (is_valid(board, number, empty_spot)):
            board[row][col] = number
            if solve(board):
                return True
            board[row][col] = 0
            
    return False


# Finds empty spot and returns the box location
def pick_empty(board):
    for row in range(len(board)):
        for col in range(len(board[0])):
            if (board[row][col] == 0):
                return (row, col)
    return None

    
# Checks if board is valid    
def is_valid(board, insert, position):
    row = position[0]
    col = position[1]
    
    # Check row
    for c in range(len(board[0])):
        if board[row][c] == insert and col != c:
            return False

    # Check column
    for r in range(len(board)):
        if board[r][col] == insert and row != r:
            return False

    # Check box
    box_x = col // 3
    box_y = row // 3

    for r in range(box_y*3, box_y*3 + 3):
        for c in range(box_x * 3, box_x*3 + 3):
            if board[r][c] == insert and (r,c) != position:
                return False

    return True


# Prints the sudoku board
def print_board(board):
    
    for row in range(len(board)):
        if (row % 3 == 0 and row != 0):
            print("- - - - - - - - - - - - - ")
            
        for col in range(len(board[0])):
            if (col % 3 == 0 and col != 0):
                print(" | ", end="")
            
            if col == 8:
                print(board[row][col])
            else:
                print(str(board[row][col]) + " ", end="")

solve(example_board)            
print_board(example_board)
