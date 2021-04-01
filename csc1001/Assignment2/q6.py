# Place the queen row by row
def queen(row):
    # Generate one valid chessboard
    if row > 7:
        print('._._._._._._._._.')
        for i in range(8):
            for j in range(8):
                if(chessboard[i][j] == 1):
                    print('|' + '_|' * j + 'Q|' + '_|' * (7 - j))
        exit()
    # Use the recursion of queen() function to find the no text valid queen postion
    # If there is no valid place, the function will return the upper one and clear last statement
    # Then test the next position of the queen
    for i in range(8):
        if test(row, i):
            chessboard[row][i] = 1
            queen(row + 1)
            chessboard[row][i] = 0

# Check the four directions of the queen
def test(row, column):
    # Test row
    for i in range(8):
        if chessboard[i][column] == 1:
            return False 
    # Test column
    for i in range(row):
        if column - 1 - i < 0:
            break
        if chessboard[row - 1 - i][column - 1 - i] == 1:
            return False
    # Test the two diagonals
    for i in range(row):
        if column + 1 + i > 7:
            break
        if chessboard[row - 1 - i][column + 1 + i] == 1:
            return False
    return True
# Generate an empty chessboard
chessboard = [[0 for _ in range(8)] for _ in range(8)]
queen(0)