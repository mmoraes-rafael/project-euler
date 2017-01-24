
def get_digit_pow_sum(x):
	soma = 0
	while x > 0:
		dig = x % 10
		x /= 10
		soma += pow(dig, 5)
	return soma

soma = 0
k = 0
for i in range(1, 1000000):
	if get_digit_pow_sum(i) == i:
		k += 1
		print("\n[%d]: %d" %(k, i))
		soma += i
print("\n\nSoma: %d" % soma)
