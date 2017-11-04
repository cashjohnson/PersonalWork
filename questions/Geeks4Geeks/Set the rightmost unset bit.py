
def setRightmostBit(value):
	inputNumBin = str(bin(int(values[0])))[2:]
	for i in range(0,len(inputNumBin)):
		checkValue = int(value) | 1 << i
		if (checkValue) != int(value):
			print(checkValue)
			break

testCases = input()
testCases = int(testCases)

while testCases > 0:
	setRightmostBit(input())
	testCases = testCases - 1