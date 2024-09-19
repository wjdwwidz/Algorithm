#include<cstdio>

int main(){
    int n, sum = 0;
    scanf("%d", &n);
    char myArray[n];
    scanf("%s", &myArray);
    for(int i = 0; i < n; i++){
        sum += myArray[i] - '0';
    }
    printf("%d", sum);
}