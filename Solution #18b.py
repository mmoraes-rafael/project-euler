from Solution_18a import matrix

#print("%d" % matrix[1][1])

answer = [[0 for i in range(0, 16)] for j in range(0,16)]
answer[0][0] = 75

for line in range(0, 16):
	for col in range(0, 16):
		if col > line:
			continue 
		
		if(line < 15):
			if col > 0:
				sup = max((answer[line - 1][col], answer[line - 1][col - 1]))
			else:
				if line > 0:
					sup = answer[line - 1][col]
				else:
					sup = 0

			answer[line][col] = matrix[line][col] + sup


for line in range(0, 16):
	for col in range(0, 16):
		if col > line:
			continue 
		print("%5d" % answer[line][col]),
	print("\n")
		
print("\n\nO valor do maior caminho eh: %d" % max(answer[14]))
			
