t = 0
x = 0
y = 1

for i in range(0, 20):
	t = y
	y += x
	x = t
	print(y)
