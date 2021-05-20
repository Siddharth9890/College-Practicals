#include<stdio.h>
#include"binarytree.h"

void main()
{
    int choice,num;
    node *root,temp;
    root=NULL;
    do
    {
        printf("\n1.Create:\n");
        printf("2.Search:\n");
        printf("3.Insert:\n");
        printf("4.Inorder Traversal:\n");
        printf("5.Preorder Traversal:\n");
        printf("6.Postorder Traversal:\n");
        printf("7.Exit:\n");
        printf("enter your choice\n");
        scanf("%d",&choice);
        switch(choice)
        {
            case 1:
                root=createbst(root);
                break;

            case 2:
                printf("enter the element to be searched:\n");
                scanf("%d",&num);
                node *temp=search(root,num);
                if(temp==NULL)
                    printf("element not found\n");
                else
                    printf("element found\n");

                break;

            case 3:
                printf("enter the element to be inserted");
                scanf("%d",&num);
                root=insert(root,num);

                break;

            case 4:
                printf("\nInorder:\n");
                inorder(root);
                break;

            case 5:
                printf("\nPreorder:\n");
                preorder(root);
                break;

            case 6:
                printf("\nPostorder:\n");
                postorder(root);
                break;

        }
    }while(choice!=7);
}
