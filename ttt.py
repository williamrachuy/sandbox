import random

class Board(object):
	def __init__(self):
		self.board = [
			'0','1','2',
			'3','4','5',
			'6','7','8'
		]

	def printBoard(self):
		rows = [self.board[0:3], self.board[3:6], self.board[6:9]]
		for row in rows:
			print("{0} {1} {2}".format(row[0], row[1], row[2]))

	def placeToken(self, token, position):
		if (not (token is 'X' or 'O')):
			print("Token {} not valid".format(token))
			return False
		if (position not in range(0, 9)):
			print("Position {} not valid".format(position))
			return False
		self.board[position] = token
		return True

		pass

class Player(object):
	def __init__(self, token):
		self.token = token

	def getToken(self):
		return self.token

	# @property
	# def token(self):
	# 	return self._token

	# @token.setter
	# def token(self, token):
	# 	self._token = token


def main():
	player1 = Player(token = 'X')
	player2 = Player(token = 'O')
	board = Board()

	board.printBoard()
	print()

	player_token = player1.getToken()
	player_position = 4
	result = board.placeToken(token = player_token, position = player_position)
	print("Player places {0} at position {1} with outcome {2}".format(player_token, player_position, result))
	board.printBoard()
	print()

	player_token = player2.getToken()
	player_position = 1
	board.placeToken(token = player_token, position = player_position)
	print("Player places {0} at position {1} with outcome {2}".format(player_token, player_position, result))
	board.printBoard()
	print()

	pass

if __name__ == '__main__':
	main()