import praw
import config

def botLogin():
	instance = praw.Reddit(
		username = config.username,
		password = config.password,
		client_id = config.client_id,
		client_secret = config.client_secret,
		user_agent = "it's a secret to everyone")
	return instance

def printComment(comment):
	print("===========================================================")
	print(comment.author, "writes:")
	print(comment.body)
	print("-----------------------------------------------------------")
	print("\n")

def findString(string, subreddit):
	flag = False
	for comment in instance.subreddit(subreddit).comments(limit = 25):
		#print(comment.body)
		if string in comment.body:
			printComment(comment)
			flag = True
	return flag

def runBot(instance):
	if findString("abacus", "test"):
		# print("String successfully found")
		pass
	else:
		print("String not found")


if __name__ == "__main__":
	instance = botLogin()
	runBot(instance)