def count_tamanho(x):
	tamanho = 0
	while x > 0:
		tamanho += 1
		x /= 10
	return tamanho

fib_arr = [0 for i in range(10000)]
fib_arr[0] = 1
fib_arr[1] = 1

def fibo(x):
	global fib_arr
	if(fib_arr[x] == 0):
		fib_arr[x] = fibo(x - 1) + fibo(x - 2)
	return fib_arr[x]

print("fibo(%d) tem %d digitos" % (10, count_tamanho(fibo(10))))

#for i in range(10,10000):
#	num = count_tamanho(fibo(i))
#	print("%d: num = %d" % (i, num))
#	if(num > 999):
#		print("\n\nO numero eh: fibo(%d) = %d\n\n" % (i, fibo(i)))
#		break
