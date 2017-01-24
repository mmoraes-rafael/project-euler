
def fact(x):
	if(x == 1):
		return 1
	elif(x == 0):
		return 1
	elif(x == 2):
		return 2
	elif(x == 3):
		return 6
	elif(x == 4):
		return 24
	elif(x == 5):
		return 120
	elif(x == 6):
		return 720
	elif(x == 7):
		return 5040
	elif(x == 8):
		return 40320
	elif(x == 9):
		return 362880
	else:
		return x * fact(x-1)

L = []
for i in range(3, 10000000):
	x = i
	soma = 0
	while x > 0:
		dig = x % 10
		#print ("x: %d  |  dig: %d" % (x, dig))
		x /= 10
		soma += fact(dig)
		if(soma > i):
			continue
	if(soma == i):
		L.append(i)

print(sorted(L))
print("\n\nExistem: %d" % len(L)) 
