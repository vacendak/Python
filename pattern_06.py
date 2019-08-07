for i in range(0, 10):
	for j in range(0, i):
		print(' ', end = ' ')
	for k in range(0, 19 - 2 * i):
		print('*', end = ' ')
	print('')