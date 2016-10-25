#Game Board Format - N x N grid
#Columns - A, B, C, ...
#rows - 1, 2, 3, ...



def makeCellValues(N, cell_value, row_number):
	each_row = cell_value.split(' ')
	column_number = 0
	for i in range(N):
		column_number += 1
		if row_number not in game_board_cell_values:
			game_board_cell_values[row_number] = {}
		(game_board_cell_values[row_number])[column_number] = each_row[i]
	return game_board_cell_values

def makeBoardState(N, board_state, row_number):
	#each_row = board_state.split(' ')
	column_number = 0
	for i in range(N):
		column_number += 1
		if row_number not in game_board_state:
			game_board_state[row_number] = {}
		(game_board_state[row_number])[column_number] = board_state[i]
	return game_board_state

def read_input():
	input_file = open("G:\Documents\USC\Artificial Intelligence\Homework\Homework 2\Input\input0.txt","r")
	line_number = -1
	row_number = 0
	for each_line in input_file:
		line_number += 1

		if line_number<4:
			if line_number == 0:
				N = int(each_line.rstrip('\n'))
			elif line_number == 1:
				mode = str(each_line.rstrip('\n'))
			elif line_number == 2:
				you_play = str(each_line.rstrip('\n'))
				#print you_play
				if you_play == 'X':
					player = 'X'
					opponent = 'O'
				else:
					player = 'O'
					opponent = 'X'
			else:
				depth = int(each_line.rstrip('\n'))
				#print depth
		elif line_number < 4 + N:
			row_number += 1
			cell_value = each_line.rstrip('\n')
			game_board_cell_values = makeCellValues(N, cell_value, row_number)
		else:
			#print row_number
			if row_number == N:
				row_number = 0
			row_number += 1
			board_state = each_line.rstrip('\n')
			game_board_state = makeBoardState(N, board_state, row_number)
	return N, player, opponent

def calculateScores(N, player, opponent, player_score, opponent_score):
	for i in range(1, N+1):
		for j in range(1, N+1):
			if game_board_state[i][j] == player:
				player_score += int(game_board_cell_values[i][j])
			elif game_board_state[i][j] == opponent:
				opponent_score += int(game_board_cell_values[i][j])

	return player_score, opponent_score

#def actions(game_board_state, game_board_cell_values):

def actions(current_game_board_state, N, current_player):
	for i in range(1, N+1):
		for j in range(1, N+1):
			if current_game_board_state[i][j] == '.':
				#action = "Stake"
				#best_score_dictionary = dict()
				best_action = -10000
				raid_possibility = false
				if i > 1:
					if current_game_board_state[i-1][j] == opponent:
						raid_possibility = true
						current_game_board_state[i][j] = current_player
						current_game_board_state[i-1][j] = current_player

						best_score = minimax(N, current_game_board_state, 0, current_player)
						current_game_board_state = game_board_state

						if(best_score > best_action){
							best_action = best_score
							next_move = "".join(str("R")+i+j)
						}

				if i < N:
					if current_game_board_state[i+1][j] == opponent:
						raid_possibility = true
						current_game_board_state[i][j] = current_player
						current_game_board_state[i+1][j] = current_player

						best_score = minimax(N, current_game_board_state, 0, current_player)
						current_game_board_state = game_board_state

						if(best_score > best_action){
							best_action = best_score
							next_move = "".join(str("R")+i+j)
						}

				if j > 1:
					if current_game_board_state[i][j-1] == opponent:
						raid_possibility = true
						current_game_board_state[i][j] = current_player
						current_game_board_state[i][j-1] = current_player

						best_score = minimax(N, current_game_board_state, 0, current_player)
						current_game_board_state = game_board_state

						if(best_score > best_action){
							best_action = best_score
							next_move = "".join(str("R")+i+j)
						}

				if j < N:
					if current_game_board_state[i][j+1] == opponent:
						raid_possibility = true
						current_game_board_state[i][j] = current_player
						current_game_board_state[i][j+1] = current_player

						best_score = minimax(N, current_game_board_state, 0, current_player)
						current_game_board_state = game_board_state	

						if(best_score > best_action){
							best_action = best_score
							next_move = "".join(str("R")+i+j)
						}

				
				current_game_board_state[i][j] = current_player

				best_score = minimax(N, current_game_board_state, 0, current_player)
						
				current_game_board_state = game_board_state
				if(best_score > best_action){
					best_action = best_score
					next_move = "".join(str("S")+i+j)
				}





	return best_action, next_move

def terminalTest(current_game_board_state, N):
	for i in range(1, N+1):
		for j in range(1, N+1):
			if current_game_board_state[i][j] == '.':
				return false
	return true
def minimax(N, current_game_board_state, d, current_player):
	if terminalTest(current_game_board_state, N) or d > depth:
		return calculateScores(N, player, opponent, 0, 0)
	if current_player == player:
		v = -10000
		for i in range(1, N+1):
			for j in range(1, N+1):
				if current_game_board_state[i][j] == '.':
					if i > 1:
						if current_game_board_state[i-1][j] == opponent:
							current_game_board_state[i][j] = current_player
							current_game_board_state[i-1][j] = current_player

							v = max(v, minimax(N, current_game_board_state, d+1, opponent))
							current_game_board_state = game_board_state


					if i < N:
						if current_game_board_state[i+1][j] == opponent:
							current_game_board_state[i][j] = current_player
							current_game_board_state[i+1][j] = current_player

							best_score = minimax(N, current_game_board_state, 0, current_player)
							current_game_board_state = game_board_state

						

				if j > 1:
					if current_game_board_state[i][j-1] == opponent:
						raid_possibility = true
						current_game_board_state[i][j] = current_player
						current_game_board_state[i][j-1] = current_player

						best_score = minimax(N, current_game_board_state, 0, current_player)
						current_game_board_state = game_board_state

						if(best_score > best_action){
							best_action = best_score
							next_move = "".join(str("R")+i+j)
						}

				if j < N:
					if current_game_board_state[i][j+1] == opponent:
						raid_possibility = true
						current_game_board_state[i][j] = current_player
						current_game_board_state[i][j+1] = current_player

						best_score = minimax(N, current_game_board_state, 0, current_player)
						current_game_board_state = game_board_state	

						if(best_score > best_action){
							best_action = best_score
							next_move = "".join(str("R")+i+j)
						}

				
				current_game_board_state[i][j] = current_player

				best_score = minimax(N, current_game_board_state, 0, current_player)
						
				current_game_board_state = game_board_state
				if(best_score > best_action){
					best_action = best_score
					next_move = "".join(str("S")+i+j)
				}

	
# Dictionary Data Structure Format - Eg. {'1': {'A' : 4, 'B' : 8}}
game_board_cell_values = dict()
game_board_state = dict()			

N, player, opponent = read_input()
print game_board_cell_values
print game_board_state

#print ord('A')
game_board_stake = dict()

player_score = 0
opponent_score = 0
current_game_board_state = game_board_state
player_score, opponent_score = calculateScores(N, player, opponent, player_score, opponent_score)
#available_moves = getAvailableMoves(current_game_board_state, game_board_cell_values)

print available_moves
print player_score

