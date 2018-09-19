import random
from datetime import datetime

random.seed(datetime.now())

CHOICES = ['rock', 'paper', 'scisors']
XTENDED = ['rp', 'ps', 'sr']
BEATS = {
    'rock'    : ['paper',   'ps'],
    'paper'   : ['scisors', 'sr'],
    'scisors' : ['rock',    'rp'],
    'rp'      : (['rock', 'paper']    + XTENDED),
    'ps'      : (['paper', 'scisors'] + XTENDED),
    'sr'      : (['scisors', 'rock']  + XTENDED)
}

class Player(object):
    def __init__(self, name, intellect='human'):
        self.name = name
        self.intellect = intellect
        self.choice = 'none'
        self.collection = {
            'rock'      : 0,
            'paper'     : 0,
            'scisors'   : 0,
            'rp'        : 0,
            'ps'        : 0,
            'sr'        : 0
        }

    def getName(self):
        name = self.name
        return name

    def getIntellect(self):
        intellect = self.intellect
        return intellect


    def getWinCollection(self):
        wins_rock = self.collection['rock']
        wins_paper = self.collection['paper']
        wins_scissors = self.collection['scisors']
        wins_rp = self.collection['rp']
        wins_ps = self.collection['ps']
        wins_sr = self.collection['sr']
        return [wins_rock, wins_paper, wins_scissors,
                wins_rp, wins_ps, wins_sr]

    def updateWinCollection(self, choice):
        self.collection[choice] += 1

    def setChoice(self, choice):
        if (choice in (CHOICES + XTENDED)):
            self.choice = choice
            return True
        else:
            self.choice = 'none'
            return False

    def getChoice(self):
        choice = self.choice
        return choice


def playerTurn(player):
    name = player.getName()
    intellect = player.getIntellect()
    if (intellect == 'human'):
        print("{}, choose now".format(name))
        valid = False
        while (valid == False):
            choice = input(">>> ")
            valid = player.setChoice(choice)
            if (valid == False):
                print("I didn't understand your choice. Try again...")
    elif (intellect == 'stupid'):
        choice = random.choice((CHOICES + XTENDED))
        valid = player.setChoice(choice)
        print("{0} chooses: {1}".format(name, choice))
    else:
        print("Player turn error. Possibly invalid intellect.")

def determineWinners(players):
    for attacking in players:
        for defending in players:
            if (attacking is not defending):
                attacking_choice = attacking.getChoice()
                defending_choice = defending.getChoice()
                if (attacking_choice in BEATS[defending_choice]):
                    attacking.updateWinCollection(defending_choice)

def getPlayers():
    player1_intel = 'human'
    player2_intel = 'human'
    valid = False
    while (valid == False):
        print("Select game type: hvh, hvr, rvr?")
        game_type = input(">>> ")
        if (game_type in ['hvh', 'hvr', 'rvr']):
            valid = True
            if (game_type == 'hvh'):
                pass
            elif (game_type == 'hvr'):
                player2_intel = 'stupid'
            elif (game_type == 'rvr'):
                player1_intel = 'stupid'    
                player2_intel = 'stupid'
        else:
            print("I didn't understand your choice...")
    player1 = Player(name='Player 1', intellect=player1_intel)
    player2 = Player(name='Player 2', intellect=player2_intel)
    players = [player1, player2]    
    return players

def playGame(players):
    turn_counter = 0
    while (True):
        turn_counter += 1
        print("Turn {}".format(turn_counter))
        for player in players:
            playerTurn(player=player)
        determineWinners(players=players)
        for player in players:
            name = player.getName()
            win_collection = player.getWinCollection()
            print("[{0}] R: {1} | P: {2} | S: {3} | RP: {4} | PS: {5} | SR: {6} | Total: {7}".format(name,
                    win_collection[0], win_collection[1], win_collection[2],
                    win_collection[3], win_collection[4], win_collection[5],
                    sum(win_collection)))

def main():
    players = getPlayers()
    playGame(players=players)


if __name__ == '__main__':
    main()