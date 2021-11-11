#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

void bubblesort(int a[], int n)
{
    for (int pass = 1; pass < n; pass++)
    {
        for (int i = 0; i <= n - pass - 1; i++)
        {
            if (a[i] > a[i + 1])
            {
                int temp = a[i];
                a[i] = a[i + 1];
                a[i + 1] = temp;
            }
        }
    }
}

void insertionsort(int a[], int n)
{
    int key, i, j;
    for (i = 1; i < n; i++) //unsorted set
    {
        key = a[i];
        for (j = i - 1; j >= 0; j--) //sorted set
        {
            if (key < a[j])
                a[j + 1] = a[j];
            else
                break;
        }
        a[j + 1] = key;
    }
}

int main()
{
    int parr[10], carr[10], n;
    printf("Enter number of elements:\n");
    scanf("%d", &n);

    printf("enter the elements:\n");
    for (int i = 0; i < n; i++)
    {
        scanf("%d", &parr[i]);
        carr[i] = parr[i];
    }

    printf("I am Parent process id: %d\n\n", getppid());

    int pid = fork();
    if (pid < 0)
    {
        printf("child process creation failed.\n\n");
    }
    else if (pid == 0)
    {
        printf("I am Child process id:%d\n\n", getpid());
        printf("child process is sorting the elements using insertion sort\n\n");
        insertionsort(carr, n);
        printf("the sorted elements using insertion sort are:\n");
        for (int i = 0; i < n; i++)
        {
            printf("%d\n", carr[i]);
        }
    }
    else
    {
        wait();
        printf("parent process is sorting the elements using bubble sort\n\n");
        bubblesort(parr, n);
        printf("the sorted elements using bubble sort are:\n");
        for (int i = 0; i < n; i++)
        {
            printf("%d\n", parr[i]);
        }
    }
    return 0;
}