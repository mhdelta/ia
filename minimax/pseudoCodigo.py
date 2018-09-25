MAXDEPTH = 50 #EXAMPLE
int blueValue(board b, int depth):
    if Gameover(b) or depth > MaxDepth:
        return Analisis(b)
    int max == -infinity
    for each legal move m in board b :
        copy b to c
        make move m in board c
        int x = ReadValue(c, depth + 1)
        if x > max : max = x
    return max


int RedValue(board b, int depth):
    if GameOver(b) or depth > MAXDEPTH:
        return Analisis(b)
    int min = infinity
    for eeach legal move m in board b:
        copy b to c 
        make move in board c
        int x = BlueValue(c, Depth + 1)
        if x < min : min = x

    return min
