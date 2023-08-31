
#include<cstdio>
#include<cstdlib>
#include <algorithm>
using namespace std;


int main(){
	int N,M,i;
	scanf("%d", &N);
	int* arr = (int*)malloc(sizeof(int) * N);

	
	for (i = 0; i < N; i++) {
		scanf("%d", &arr[i]);
	}

	sort(arr, arr + N);
	
	for (i = 0; i < N; i++) {
		printf("%d\n", arr[i]);
	}


	return 0;
}