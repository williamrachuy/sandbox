# basic functions using combinations
def findTerms1(terms, target, a, b):
	for i in terms:
		for j in terms:
			# print(i, "+", j, "=?", target)
			if (i + j == target):
				a[0] = i
				b[0] = j
				return True
	return False

# streamlined function using permutations
def findTerms2(terms, target, a, b):
	for i in range(0, len(terms)):
		for j in range(i + 1, len(terms)):
			# print(terms[i], "+", terms[j], "=?", target)
			if (terms[i] + terms[j] == target):
				a[0] = terms[i]
				b[0] = terms[j]
				return True
	return False

# run main
if __name__ == "__main__":

	# define terms and target
	terms  = [2, 7, 11, 15]
	target = 0
	a, b   = [0], [0]

	# get user input
	print("List:", terms)
	target = int(input("Find target: "))

	# find terms using combinations
	if findTerms1(terms, target, a, b):
		print("Terms are", a[0], "and", b[0])
	else:
		print("No terms were found")

	#find terms using permutations
	if findTerms2(terms, target, a, b):
		print("Terms are", a[0], "and", b[0])
	else:
		print("No terms were found")