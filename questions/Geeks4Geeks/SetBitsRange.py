
def bitConversion(values):
	values = values.split()
	inputNumBin = str(bin(int(values[0])))
	val = ['0','b']
	bits = len(inputNumBin)
	for i in range(2,bits):
		if ((bits - i) >= int(values[1]) and (bits - i) <= int(values[2])):
			val.append('1')
		else:
			val.append('0')

	val = "".join(val)
# 	print(val)
# 	print(inputNumBin)
	output = int(val[2:],2) | int(inputNumBin[2:],2)
	print(output)


testCases = input()
# strings = []
# strings.append(input())
testCases = int(testCases)

while testCases>0:
	bitConversion(input())
	testCases = testCases - 1

