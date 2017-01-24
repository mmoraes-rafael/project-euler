import numpy

matrix = numpy.zeros((22,22))

matrix[0][0] = 1

for i in range(0, 21):
	for j in range (0, 21):
		if i + j > 0: 
			if i == 0 or j == 0: 
				matrix[i][j] = 1		
			else:
				matrix[i][j] = matrix[i - 1][j] + matrix[i][j - 1]

for i in range(0, 21):
	for j in range (0, 21):
		print("%8d " % matrix[i][j]),
	print("\n")
