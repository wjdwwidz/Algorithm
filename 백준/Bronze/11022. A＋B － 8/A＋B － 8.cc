#include<cstdio>
using namespace std;
int main() {

	int n, a, b, i,sum;
	scanf("%d", &n);
	for (i = 1; i <= n; i++) {
		scanf("%d %d", &a, &b);
		sum = a + b;

		printf("Case #%d: %d + %d = %d\n", i,a,b,sum);


	}


	return 0;
}