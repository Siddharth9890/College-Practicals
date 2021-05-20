#include<stdio.h>
#include<stdlib.h>

typedef struct node
{
    int info;
    struct node *left,*right;
}node;

node * createbst(node *root)
{
    node *newnode,*temp,*parent;
    int i,num,n;
    printf("how many nodes:\n");
    scanf("%d",&n);
    for(i=1;i<=n;i++)
    {
        newnode=(node *)malloc(sizeof(node));
        printf("Enter the element:\n");
        scanf("%d",&num);
        newnode->info=num;
        newnode->left=newnode->right=NULL;

        if(root==NULL)
        {
            root=newnode;
            continue;
        }

        temp=root;
        while(temp!=NULL)
        {
            parent=temp;
            if(num<temp->info)
                temp=temp->left;
            else
                temp=temp->right;
        }
        if(num<parent->info)
            parent->left=newnode;
        else
            parent->right=newnode;
    }
    return(root);
}

node *search(node *root,int key)
{
    node *temp=root;
    while(temp!=NULL)
    {
        if(key==temp->info)
            return temp;
        if(key<temp->info)
            temp=temp->left;
        else
        temp=temp->right;
    }
    return NULL;
}
node *insert(node *root,int num)
{
    node *newnode,*temp=root,*parent;
    newnode=(node*)malloc(sizeof(node));
    newnode->info=num;
    newnode->left=newnode->right=NULL;
    if(root==NULL)
    {
        root=newnode;
        return root;
    }
    while(temp!=NULL)
    {
        parent=temp;
        if(num<temp->info)
            temp=temp->left;
        else
            temp=temp->right;
    }
    if(num<parent->info)
        parent->left=newnode;
    else
        parent->right=newnode;
    return root;
}

void preorder(node *root) //DLR
{
    node *temp=root;
    if(temp!=NULL)
   {
       printf("%d ",temp->info);
       preorder(temp->left);
       preorder(temp->right);
   }
}

void inorder(node *root) //LDR
{
    node *temp=root;
    if(temp!=NULL)
   {
       inorder(temp->left);
       printf("%d ",temp->info);
       inorder(temp->right);
   }
}

void postorder(node *root) //LRD
{
    node *temp=root;
    if(temp!=NULL)
   {
       postorder(temp->left);
       postorder(temp->right);
       printf("%d ",temp->info);
   }
}



int countnode(node *root)
{
    static int count=0;
    node *temp=root;
    if(temp!=NULL)
    {
        count++;
        countnode(temp->left);
        countnode(temp->right);
    }
    return count;
}

int countleaf(node *root)
{
    static int leaf=0;
    node *temp=root;
    if(temp!=NULL)
    {
        if((temp->left==NULL) && (temp->right==NULL))
            leaf++;
        countleaf(temp->left);
        countleaf(temp->right);
    }
    return leaf;
}

node *treecopy(node *root) {
    node *newnode;
    if (root != NULL) {
        newnode = (node *) malloc(sizeof(node));
        newnode->info = root->info;
        newnode->left = treecopy(root->left);
        newnode->right = treecopy(root->right);
        return(newnode);
    }
    else
        return NULL;
}

int compare(node *root1 ,node *root2)
{
    if(root1==NULL && root2==NULL)
    {
        return 1;
    }else{
        if(root1!=NULL && root2!=NULL)
        {
            if(root1->info==root2->info)
            {
                if(compare(root1->left,root2->left))
                    return compare(root1->right,root2->right);
            }
        }
        return 0;
    }
}
#define maxsize 100
typedef struct queue
{
    node *data[maxsize-1];
    int front,rear;
}queue;

void initq(queue *pq)
{
    pq->front=pq->rear=-1;
}

void addq(queue *pq,node *ptr)
{
    pq->data[++pq->rear]=ptr;
}

node * removeq(queue *pq)
{
    return pq->data[++pq->front];
}

int isempty(queue *pq)
{
    return pq->front==pq->rear;
}

void levelorder(node *root)
{
    int i,level=0,count=0;
    node *marker=NULL;
    node *temp;
    queue q;
    initq(&q);
    addq(&q,root);
    addq(&q,marker);
    printf("\nLevel %d :",level);
    while(!isempty(&q))
    {
        temp=removeq(&q);
        if(temp==marker)
        {
            printf("\ntotal number of node at level %d is %d",level,count);
            if(!isempty(&q))
           {

            level++;
            addq(&q,marker);
            printf("\nLevel %d :",level);
            count=0;
           }
        }
        else
        {
            printf("%d ",temp->info);
            count ++;
            if(temp->left!=NULL)
                addq(&q,temp->left);
            if(temp->right!=NULL)
                addq(&q,temp->right);
        }
    }
    printf("\ntotal number of levels: %d",level+1);
}