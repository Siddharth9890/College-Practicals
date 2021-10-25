#include<stdio.h>
#include"binarytree.h"

void main()
{
    node *root1=NULL;
    node *root2=NULL;

    root1=createbst(root1);
    root2=treecopy(root1);

    int comp=compare(root1,root2);
    if(comp==0)
        printf("the two trees are not equal");
    else
        printf("the two trees are equal");


}
