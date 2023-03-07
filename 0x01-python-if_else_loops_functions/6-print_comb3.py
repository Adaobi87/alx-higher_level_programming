#!/usr/bin/python3
for n in range(0, 10):
	for x in range(n + 1, 10):
	if n == 8 and x == 9:
		print(98)
	else:
		print('{}{}, '.format(n,x), end='')
