#include <cstdio>
using namespace std;

int main() {

	int N;
	int i;

	scanf("%d", &N);
	

	for (i = 1; i <= 9; i++) {
		int answer = i * N;
		printf("%d * %d = %d \n", N,i, answer );
	}

	return 0;
}