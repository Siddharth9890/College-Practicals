#include<stdio.h>
#include"binarytree.h"

void main()
{
    node *root=NULL;
    root=createbst(root);

    printf("\nthe total number of nodes in the binary search tree is %d",countnode(root));

    printf("\nthe total number of leaf nodes in the binary search tree is %d",countleaf(root));
}
