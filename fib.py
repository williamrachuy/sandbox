num1 = 0
num2 = 1

count = 13

print('-'*num1)
print('-'*num2)
# print(num1)
# print(num2)
for current in range(0, count):
	num3 = num1 + num2
	# print(num3)
	# print('-' * num3)
	print("{}".format(num3 / num2))
	num1 = num2
	num2 = num3
