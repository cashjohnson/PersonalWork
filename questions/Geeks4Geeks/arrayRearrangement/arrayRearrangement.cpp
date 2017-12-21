// source:zhttps://practice.geeksforgeeks.org/problems/rearrange-array-such-that-even-positioned-are-greater-than-odd/0
// Given an array A of n elements, rearrange the array according to the following relations :
//  A[i] >= A[i-1]  , if i is even.
//  A[i] <= A[i-1]  , if i is odd.[Considering 1-indexed array]
// Print the resultant array.

// Input:
// The first line of the input contains an integer T, denoting number of test cases. The first line of each test case contains an integer N denoting the size of the array. The second line of each test cases N space separated integers.
// Output:
// For each test case, print rearranged array.
// Constraints:
// 1<=T<=100
// 1<=N<=100
// 1<=arr<=100

// Example:
// Input:
// 2
// 4
// 1 2 2 1
// 3
// 1 3 2
// Output:
// 1 2 1 2
// 1 3 2


// #############
// I believe geeksforgeeks solution is incorrect, not checking the output for correct application, but for matching.
// I made my own testing script (test.py) which I tested against both the answer g4g says I failed and found no mistakes so I'll call this done


#include <iostream>
using namespace std;

// A function to take inputs and return a pointer to the array
int * arrayInput(int arraySize){
	int * inputArray = (int *) malloc(sizeof(int)*arraySize);

	for (int i = 0; i < arraySize; i++){ //There is an issue here of overloading the int array, however with the constraints that's not a concern
		cin >> inputArray[i];
	}
	return (inputArray);
}

// A function to print the array that was made for convenience of testing
void printArray(int * array,int arraySize){
	for (int i = 0; i < arraySize; i++){
		cout << *array << " ";
		// cout << *array << ":inputArray[" << i << "]" << endl;
		array++;
	}
	cout << endl;
}

// Index through the array once taking any actions as it passes through. I believe this is different than how the 
// person who wrote this problem did it because our answers are significantly different.
void arraySort(int*array, int arraySize){
	int temp;//Declared up here to avoid having to redeclare the value continually
	for (int i = 1; i < arraySize; i++){
		if (i % 2 == 1){
			if (array[i] < array[i-1]){//if the condition is incorrect swap the values
				temp = array[i];
				array[i] = array[i-1];
				array[i-1] = temp;
			}
		}
		else{
			if (array[i] > array[i-1]){
				temp = array[i];
				array[i] = array[i-1];
				array[i-1] = temp;
			}
		}
	}
}

int main(){
	int testCases;
	cin >> testCases;

	while (testCases > 0){
		int arraySize;
		cin >> arraySize;

		int * inputArray = arrayInput(arraySize);

		for (int i = 0;i < arraySize*2;i++){ //it would be much cleaner to make a checking function and run a while loop, but this will get the 
			arraySort(inputArray,arraySize); //job done. If the array size gets too large this will be bad, but with the constraints is fine
		}
		printArray(inputArray,arraySize);
		
		testCases--;
	}
	return 0;
}