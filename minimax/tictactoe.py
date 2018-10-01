game = []
player = 'x'
oponent = 'o'

def gameWon(board, player):
    if board[0][y] == board[1][y] == board [2][y] == player:
        return True
    if board[x][0] == board[x][1] == board [x][2] == player:
        return True
    if x == y and board[0][0] == board[1][1] == board [2][2] == player:
        return True
    if x + y == 2 and board[0][2] == board[1][1] == board [2][0] == player:
        return True
    return False   

def score(game):
    if gameWon(game, player):
        return 10
    elif not gameWon(game, oponent):
        return -10
    else:
        return 0

def getEmpySpaces(game):
    emptySpaces = []
    for i in range(3):
        for j in range(3):
            if game[i][j] == '':
                emptySpaces.append([i,j])
    return emptySpaces

    
def minimax(game):
    if getEmpySpaces(game) == []:
        return score(game)
    scores = [] # an array of scores
    moves = []  # an array of moves

    # Populate the scores array, recursing as needed
    game.get_available_moves.each do |move|
        possible_game = game.get_new_state(move)
        scores.push minimax(possible_game)
        moves.push move
    end

    # Do the min or the max calculation
    if game.active_turn == @player
        # This is the max calculation
        max_score_index = scores.each_with_index.max[1]
        @choice = moves[max_score_index]
        return scores[max_score_index]
    else
        # This is the min calculation
        min_score_index = scores.each_with_index.min[1]
        @choice = moves[min_score_index]
        return scores[min_score_index]
    end
end