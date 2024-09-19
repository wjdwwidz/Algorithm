#define _CRT_SECURE_NO_WARNINGS
#include<cstdio>

int main() {

	int myArray[9];
	int input;
	int max = 0;

	for (int i = 0; i < 9; i++) {
		scanf("%d", &input);
		myArray[i] = input;
	
		if (input > max) {
			max = input;
		}
	}
	printf("%d\n", max);

	for (int i = 0; i < 9; i++) {
		if (max == (int)(myArray[i]))
		    printf("%d", i + 1);
	}
	return 0;

}