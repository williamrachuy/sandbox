import random
import time
import sys
import os

MAX_X = 5
MAX_Y = 5

mapTemplate = array(
	['.', '.', '.', '.'],
	['.', '.', '.', '.'],
	['.', '.', '.', '.'],
	['.', '.', '.', '.']
)

playerChar = 'o'

if __name__ == "__main__":
	playerLoc = array(0, 0)
	playerVec = array(1, 1) 
	while True:
		map = mapTemplate
		map[playerLoc[0], playerLoc[1]] = playerChar
