#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
int
main ()
{
  printf ("I am Parent process id:%d\n", getppid ());

  int pid = fork ();
  if (pid < 0)
    {
      printf ("Chile Creation Failed!\n");
    }
  if (pid == 0)
    {
      wait ();
      printf ("I am Child process id:%d\n", getpid ());
      printf ("I am init process id:%d\n", getppid ());
    }
  else
    {
      sleep (500);
    }

  return 0;
}
