def queen(row):

    if row > 7:
        print('._._._._._._._._.')
        for i in range(8):
            for j in range(8):
                if(chessboard[i][j] == 1):
                    print('|' + '_|' * j + 'Q|' + '_|' * (7 - j))
        exit()
    for i in range(8):
        if test(row, i):
            chessboard[row][i] = 1
            queen(row + 1)
            chessboard[row][i] = 0

def test(row, column):

    for i in range(8):
        if chessboard[i][column] == 1:
            return False 
    for i in range(row):
        if column - 1 - i < 0:
            break
        if chessboard[row - 1 - i][column - 1 - i] == 1:
            return False
    for i in range(row):
        if column + 1 + i > 7:
            break
        if chessboard[row - 1 - i][column + 1 + i] == 1:
            return False
    return True

chessboard = [[0 for _ in range(8)] for _ in range(8)]
queen(0)