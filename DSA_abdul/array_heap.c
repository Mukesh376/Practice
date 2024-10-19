#include <stdio.h>
#include <stdlib.h>

int main()
{
    int A[5] = {1, 2, 3, 4, 5}; // static allocation of array in stack
    int* p;
    p = (int*)malloc(5 * sizeof(int));

    for (int i = 0; i < 5; i++)
    {
        printf("%d\t", A[i]);
        printf("%p\n", (void*)&p[i]);
    }

    free(p); // Don't forget to free the allocated memory
    return 0;
}