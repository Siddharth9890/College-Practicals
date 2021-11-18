#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
int main(int argc, char *argv[])
{
    char* cval[10];
    char *newenviron[] = { NULL };
    int i,j,n,temp;
    
    cval[i]=NULL;
       
    int pid=fork();
    
    if(pid==0)
    {
        printf("I am child process\n");
        printf("Child process id:%d\n",getpid());
        execve(argv[1], cval, newenviron);
        perror("Error in execve call...");
    }
    
    sleep(3);
    printf("I am Parent\n");
}