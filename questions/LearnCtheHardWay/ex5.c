#include <stdio.h>

int main(int argc, char *argv[]){
	
	printf("%d",argc);
	printf("%s",argv[0]);

	int distance = 100;

	printf("You are %d miles away\n", distance);

	return 0;
}