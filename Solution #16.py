def count(x):
	soma = 0
	while x > 0:
		soma += x % 10
		x /= 10
	return soma

for i in range(1, 10000):
	n = pow(2, i)
	print("%d:: %8d | %4d\n" % (i, n, count(n)))
