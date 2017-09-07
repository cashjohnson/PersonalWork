# sort the inputArray into smallest to largest format using only random sort and
# count the iterations
from random import randint

def main(mainArray):
	placeholderArray = mainArray[:] #deepcopy, not reference
	counter = 0 #set up iteration measurement
	while True:
		if arrayCheck(placeholderArray): #stop the loops if its true
			break
		print(counter,placeholderArray) #print to show progress
		placeholderArray = arrayMix(placeholderArray) #mix everything up
		counter = counter + 1 #iterate

	print(counter,placeholderArray)
	print("It took",counter,"random iterations to sort",mainArray,"to",placeholderArray)
	return

# checked
# return mixed up array
def arrayMix(array):
	holdingArray = []
	for i in range(len(array)-1,-1,-1): #remove elements 1 at a time from array -> holdingArray
		curr = randint(0,i) #select a random element from the array
		holdingArray.append(array[curr]) #add that element to another array
		array.remove(array[curr]) #cut down original array
		# print(i,holdingArray)
	return holdingArray

# checked
# return True if sorted
# return False if not sorted
def arrayCheck(array): 
	for i in range(len(array)-1): #for whatever length of array
		if not (array[i] < array[i+1]): #check that each spot is less than the next
			return False #if that didn't happen return False
	return True #if that happened return True

if __name__ == "__main__":
	inputArray = [0,9,8,7]
	# inputArray = [0,3,2,4]
	main(inputArray)
