for i in range(0, 10):					#Number of rows
	for j in range(0, i):				#Blank spaces before the stars
		print(' ', end = ' ')
	for k in range(0, 19 - 2 * i):		#Number of stars per row
		print('*', end = ' ')
	print('')							#New line after each row