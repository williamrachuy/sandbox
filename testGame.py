import random
import time
import sys
import os

MAP_DIMENSION = {
	"x": 10,
	"y": 10
}


class Map():
	mapDimension = MAP_DIMENSION
	particleMap[][]

	def setMapDimension(self):
		mapDimension = MAP_DIMENSION

	def generateParticleMap(self):
		for columns in range(0, self.mapDimension["y"]):
			for rows in range(0, self.mapDimension["x"]):
				particle = Particle()
				self.particleMap[rows][columns] = particle.createParticle()

	def renderMap(self):
		for row in self.particleMap:
			line = ""
			for element in row:
				line += element
			print(line)

class Particle():
	particleChar = None
	particlePosition = None

	def setParticleChar(self, c = ' '):
		particleChar = c
		return self.particleChar

	def setParticlePosition(self, x = 0, y = 0):
		self.particlePosition = [x, y]
		return self.particlePosition

	def createParticle(self):
		particle = Particle()
		self.setParticleChar(particle)
		self.setParticlePosition(particle)
		return particle


class Player():
	playerChar = None
	PlayerPosition = None




if __name__ == "__main__":
	map = Map()
	map.generateParticleMap()
	while True:
		os.system('clear')
		map.renderMap()
		time.sleep(0.01)