print "enter a positive integer"
n = input()
n1 = n
number=0
while n1 != 0:
	rem = n1 % 10
	number += rem * rem * rem
	n1 = n1 / 10

if number == n:
	print "num is amstrong"
else:
	print "num is not amstrong"
