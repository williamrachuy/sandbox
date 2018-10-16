import random
from collections import defaultdict

breeds = ['pitbull', 'lab', 'chihuahua', 'mastiff', 'poodle']
moods = ['happy', 'fun', 'sad', 'upset', 'tired', 'vexed', 'calm']
locations = ['on the bed', 'in the backyard', 'in the living room', 'in the kitchen', 'upstairs', 'at the front door']
primaries = ['sanding', 'sitting', 'laying down', 'walking around', 'sleeping']
secondaries = ['whining', 'growling', 'yawning', 'barking', 'panting', 'sniffing']
hungers = ['full', 'satisfied', 'peckish', 'hungry', 'very hungry']
# actions = ['Woof!', 'Bark!', '<Whining...>', '<Groaning...>', '<Tippy taps...>', '<Demon noises!>', '<Playing with Big Bear...>']
objects = ['a chair', 'the table', 'a pillow', 'the sheets', 'a cabinet', 'some vines']
modifiers = ['beneath', 'behind', 'inside', 'under']
situations = ['trapped']

actions_happy	= ['Woof!', 'Woof woof!!', 'Woof woof woof!!!']
actions_fun		= ['Bark!', 'Bark bark!!', 'Bark bark bark!!!', '<Wagging tail...>', '<Playing with Big Bear...>']
actions_sad		= ['<Sighs...>', '<Moans...>', '<Wants attention...>']
actions_upset	= ['<Wnines...>', '<Groans...>', '<Angrily> Wooorwooorwoor!!! >8^(']
actions_tired	= ['<Yawns...>', '<Nesting...>']
actions_vexed	= ['<Panting...>', '<Demon noises!>']
actions_calm	= ['<Tippy taps...>', '<Looking around...>']


mood_based_actions = {
	'happy' : actions_happy + actions_calm,
	'fun'	: actions_happy + actions_fun,
	'sad'   : actions_sad + actions_calm,
	'upset' : actions_upset + actions_sad,
	'tired' : actions_tired + actions_calm,
	'vexed' : actions_vexed + actions_sad + actions_upset,
	'calm'  : actions_calm
}


class Dog(object):

	def __init__(
			self,
			name,
			breed,
			age,
			hunger,
			mood,
			location,
			primary,
			secondary,
			last_action):
		self.name = name
		self.breed = breed
		self.age = age
		self.hunger = hunger
		self.mood = mood
		self.location = location
		self.primary = primary
		self.secondary = secondary
		self.last_action = last_action
		self.situation = None
		self.affection = defaultdict(int)

	def reset(
			self,
			name,
			breed,
			age,
			hunger,
			mood,
			location,
			primary,
			secondary,
			last_action,
			affection):
		self.name = name
		self.breed = breed
		self.age = age
		self.hunger = hunger
		self.mood = mood
		self.location = location
		self.primary = primary
		self.secondary = secondary
		self.last_action = last_action
		self.situation = None
		if (affection is True):
			self.affection = defaultdict(int)
		return "{} has been reset.".format(self.name)

	def getStatus(self):
		ret_string = "{0} is {1} and {2} {3}.".format(self.name, self.primary, self.secondary, self.location)
		return ret_string

	def getBreed(self):
		ret_string = "{0} is a {1}.".format(self.name, self.breed)
		return ret_string

	def getHunger(self):
		ret_string = "{0} is {1}.".format(self.name, self.hunger)
		return ret_string

	def _hunger(self):
		return self.hunger

	def getMood(self):
		ret_string = "{0} is {1}.".format(self.name, self.mood)
		return ret_string

	def _mood(self):
		return self.mood

	def getAge(self):
		ret_string = "{0} is {1} years old.".format(self.name, self.age)
		return ret_string

	def updateAction(self, action=None):
		if (action is None):
			action = random.choice(mood_based_actions[self.mood])
		self.last_action = action
		return action

	def _lastAction(self):
		return self.last_action

	def updateMood(self, mood=None):
		if (mood is None):
			mood = random.choice(moods)
		self.mood = mood
		ret_string = getMood()
		return ret_string

	def getAffection(self, person=None):
		if (person is None):
			if (len(self.affection) == 0):
				ret_string = "{}'s affection list is empty!".format(self.name)
			else:
				ret_string = "{}'s friends with everyone!\n".format(self.name)
				for key in self.affection:
					ret_string = ret_string + "{0}'s affection for {1}: {2}\n".format(self.name, key, self.affection[key])
		else:
			ret_string = "{0}'s affection for {1}: {2}".format(self.name, person, self.affection[person])
		return ret_string

	def getSituation(self):
		if (self.situation is None):
			ret_string = None
		else:
			ret_string = self.situation
		return ret_string
		
	def updateAffection(self, person, amount=1):
		self.affection[person] += amount
		return self.affection[person]

	def updateStatus(self, primary=None, secondary=None, location=None, mood=None, hunger=None, situation=None):
		# if (self.situation is not None):
		#     return
		if (primary is None):
			primary = random.choice(primaries)
		if (secondary is None):
			secondary = random.choice(secondaries)
		if (location is None):
			location = random.choice(locations)
		if (mood is None):
			mood = random.choice(moods)
		if (hunger is None):
			hunger = random.choice(hungers)
		self.primary = primary
		self.secondary = secondary
		self.location = location
		self.mood = mood
		self.hunger = hunger
		self.situation = situation

	def updateHunger(self, hunger='full'):
		self.hunger = hunger

	def updateSituation(self, situation=None):
		if ((self.situation is not None) and (situation != 'helped')):
			ret_string = "{0} is {1}!".format(self.name, self.situation)
			return ret_string

		primary = None
		secondary = None
		location = None
		mood = None
		hunger = self.hunger

		ret_string = ''
		if (situation == 'trapped'):
			primary = 'trapped'
			secondary = 'whining'
			location = random.choice(modifiers) + " " + random.choice(objects)
			mood = 'upset'
			situation = 'trapped'
		elif (situation == 'helped'):
			if (self.situation is None):
				ret_string = "{} didn't need any help...".format(self.name)
			situation = None

		self.updateStatus(primary=primary, secondary=secondary, location=location, mood=mood, hunger=hunger, situation=situation)

		return ret_string

	def updateMood(self, mood=None):
		if (mood == None):
			mood = random.choice(moods)
		self.mood = mood
		return mood