#include <cstdio>
using namespace std;

int main() {

	int n, i;
	scanf("%d", &n);

	for (i = n; i--;) {
		printf("%d\n", i+1);
		if (n == i) { break; }

	}
	return 0;
}