from sets import Set

L = Set(())
for a in range(2, 101):
	for b in range(2, 101):
		L.add(pow(a, b))

print(sorted(L))
print("\nLen: %d" % len(L))
