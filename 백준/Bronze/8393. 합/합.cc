#include<cstdio>
#define _CRT_NO_WARNINGS
using namespace std;

int main() {

	int n, answer;

	scanf("%d", &n);
	answer = (n * (n + 1)) * (0.5);
	printf("%d", answer);

	

	return 0;

}