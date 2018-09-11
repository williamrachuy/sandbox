import random

play_tokens = ['X', 'O']

# board_chars = [
#     '0', '1', '2',
#     '3', '4', '5',
#     '6', '7', '8'
# ]

board_chars = [
    '.', '.', '.',
    '.', '.', '.',
    '.', '.', '.'
]


class Board(object):
    def __init__(self):
        self.board = board_chars
        print(self.board)

        self.winPatterns = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            [0, 4, 8], [2, 4, 6]
        ]

    def printBoard(self):
        rows = [self.board[0:3], self.board[3:6], self.board[6:9]]
        print()
        for row in rows:
            print("{0} {1} {2}".format(row[0], row[1], row[2]))
        print()

    def placeToken(self, token, position):
        if (self._checkValidToken(token) and self._checkValidPosition(position) and self._checkValidPlacement(position)):
            self.board[position] = token
            return True
        else:
            return False

    def checkWin(self, token):
        board = self.board
        for pattern in self.winPatterns:
            if (    self._checkSameToken(board[pattern[0]], token) and
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


class Player(object):
    def __init__(self, token):
        self.token = token
        self.name = "Player {}".format(token)
        self.win = False

    def getToken(self):
        return self.token

    def getName(self):
        return self.name


def playerMove(player, board):
    player_name = player.getName()
    player_token = player.getToken()
    print("{}, place your token...".format(player_name))
    player_position = int(input(">>> "))
    result = board.placeToken(token=player_token, position=player_position)
    # print("{0} places {1} at position {2} with outcome {3}".format(
    #     player_name, player_token, player_position, result))


def switchPlayers(current_player, players):
    for player in players:
        if player is not current_player:
            return player


def playGame():
    print("\nBeginning new game...")
    board = Board()
    player1 = Player(token=play_tokens[0])
    player2 = Player(token=play_tokens[1])
    winner = None

    current_player = player1
    board.printBoard()
    while (winner == None):
        playerMove(player=current_player, board=board)
        board.printBoard()
        if (board.checkWin(current_player.token) == True):
            winner = current_player
            print("{} wins the game!".format(winner.name))
            return
        else:
            current_player = switchPlayers(
                current_player=current_player, players=[player1, player2])


def checkReplay():
    while (True):
        print("Player another game? [ yes | no ]")
        answer = input(">>> ")

        if (answer == "yes"):
            return True
        if (answer == "no"):
            return False
        else:
            print("I didn't get that.")


def main():
    replay = True
    while (replay == True):
        playGame()
        replay = checkReplay()


if __name__ == '__main__':
    main()
