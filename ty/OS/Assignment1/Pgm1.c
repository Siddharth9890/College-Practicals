#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
int main()
{
    printf("I am Parent process!\n");
    printf("Parent process id:%d\n",getppid());
    int pid;
    pid = fork();
    
    printf("I am child process\n");
    printf("Child process id:%d\n", getpid());
    return 0;
}