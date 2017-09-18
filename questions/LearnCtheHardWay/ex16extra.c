#include <stdio.h>
#include <assert.h>
#include <stdlib.h>
#include <string.h>

struct Person {
	char *name;
	int age;
	int height;
	int weight;
};


struct Person createPerson(char *name, 
			int age, 
			int height, 
			int weight){
	struct Person who;
	who.name = name;
	who.age = age;
	who.height = height;
	who.weight = weight;
	return who;
}

void printPerson(struct Person who){
	printf("%s\n", who.name);
	printf("%d\n", who.age);
	printf("%d\n", who.height);
	printf("%d\n", who.weight);
	return;
}

int main(){

	struct Person Cashie;

	Cashie.name = "Cashie";
	Cashie.age = 22;
	Cashie.height = 64;
	Cashie.weight = 168;

	struct Person Anneliese = createPerson("Anneliese", 22, 60, 130);

	// createPerson("Cashie", 22, 64, 168);

	printPerson(Cashie);
	printPerson(Anneliese);
	return 0;
}