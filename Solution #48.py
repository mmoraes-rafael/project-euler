soma = 0

for i in range(1, 1001):
	soma += pow(i, i)

print soma % 10000000000
