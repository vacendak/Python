for i in range(0, 10):
	for j in range(0, 9 - i):
		print(' ', end = ' ')
	for k in range(0, 2 * i + 1):
		print('*', end = ' ')
	print('')
for i in range(0, 10):
	for j in range(0, i + 1):
		print(' ', end = ' ')
	for k in range(0, 17 - 2 * i):
		print('*', end = ' ')
	print('')