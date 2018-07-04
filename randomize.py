import random
import time
import sys

def getUserOption():
	print("\nMenu: 'q' to quit | 'g' to generate | 'c' to compare | 's' for stars")
	return str(input())

def getUserInput(prompt="No prompt"):
	print("\n" + prompt)
	return int(input())

def getRandomString(length = 10):
	retString = ""
	for i in range(0, length):
		c = chr(random.randint(0x20, 0x7E))
		retString = retString + c
	return retString

def compareStrings(string1, string2, printFlag = False):
	outString = ""
	matches = 0
	for charIndex in range(0, len(string1)):
		if string1[charIndex] == string2[charIndex]:
			matches += 1
			outString = outString + string1[charIndex]
		else:
			outString = outString + " "
	if printFlag:
		print("\n" + outString)
		percent = float(matches) / len(string1)
		print("\nFound {0} matches. {1} percent match.".format(matches, percent))
	return outString

def generateStars(speed = 1):
	delay = float(1) / float(speed)
	while True:
		print(compareStrings(string1 = getRandomString(length = 100), string2 = getRandomString(length = 100), printFlag = False))
		time.sleep(delay)

if __name__ == "__main__":
	while True:
		myOption = getUserOption()
		if myOption is "q":
			break
		elif myOption is "g":
			myLength = getUserInput("Enter length")
			myString = getRandomString(length = myLength)
			print("\n" + myString)
		elif myOption is "c":
			myLength = getUserInput("Enter length")			
			myString1 = getRandomString(length = myLength)
			myString2 = getRandomString(length = myLength)
			print("\nComparing letter sequences:")
			print("\n" + myString1 + "\n\n" + myString2)
			compareStrings(string1 = myString1, string2 = myString2, printFlag = True)
		elif myOption is "s":
			mySpeed = getUserInput("Enter speed")
			generateStars(speed = mySpeed)
