import getpass as gt


def rules_and_control():
	print("""Welcome to Tic Tac Toe!
The rules are simple, get 3 in a row with your piece to win.
Use the coordinate system to place your piece.
Good luck and have fun!
""")

rules_and_control()


def board(p_two_y = 0, p_two_x = 0, p_one_x = 0, p_one_y = 0, just_display = False):
	board = []

	for i in range(3):
		board.append(["[ ]"] * 3)

		
	player_X = '[X]'
	player_O = '[O]'

	if not just_display:
		board[p_one_x][p_one_y] = player_X 
		board[p_two_x][p_two_y] = player_O

	print('   0  1  2')
	for count, row in enumerate(board):
		print(count, "".join(row))

board(just_display = True)


def game():
	p_one_x = gt.getpass('In which column would you like to put your piece P1? ')
	p_one_y = gt.getpass('In which row would you like to put your piece P1? ')
	p_two_x = gt.getpass('In which column would you like to put your piece P2? ')
	p_two_y = gt.getpass('In which row would you like to put your piece P2? ')
	board()

game()
