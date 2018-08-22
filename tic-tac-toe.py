import numpy as np 


def win(game,player=1):
	x,y = game.shape
	diag = game.diagonal()
	diag2 = np.flip(game,0).diagonal()
	return all(map(lambda x:x==player,diag)) or all(map(lambda x:x==player,diag2)) or len(list(filter(lambda x:all(x),[map(lambda x:x==player,game[i]) for i in range(x)]))) == 1 or len(list(filter(lambda x:all(x),[map(lambda x:x==player,game[:,i]) for i in range(y)]))) == 1

def possible_move(game):
	x,y = np.where(game == 0)
	return zip(x,y)

def min_max(game,depth=9,player=1):
	if win(game,1):
		return 1
	elif win(game,-1):
		return -1
	elif depth==0:
		return 0
	else:
		score = -1*player*100000
		for x,y in possible_move(game):
			game2 = game.copy()
			game2[x][y] = player
			if player == 1: score = max(min_max(game2,depth-1,player=-1*player),score)
			else:  score = min(min_max(game2,depth-1,player=-1*player),score)
			del game2
		return score

def alpha_beta(game,depth=9,alpha=-100000,beta=100000,player=1):
	if win(game,1):
		return 1
	elif win(game,-1):
		return -1
	elif depth==0:
		return 0
	else:
		score = -1*player*100000
		for x,y in possible_move(game):
			game2 = game.copy()
			game2[x][y] = player
			if player == 1: 
				score = max(alpha_beta(game2,depth-1,alpha,beta,player=-1*player),score)
				alpha = max(score,alpha)
			else: 
				score = min(alpha_beta(game2,depth-1,alpha,beta,player=-1*player),score)
				beta = min(score,beta) 
			if alpha >= beta:
				break
			del game2
		return score 
		
# def action(game,player=1):
# 	scores = []
# 	for x,y in possible_move(game):
# 		game2 = game.copy()
# 		game2[x][y] = player
# 		score = min_max(game2,player=-player)
# 		scores.append(score)
# 		del game2
# 	return list(possible_move(game))[np.argmax(scores)]

def action(game,player=1):
	scores = []
	for x,y in possible_move(game):
		game2 = game.copy()
		game2[x][y] = player
		score = alpha_beta(game2,player=-player)
		scores.append(score)
		del game2
	return list(possible_move(game))[np.argmax(scores)]
game = np.array([[1,1,-1],[0,-1,0],[1,0,0]])
print(action(game,1))