def count(x):
	soma = 0
	while x > 0:
		soma += x % 10
		x /= 10
	return soma

def partfat(x):
	if x > 1:
		return x * partfat(x-1)
	else:
		return 1

print("soma dos digitos de 100! eh %d" % count(partfat(100)))
