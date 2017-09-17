#include <stdio.h>

int main(int argc, char *argv[]){
	
	char mer[100] = {'a','b','c'};
	char first[] = "Cash";
	char initial = 'N';
	char thing[] = "";


	printf("Hi, I'm %s %c.\n", first, initial);
	printf("is this %s a thing?\n", thing);

	int value = 5;

	int things = value * initial;
	printf("%d\n\n\n\n",things);
	printf("%s", mer);
	mer[2] = 'e';
	printf("%s", mer);

	printf("%ld\n", sizeof(int));

	return 0;
}