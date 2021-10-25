#include<stdio.h>
#include<time.h>
#include<stdlib.h>

void display(int arr[], int n)
{
int i;
for(i=0; i<n; i++)
  printf("%d\t", arr[i]);
printf("\n");
}
void Heapify(int A[], int parent, int last)
{
   // converts tree having root A[top] into a heap
    int temp, pos, left, right;
    
    left = 2*parent+1;  //left points to left child
    right = 2*parent+2; //right points to right child
    pos = left;
    if((left<last)&&(A[left]<A[right]))  //compare left and right children
pos = right;
     if((pos<=last)&&(A[parent]<A[pos]))
     {
       temp = A[parent];
       A[parent] = A[pos];
       A[pos] = temp;
       Heapify(A,pos,last);
    }
}
void BuildHeap(int A[], int n)
{
   // converts A[0]..A[n-1] into a heap
int parent;
for(parent=n/2-1; parent>=0; parent--) /* parent nodes are at positions n/2 .. 0 */
  Heapify(A,parent,n-1);
}
void HeapSort(int A[], int n)
{
   // sorts A[0]..A[n-1] in the ascending order
  int i, temp, root=0, last=n-1, pass; 
  BuildHeap(A,n);
  printf("Initial heap = ");
  display(A,n);
  for(pass=1; pass<=n-1; pass++)
  {
    temp = A[root];
    A[root] = A[last];
    A[last] = temp;
    printf("\nAfter Iteration %d :", n-last);
    display(A,n);
    last--;
    Heapify(A,root,last);
  }
}

void generate(int A[],int n)
{
    srand(time(0));
    for(int i=0;i<n;i++)
    {
        A[i]=rand()%100;
    }
}

int main()
{
int A[20],n;
printf("enter the number of elements:\n");
scanf("%d",&n);
generate(A,n);
printf("the unsorted elements are:\n");
display(A,n);
HeapSort(A,n);
printf("\nThe sorted elements are : ");
display(A,n);
return 0;
}