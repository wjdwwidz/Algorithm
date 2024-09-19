#define _CRT_SECURE_NO_WARNINGS
#include<cstdio>

int main() {

	int A;
	int B;
	while (1)
	{
		scanf("%d %d", &A, &B);
	
		int answer = A + B;
		if (A == 0 && B == 0) break;
		printf("%d\n" ,answer);
	}


	return 0;
}