#define _CRT_SECURE_NO_WARNINGS
#include <cstdio>
int main() {
    int Box = 0, input;
    scanf("%d", &input);

    while (1) {
        if (input % 5 == 0) { //5로 나누어질때 
            Box += input / 5;
            printf("%d", Box);
            break;
        }

        input = input - 3;  //
        Box++;

        if (input < 0) {
            printf("-1");
            break;
        }
    }
    return 0;
}