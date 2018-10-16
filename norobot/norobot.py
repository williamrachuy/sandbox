import discord
import random
import dog
import pickle
import asyncio
from dog import Dog

noro_file = "noro.pkl"
default_channel_id = 'Norobot'
minutes = 60
poopie_multiplier = 3
poopie_count = 0
tug_count = 0

def saveObject(obj, filename):
	with open(filename, 'wb') as output:  # Overwrites any existing file.
		pickle.dump(obj, output, pickle.HIGHEST_PROTOCOL)

def loadObject(filename):
	try:
		with open(filename, 'rb') as input:
			return pickle.load(input)
	except Exception as details:
		print("Error: {}".format(details))

noro = loadObject(noro_file)
if (noro is None):
	noro = Dog(
			name='Noro',
			breed='mutt',
			age='6',
			hunger='satisfied',
			mood='happy',
			location='backyard',
			primary='walking around',
			secondary='sniffing',
			last_action=None)
	noro.updateStatus()

TOKEN = 'NDk4Mjg3MjA1NjIyNzQzMDQw.DprjIA.eysq1xlN7ZxHwrRA_bQZEqST094'
client = discord.Client()
try:
	client.close()
except:
	print("Client not closed, possibly not running.")

@client.event
async def on_message(message):
	global poopie_count
	global tug_count
	# we do not want the bot to reply to itself
	if message.author == client.user:
		return

	msg_cont = message.content.lower()
	if (msg_cont.find('noro, what\'s wrong') >= 0):
		msg = noro.updateSituation(situation='trapped')
		msg += " " + noro.getStatus()
		await client.send_message(message.channel, msg)
	elif (msg_cont.find('noro, i\'ll help you') >= 0):
		result = noro.updateSituation(situation='helped')
		noro.updateAffection(person=message.author.mention, amount=random.choice(range(1, 3)))
		msg = "{0.author.mention} helped Noro.\n".format(message) + result
		await client.send_message(message.channel, msg)
	elif (msg_cont.find('noro,') >= 0):
		msg = "{0.author.mention} {1}".format(message, noro.updateAction())
		await client.send_message(message.channel, msg)
	elif (msg_cont.find('noro status') >= 0):
		msg = noro.getStatus()
		await client.send_message(message.channel, msg)
	elif (msg_cont.find('noro breed') >= 0):
		msg = "{}".format(noro.getBreed())
		await client.send_message(message.channel, msg)
	elif (msg_cont.find('noro hunger') >= 0):
		msg = "{}".format(noro.getHunger())
		await client.send_message(message.channel, msg)
	elif (msg_cont.find('noro mood') >= 0):
		msg = "{}".format(noro.getMood())
		await client.send_message(message.channel, msg)
	elif (msg_cont.find('noro age') >= 0):
		msg = "{}".format(noro.getAge())
		await client.send_message(message.channel, msg)
	elif (msg_cont.find('noro feed') >= 0):
		if (noro._hunger() != 'full'):
			noro.updateHunger()
			noro.updateAffection(person=message.author.mention, amount=random.choice(range(1, 5)))
			msg = "{0.author.mention} fed Noro.\n".format(message) + noro.getHunger() + "\n" + noro.updateAction('Woof!')
		else:
			msg = "Noro isn't hungry. He didn't eat anything."
			noro.updateAffection(person=message.author.mention, amount=random.choice(range(-2, 1)))
		await client.send_message(message.channel, msg)
	elif (msg_cont.find('pass time') >= 0):
		noro.updateStatus()
		msg = "Time passes for Noro..."
		await client.send_message(message.channel, msg)
	elif ((msg_cont.find('noro') >= 0) and any(x in msg_cont for x in ['good boy', 'pet'])):
		noro.updateAffection(person=message.author.mention, amount=random.choice(range(-1, 5)))
		msg = "{0.author.mention} uplifts Noro.".format(message)
		if ((noro.getMood() in ['Noro is sad.', 'Noro is upset.', 'Noro is vexed.']) and (random.choice(range(0, 5)) > 3)):
			noro.updateMood(mood=random.choice(['happy', 'tired', 'calm']))
			msg += " Noro feels better."
		await client.send_message(message.channel, msg)
	elif (msg_cont.find('noro likes me') >= 0):
		msg = noro.getAffection(person=message.author.mention)
		await client.send_message(message.channel, msg)
	elif (msg_cont.find('noro likes') >= 0):
		msg = noro.getAffection()
		await client.send_message(message.channel, msg)
	elif (msg_cont.find('noro situation') >= 0):
		msg = "{}".format(noro.getSituation())
		await client.send_message(message.channel, msg)
	elif (msg_cont.find('noro admin reset') >= 0):
		reset_affection = False
		msg_append = ''
		if (msg_cont.find('noro admin reset affection') >= 0):
			reset_affection = True
			msg_append = " Affection reset."
		msg = noro.reset(
				name='Noro',
				breed='mutt',
				age='6',
				hunger='satisfied',
				mood='happy',
				location='backyard',
				primary='walking around',
				secondary='sniffing',
				last_action=None,
				affection=reset_affection)
		msg += msg_append
		await client.send_message(message.channel, msg)
	elif (msg_cont.find('noro sleep') >= 0):
		noro.updateStatus(primary='sleeping', secondary='snoring', location='on the bed', mood='tired', situation=None)
		msg = noro.getStatus()
		await client.send_message(message.channel, msg)
	elif (msg_cont.find('noro buzz') >= 0):
		noro.updateStatus(secondary='whining', mood='upset')
		num_actions = random.choice(range(5, 10))
		noro.updateAffection(person=message.author.mention, amount=poopie_multiplier*(0 - num_actions))
		msg = "Noro is throwing a fit!"
		await client.send_message(message.channel, msg)
		for action in range(num_actions):
			await asyncio.sleep(random.choice(range(2, 10)))
			msg = noro.updateAction()
			await client.send_message(message.channel, msg)
	elif (msg_cont.find('noro scoop') >= 0):
		if (poopie_count > 0):
			count = poopie_count
			poopie_count = 0
			msg = "{0} cleaned up {1} Noro poopies. Thanks!".format(message.author.mention, str(count))
			noro.updateMood(mood='happy')
			msg += "\nNoro feels better."
		else:
			msg = "There are no poopies to clean."
		await client.send_message(message.channel, msg)
	elif (msg_cont.find('noro admin 3poopie') >= 0):
		poopie_count = poopie_count + 3
		msg = "Incremented poopie_count +3... poopie_count = {}".format(str(poopie_count))
		if (poopie_count > 10):
			msg += "\nIt stinks! There are too many poopies in the yard. Someone should clean them up..."
			noro.updateMood(mood='sad')
			msg += "\n" + noro.getMood()
		await client.send_message(message.channel, msg)
	elif (msg_cont.find('noro tug') >= 0):
		if (noro._mood() not in ['sad', 'upset', 'vexed']):
			if (noro._lastAction() == '<Tugging...>'):
				tug_count -= 1
				noro.updateAffection(person=message.author.mention, amount=1)
				if (tug_count == 0):
					noro.updateMood(mood='happy')
					msg = "Noro is finished tugging. He's so happy!"
			else:
				noro.updateAction(action='<Tugging...>')
				tug_count = random.choice(range(3, 16))
				msg = "Noro tugs back!"
		else:
			msg = "Noro doesn't feel like playing right now."
		await client.send_message(message.channel, msg)



	saveObject(obj=noro, filename=noro_file)

