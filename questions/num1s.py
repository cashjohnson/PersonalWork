import sys

inNum = sys.argv[1]
number = int(inNum)
counter = 0

for i in range(64,-1,-1):
	value = 2**i
	# print value
	if number >= value:
		counter = counter + 1
		number = number - value

print "The number input is",inNum
print "There are",counter,"bits if this is an unsigned int"