def minimax(depth, node, maxplayer):
    if depth == 3:
        return tree[node]

    if maxplayer:
        best = -999
        for i in range(2):
            value = minimax(depth+1, node*2+i+1, False)
            best = max(best, value)
        return best

    else:
        best = 999
        for i in range(2):
            value = minimax(depth+1, node*2+i+1, True)
            best = min(best, value)
        return best


tree = [0]*7 + [3, 5, 6, 9, 1, 2, 0, -1]

print("Best value:", minimax(0, 0, True))