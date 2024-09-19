#include<cstdio>
#define _CRT_NO_WARNINGS
using namespace std;


int main() {
	int line;
	int i = 0;
	int a;
	int b;


	scanf("%d", &line);
	for (i; i < line; i++) {
		scanf("%d %d", &a, &b);
		printf("%d\n", a + b); 


	}
	return 0;
}