# @bot.command(pass_context=True)
# async def broadcast(ctx, *, msg):
#     for server in bot.servers:
#         for channel in server.channels:
#             try:
#                 await bot.send_message(channel, msg)
#             except Exception:
#                 continue
#             else:
#                 break

def get_channel(channels, channel_name):
	for channel in client.get_all_channels():
		if channel.name == channel_name:
			return channel
	return None

async def situationTask():
	await client.wait_until_ready()
	target_channel = get_channel(client.get_all_channels(), 'norobot')
	while not client.is_closed:
		await asyncio.sleep(random.choice(range(60*minutes, 360*minutes)))
		msg = noro.updateSituation(situation='trapped')
		await client.send_message(target_channel, msg)

async def statusTask():
	await client.wait_until_ready()
	target_channel = get_channel(client.get_all_channels(), 'norobot')
	while not client.is_closed:
		await asyncio.sleep(random.choice(range(30*minutes, 120*minutes)))
		noro.updateStatus()

async def actionTask():
	await client.wait_until_ready()
	target_channel = get_channel(client.get_all_channels(), 'norobot')
	while not client.is_closed:
		await asyncio.sleep(random.choice(range(5*minutes, 120*minutes)))
		if (random.choice(range(0, 100)) >= 94):
			num_actions = random.choice(range(5, 10))
			msg = "Noro is throwing a fit!"
			await client.send_message(target_channel, msg)
		else:
			num_actions = random.choice(range(1, 3))
		members = client.get_all_members()
		for member in members:
			if (member.name != 'Norobot'):
				noro.updateAffection(person=member.mention, amount=poopie_multiplier*(0 - 1))
		for action in range(num_actions):
			await asyncio.sleep(random.choice(range(2, 10)))
			msg = noro.updateAction()
			await client.send_message(target_channel, msg)

async def specialActionTask():
	global poopie_count
	await client.wait_until_ready()
	target_channel = get_channel(client.get_all_channels(), 'norobot')
	while not client.is_closed:
		await asyncio.sleep(random.choice(range(6*60*minutes, 12*60*minutes)))
		poopie_count = poopie_count + 1
		msg = updateAction(action='<Goes poopies...>')
		if (poopie_count > 10):
			msg += "\nIt stinks! There are too many poopies in the yard. Someone should clean them up..."
			msg += "\n" + noro.updateMood(mood='sad')
		await client.send_message(target_channel, msg)

@client.event
async def on_ready():
	print('Logged in as')
	print(client.user.name)
	print(client.user.id)
	print('------')
	# for channel in client.servers.channel:
	#     await client.send_message(channel, "Woof!")

client.loop.create_task(actionTask())
client.loop.create_task(statusTask())
client.loop.create_task(situationTask())
client.loop.create_task(specialActionTask())
client.run(TOKEN)