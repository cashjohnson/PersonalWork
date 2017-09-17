#include <stdio.h>

int main(int argc, char *argv[]){

	int i = 0;

	// let's make our own array of strings
	int num_states = 4;
	char *states[] = {
		"California", "Oregon",
		"Washington", "Texas"
	};

	printf("\n\n\n\n\n");
	int j = 0;
	while (states[1][j] != '\0'){
		char letter = states[1][j];
		printf("%c\n", letter);
		j++;
	}

	for(i = 1; i < argc; i++) {
		printf("arg %d: %s\n", i, argv[i]);
	}
		
	for(i = 0; i < num_states; i++) {
		printf("state %d: %s\n", i, states[i]);
	}
	
	// go through each string in argv
	// why am I skipping argv[0]?
	i = 0;
	while (i < num_states){
		argv[i+1] = states[i];
		i++;
	}

	for(i = 1; i < argc; i++) {
		printf("arg %d: %s\n", i, argv[i]);
	}
		
	for(i = 0; i < num_states; i++) {
		printf("state %d: %s\n", i, states[i]);
	}

	return 0;
}