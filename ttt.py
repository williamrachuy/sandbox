import random
from datetime import datetime

random.seed(datetime.now())

play_tokens = ['X', 'O']

# board_chars = [
#     '0', '1', '2',
#     '3', '4', '5',
#     '6', '7', '8'
# ]

board_chars = []
empty_char = '-'
for c in range(0, 9):
    board_chars.append(empty_char)
    # board_chars.append(str(c))


class Board(object):
    def __init__(self, board):
        self.board = board[:]
        self.win_patterns = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            [0, 4, 8], [2, 4, 6]
        ]

    def getBoard(self):
        return self.board

    def printBoard(self):
        rows = [self.board[0:3], self.board[3:6], self.board[6:9]]
        print()
        for row in rows:
            print(" {0} {1} {2} ".format(row[0], row[1], row[2]))
        print()

    def getWinPatterns(self):
        return self.win_patterns

    def placeToken(self, token, position):
        if (self._checkValidToken(token) and self._checkValidPosition(position) and self._checkValidPlacement(position)):
            self.board[position] = token
            return True
        else:
            return False

    def checkWin(self, token):
        board = self.getBoard()
        win_patterns = self.getWinPatterns()
        for pattern in self.win_patterns:
            if (self._checkSameToken(board[pattern[0]], token) and
                    self._checkSameToken(board[pattern[1]], token) and
                    self._checkSameToken(board[pattern[2]], token)):
                return True
        return False

    def _checkValidToken(self, token):
        if (token in play_tokens):
            return True
        else:
            print("Token {} not valid".format(token))
            return False

    def _checkValidPosition(self, position):
        if (position in range(0, 9)):
            return True
        else:
            print("Position {} not valid".format(position))
            return False

    def _checkValidPlacement(self, position):
        if (self.board[position] not in play_tokens):
            return True
        else:
            print("Position {} not valid".format(position))
            return False

    def _checkSameToken(self, token1, token2):
        if (token1 == token2):
            return True
        else:
            return False

    def getEmptyPositions(self):
        board_array = self.board
        empty_positions = []
        for position in range(0, 9):
            if (board_array[position] == empty_char):
                empty_positions.append(position)
        return empty_positions

    def _arrayToMatrix(self, board):
        board_array = board.board
        board_matrix = [board_array[0:3], board_array[3:6], board_array[6:9]]
        return board_matrix

    def _arrayMatrixMap(self, matrix, position):
        matrix_map = {
            0           : [0, 0],
                1       : [0, 1],
                    2   : [0, 2],
            3           : [1, 0],
                4       : [1, 1],
                    5   : [1, 2],
            6           : [2, 0],
                7       : [2, 1],
                    8   : [2, 2]
        }
        pair = matrix_map[position]
        return pair


class Player(object):
    def __init__(self, token, intellect='human'):
        self.token = token
        self.name = "Player {}".format(token)
        self.intellect = intellect
        self.wins = 0
        self.losses = 0

    def _checkValidPositionStr(self, position):
        positions_str = []
        for n in range(0, 9):
            positions_str.append(str(n))
        if (str(position) not in positions_str):
            print("Invalid position - try again...")
            return False
        else:
            return True

    def _getUtilityValue(self, board, position):
        board_matrix = board._arrayToMatrix(board=board)
        pair = board._arrayMatrixMap(matrix=board_matrix, position=position)

        pass

    def getToken(self):
        return self.token

    def getName(self):
        return self.name

    def getIntellect(self):
        return self.intellect

    def getRandomPosition(self, board):
        empty_positions = board.getEmptyPositions()
        position = random.choice(empty_positions)
        return position

    def getUtilityPosition(self, board):
        board_array = board.board
        win_patterns = board.win_patterns
        token = self.token
        pos_util = []
        empty_positions = board.getEmptyPositions()
        for position in empty_positions:
            utility = self._getUtilityValue(board=board, position=position)
            pos_util.append([position, utility])
        for pair in pos_util:
            pass

    def getMove(self, board):
        player_intellect = self.getIntellect()
        if (player_intellect == 'human'):
            valid = False
            while (valid == False):
                position = input(">>> ")
                valid = self._checkValidPositionStr(position)
        elif (player_intellect == 'stupid'):
            position = self.getRandomPosition(board=board)
        elif (player_intellect == 'intelligent'):
            position = self.getUtilityPosition(board=board)
        else:
            print("Invalid intellect type \"{}\"".format(player_intellect))
        return int(position)

    def incrementWins(self):
    	self.wins += 1
    	return self.wins

    def incrementLosses(self):
    	self.losses += 1
    	return self.losses

    def getWins(self):
    	return self.wins

    def getLosses(self):
    	return self.losses


def playerTurn(player, board):
    player_name = player.getName()
    player_token = player.getToken()
    player_intellect = player.getIntellect()
    valid_move = False
    while (valid_move == False):
        print("{0} [{1}], place your token...".format(player_name, player_intellect))
        player_position = player.getMove(board=board)
        valid_move = board.placeToken(token=player_token, position=player_position)
        print("{0} places {1} at position {2} with outcome {3}".format(player_name, player_token, player_position, valid_move))


def switchPlayers(current_player, players):
    for player in players:
        if player is not current_player:
            return player


def playGame(player1, player2):
    print("\nBeginning new game...")
    board = Board(board=board_chars)
    winner = None

    current_player = player1
    board.printBoard()
    while (winner == None):
        playerTurn(player=current_player, board=board)
        board.printBoard()
        if (board.checkWin(current_player.token) == True):
            winner = current_player
            loser = switchPlayers(current_player=current_player, players=[player1, player2])
            winner.incrementWins()
            loser.incrementLosses()
            print("{0} [{1}] wins the game! Wins: {2}".format(winner.getName(), winner.getIntellect(), winner.getWins()))
            print("[{0}] wins: {1} | losses: {2}".format(winner.getName(), winner.getWins(), winner.getLosses()))
            print("[{0}] wins: {1} | losses: {2}".format(loser.getName(), loser.getWins(), loser.getLosses()))
            return
        elif (len(board.getEmptyPositions()) == 0):
            print("Tie game.")
            return
        else:
            current_player = switchPlayers(current_player=current_player, players=[player1, player2])


def checkReplay():
    while (True):
        print("Play again? [ yes | no ]")
        # answer = input(">>> ")
        answer = 'yes'

        if (answer in ['yes', 'Yes', 'YES', 'y', 'Y']):
            return True
        if (answer in ['no', 'No', 'NO', 'n', 'N']):
            return False
        else:
            print("I didn't get that.")


def main():
    replay = True
    player1 = Player(token=play_tokens[0], intellect='stupid')
    player2 = Player(token=play_tokens[1], intellect='stupid')
    while (replay == True):
        playGame(player1=player1, player2=player2)
        replay = checkReplay()
    print("Goodbye!")


if __name__ == '__main__':
    main()
