#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include<string>

int main() {
    int list[10];
    int tmp[42] = { 0 };
    int cnt = 0;

    for (int i = 0; i < 10; i++) {
        scanf("%d", &list[i]);
        tmp[list[i] % 42]++;
    }

    for (int i = 0; i < 42; i++)
        if (tmp[i] != 0)
            cnt++;

    printf("%d\n", cnt);

}