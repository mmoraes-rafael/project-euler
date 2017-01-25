IS_AMICABLE = 1
NOT_AMICABLE = 0

def sum_divs(number):
	soma = 1
	for i in range(2, int(number/2)+1):
		if number % i == 0:
			soma += i
	return soma

def is_amicable(num):
	result = sum_divs(num)
	if sum_divs(result) == num and result != num:
		return IS_AMICABLE
	else:
		return NOT_AMICABLE

total = 0
for num in range(1, 10000):
	if is_amicable(num):
		total += num

print total
