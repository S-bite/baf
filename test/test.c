#include <stdio.h>
int main()
{
    int a = 0 /*@ 1,2,3*/;
    int b = 0 /*@ 1,2,3*/;
    printf("%d+%d=%d\n", a, b, a + b);
    return 0;
}