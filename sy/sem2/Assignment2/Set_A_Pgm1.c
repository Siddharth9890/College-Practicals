#include<stdio.h>
#include"binarytree.h"

void main()
{
    node *root=NULL;
    root=createbst(root);

    printf("Level Order :\n");
    levelorder(root);
}
