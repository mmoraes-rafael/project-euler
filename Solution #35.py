from math import sqrt, ceil

def is_prime(x):
	for i in range(2, int(ceil(sqrt(x))) + 1):
		if x % i == 0:
			return 1
	return 0

def count_digits(x):
	digits = 0
	while x > 0:
		digits += 1
		x /= 10
	return digits

def rotate(x, rot):
	st = str(x)
	for i in range(0, rot):
		st = st[-1] + st[0:-1]
	return int(st)
	

def check_num(x):
	for rot in range(0, count_digits(x)):
		if(is_prime(rotate(x, rot)) == 1):
			return 1
	return 0

	
L = []
for num in range(3, 1000000):
	if(check_num(num) == 0):
		L.append(num)

print(sorted(L))
print("\n\nExistem: %d" % len(L)) 
