# input = "78 87 16 94 36 93 50 87 22 63 28 91 60 64 27 41 27 73 12 69 37 68 30 83 31 63 24 68 30 36 3 59 23 70 68 94 12 57 30 74 22 43 20 85 38 99 16 71 14 27 25 92 57 81 63 74 71 97 6 82 26 85 28 37 6 47 14 58 25 96 30 83 15 68 35 65 44 51 46 88 9 79 77 89"

input = "78 87 16 94 36 93 50 87 22 63 28 91 60 64 27"

array = input.split()

print array


for i in range(1,len(array)):
	if (i % 2 == 0):
		if (int(array[i]) > int(array[i-1])):
			print "You've made a mistake at index %d" % i
	else:
		if (int(array[i]) < int(array[i-1])):
			print "You've made a mistake at index %d" % i

print "No mistakes!"