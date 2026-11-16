def solve(row):
    if row == 8:
        print(board)
        return True

    for col in range(8):
        safe = True
        for r in range(row):
            if board[r] == col or abs(board[r]-col) == row-r:
                safe = False
                break

        if safe:
            board[row] = col
            if solve(row+1):
                return True
            board[row] = -1

    return False


board = [-1] * 8
solve(0)