/*
A hilariously bad solution to a very simple problem in order to force myself to work with classes and pointers

Problem:
Given the sum of length, breadth and height of a cuboid. The task is to find the maximum volume that can be achieved such that the sum of sides is S.

Input:
The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. Each test case contains an integer S.

Output:
For each test case, print the maximum volume you can obtain in new line.

Constraints:
1<=T<=500
3<=S<=105

Example:
Input:
2
4
8

Output:
2
18
*/

#include <iostream>
using namespace std;

class Cuboid {
	public:
	int width, length, height;
	unsigned long volume;
	Cuboid(int, int, int);
	unsigned long area();
};

Cuboid::Cuboid(int x, int y, int z){
	width = x;
	length = y;
	height = z;
}

unsigned long Cuboid::area() {
	unsigned long widthl = (unsigned long) this->width;
	unsigned long lengthl = (unsigned long) this->length;
	unsigned long heightl = (unsigned long) this->height;
	this->volume = widthl*lengthl*heightl;
	return this->volume;
}


int main(){
	cout << "Please input the number of testCases:";
	int testCases;//input the number of test cases
	cin >> testCases;
	cout << endl;
	int counter = 1;//to make things a little more user friendly

	while (testCases>0){ //while loop through each test case
		cout << "Input the sum for test case #" << counter;
		int sum;//input the sum
		cin >> sum;
		cout << endl;

		Cuboid * largestCube = new Cuboid(sum-2,1,1); //a starting smallest volume cuboid to start comparison against

		for (int i = sum-2; i >= sum/3; i--){//iterating through all the variations
			for (int j = 1; j <= i; j++){
				for (int k = 1; (i+j+k) <= sum; k++){
					if (i+j+k == sum){//taking only the variations that sum to the total (because they will be the largest)
						cout << i << "L " << j << "W " << k << "H " << (i+j+k) << endl;
						Cuboid * newCube = new Cuboid(i,j,k);//creating a new cuboid with the dimensions
						if (newCube->area() > largestCube->area()){//reassigning largestCuboid if newCube is larger
							delete largestCube;
							largestCube = newCube;
						}
					}

				}	
			}
		}
		cout << "Best cube for sum=" << sum <<" was " << largestCube->width << "W ";
		cout << largestCube->length << "L " << largestCube->height << "H with a total area of " << largestCube->area() << endl;
		testCases--;//iterating through test cases
		counter++;//iterating for formatting
	}
	

	return 0;
}