def alphabeta(depth, node, alpha, beta, maxplayer):
    if depth == 3:
        return tree[node]

    if maxplayer:
        best = -999
        for i in range(2):
            value = alphabeta(depth+1, node*2+i+1,
                              alpha, beta, False)
            best = max(best, value)
            alpha = max(alpha, best)
            if alpha >= beta:
                break
        return best

    else:
        best = 999
        for i in range(2):
            value = alphabeta(depth+1, node*2+i+1,
                              alpha, beta, True)
            best = min(best, value)
            beta = min(beta, best)
            if alpha >= beta:
                break
        return best


tree = [0]*7 + [3, 5, 6, 9, 1, 2, 0, -1]

print("Best value:",
      alphabeta(0, 0, -999, 999, True))