WHAT_BEATS = {
	'rock' 	  : 'paper',
	'paper'   : 'scisors',
	'scisors' : 'rock'
}

CHOICES = ['rock', 'paper', 'scisors']

class Player(object):
	def __init__(self, name):
		self.name = name
		self.choice = 'none'
		self.collection = {
			'rock' 		: 0,
			'paper' 	: 0,
			'scisors' 	: 0
		}

	def getCollection(self):
		wins_rock = self.collection['rock']
		wins_paper = self.collection['paper']
		wins_scissors = self.collection['scisors']
		return [wins_rock, wins_paper, wins_scissors]

	def setChoice(self, choice):
		if coice in CHOICES:
			self.choice = choice
			return True
		else:
			self.choice = 'none'
			return False

def playerTurn(player):
	print("{}, choose now".format(player.name))
	valid = False
	while (valid == False):
		choice = input(">>> ")
		if choice is in ['rock', 'paper', 'scisors']:
			player.setChoice(choice)
			valid = True
		else:
			print("I didn't understand your choice...")
			valid = False




def main():
	player1 = Player('Player 1')
	player2 = Player('Player 2')
	players = [player1, player2]

	turn_counter = 0
	while (True):
		turn_counter += 1
		print("Turn {}".format(turn_counter))
		for player in players:
			playerTurn(player=player)




if __name__ == '__main__':
	main()