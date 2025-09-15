#include <stdio.h>
int rear=-1;
int front=-1;
 int queue[10];
void enqueue(int n){
    if(rear==10-1){
        printf("queue is full");
    }
    else if(front==-1&&rear==-1){
        front=0;
        rear=0;
        queue[rear]=n;
    }
    else {
        
        rear++;
        queue[rear]=n;
        
    }
}

void dequeue(){
    int n;
    if(front==-1&&rear==-1){
        printf("queue is empty");
    }
    else{
        n=queue[front];
        printf("Deleted element is %d \n",n);
        front++;
    }
}
void peek(){
    if(front==-1&&rear==-1){
        printf("queue is empty");
    }
    else{
        printf("The top element is %d \n",queue[rear]);
    }

}
void display(){
    int i;
    if(front==-1&&rear==-1){
        printf("queue is empty");
    }
    else{
    printf("The elements are:");
    for(i=front;i<=rear;i++){
        printf("%d\n",queue[i]);
    }
  }
}


int main(){
    int num,value;
    printf("choose \n 1 for enqueue \n 2 for dequeue\n 3 for peek\n 4 for display queue\n 5 To exit\n");
    while(1){
    printf("enter the operation number =");
    scanf("%d",&num);
    
    switch(num){
        case 1:
        printf("enter the number to be inserted =");
        scanf("%d",&value);
        enqueue(value);
        display();
        break;
        case 2:
        dequeue();
        break;
        case 3:
        peek();
        break;
        case 4:
        display();
        break;
        case 5:
        printf("The program has been existed\n");
        return 0;
        default:
        printf("invalid operation num\n");
    }
}
return 0;
}
