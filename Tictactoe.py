import getpass as gt


def rules_and_control():
	print("""Welcome to Tic Tac Toe!
The rules are simple, get 3 in a row with your piece to win.
Use the coordinate system to place your piece.
Good luck and have fun!
""")

rules_and_control()


def board(p2_y=0, p2_x=0, p1_x=0, p1_y=0, just_display=False):
	board = []

	for i in range(3):
		board.append(["[ ]"] * 3)

	player_X = '[X]'
	player_O = '[O]'

	if not just_display:
		board[p1_x][p1_y] = player_X 
		board[p2_x][p2_y] = player_O

	print('   0  1  2')
	for count, row in enumerate(board):
		print(count, "".join(row))


board(just_display=True)


def game():
	p1_x = gt.getpass('In which column would you like to put your piece P1? ')
	p1_y = gt.getpass('In which row would you like to put your piece P1? ')
	p2_x = gt.getpass('In which column would you like to put your piece P2? ')
	p2_y = gt.getpass('In which row would you like to put your piece P2? ')
	board()


game()
