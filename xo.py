import random
# init the board
board = []
for i in range(3):
	board.append(['-']*3)

def show_board():
	# Show board
	for bar in board:
		print " ".join(bar)


def user_enter():
	# User input a point
	user_x = int(raw_input("Enter x :"))
	user_y = int(raw_input("Enter y :"))
	return [user_x-1,user_y-1]

def com_enter():
	# Computer input a point
	com_x = random.randint(0,2)
	com_y = random.randint(0,2)
	return [com_x,com_y]

def play_game():
	# Main function to play tic tac toe
	check_victory = 0	
	while (check_victory == 0):
		# User turn
		user = []
		while(user == []):
			user = user_enter()
			if board[user[0]][user[1]] == '-':
				board[user[0]][user[1]] = 'X'
			else:
				print "com: you can't mark."
				user = []
				continue
			if CheckVictory(board,user[0],user[1]) == True:
				check_victory = 1
			if check_victory == 1: break

		# Com turn
		com = []
		while(com == []):
			com = com_enter()
			if board[com[0]][com[1]] == '-':
				board[com[0]][com[1]] = 'O'
			else:
				com = []
				continue
			if CheckVictory(board,com[0],com[1]) == True:
				check_victory = 2
				break
			if check_victory == 2: break
		show_board()

	# End game	
	print "---------"
	if check_victory == 1 :
		print "USER WIN !"
	if check_victory == 2 :
		print "COM WIN !"
	print "---------"

def CheckVictory(board, x, y):
	# Check Victory Algorithm by someone in Stackoverflow
  if board[0][y] == board[1][y] == board [2][y] == ( "X" or "O" ):
    # print "Win vertical"
    return True
  
  if board[x][0] == board[x][1] == board [x][2] == ( "X" or "O" ):
    # print "Win horizontal"
    return True

  if x == y and board[0][0] == board[1][1] == board [2][2] == ( "X" or "O" ):
    # print "Win left"
    return True

  if x + y == 2 and board[0][2] == board[1][1] == board [2][0] == ( "X" or "O" ):
    # print "Win right"
    return True
  
  return False

# call function zone 
# - show board
show_board()
# - play game
play_game()
