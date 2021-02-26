#include <stdio.h>
#include <stdlib.h>
typedef struct node
{
    int info;
    struct node *next, *prev;
} node;

void create(node *head)
{
    int n, count;
    node *last, *newnode;
    printf("How many nodes");
    scanf("%d", &n);
    last = head;
    for (count = 1; count <= n; count++)
    {
        newnode = (node *)malloc(sizeof(node));
        newnode->next = newnode->prev = NULL;
        printf("\n enter the node data");
        scanf("%d", &newnode->info);
        last->next = newnode;
        newnode->prev = last;
        last = newnode;
    }
}

void reverse(node *head)
{
    struct node *current, *temp;

    current = head;
    while(current != NULL)
    {
        temp = current->next;
        current->next = current->prev;
        current->prev = temp;
        current = temp;
    }
    
}

void display(node *head)
{
    node *temp;
    for (temp = head->next; temp != NULL; temp = temp->next)
    {
        printf("%d\n", temp->info);
    }
}