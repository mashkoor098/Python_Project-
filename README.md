# OS Practicals-
This repository is created on 21 Oct 2021
## Prac 1
## Study of pthread and implementation of multi threading

#include<stdio.h>
#include<pthread.h>
void *threadFunc(void *arg)
{
char *str;
int i = 0;
str=(char*)arg;
while(i < 10 )
{
usleep(1);
printf("threadFunc says: %s\n",str);
++i;
}
return NULL;
}

void *threadFunc1(void *arg)
{
char *str;
int i = 0;
str=(char*)arg;
while(i < 10 )
{
usleep(1);
printf("threadFunc says: %s\n",str);
++i;
}
return NULL;
}
int main(void)
{
pthread_t pth; // this is our thread identifier
int i = 0;
pthread_create(&pth,NULL,threadFunc,"SE Computer");
pthread_create(&pth,NULL,threadFunc1,"KCE COEIT");
while(i < 10)
{
usleep(1);
printf("main is running...\n");
++i;
}
printf("main waiting for thread to terminate...\n");
pthread_join(pth,NULL);
return 0;
}

#______________________________________________________________________
## Prac 2
# Implementation of CPU Scheduling Algorithm : FCFS

#include<stdio.h>
int main()
{
 int n,bt[20],wt[20],tat[20],avwt=0,avtat=0,i,j;
 printf("Enter total number of processes(maximum 20):");
 scanf("%d",&n);
 printf("\nEnter Process Burst Time\n");
 for(i=0;i<n;i++)
 {
 printf("P[%d]:",i+1);
 scanf("%d",&bt[i]);
 }
 wt[0]=0; //waiting time for first process is 0
 //calculating waiting time
 for(i=1;i<n;i++)
 {
 wt[i]=0;
 for(j=0;j<i;j++)
 wt[i]+=bt[j];
 }
 printf("\nProcess\t\tBurst Time\tWaiting Time\tTurnaround Time");
 //calculating turnaround time
 for(i=0;i<n;i++)
 {
 tat[i]=bt[i]+wt[i];
 avwt+=wt[i];
 avtat+=tat[i];
 printf("\nP[%d]\t\t%d\t\t%d\t\t%d",i+1,bt[i],wt[i],tat[i]);
 }
 avwt/=i;
 avtat/=i;
 printf("\n\nAverage Waiting Time:%d",avwt);
 printf("\nAverage Turnaround Time:%d",avtat);
 return 0;
}

#______________________________________________________________________

## Prac 3

# Implementation of Producer Consumer Problem Using Semaphore

#include<stdio.h>
#include<stdlib.h>
int mutex=1,full=0,empty=3,x=0;
int main()
{
int n;
void producer();
void consumer();
int wait(int);
int signal(int);
printf("\n1.Producer\n2.Consumer\n3.Exit");
while(1)
{
printf("\nEnter your choice:");
scanf("%d",&n);
switch(n)
{
case 1:if((mutex==1)&&(empty!=0))
producer();
else
printf("Buffer is full!!");
break;
case 2:if((mutex==1)&&(full!=0))
consumer();
else
printf("Buffer is empty!!");
break;
case 3:
exit(0);
break;
}
}
return 0;
}
int wait(int s)
{
return (--s);
}
int signal(int s)
{
return(++s);
}
void producer()
{
mutex=wait(mutex);
full=signal(full);
empty=wait(empty);
x++;
printf("\nProducer produces the item %d",x);
mutex=signal(mutex);
}
void consumer()
{
mutex=wait(mutex);
full=wait(full);
empty=signal(empty);
printf("\nConsumer consumes item %d",x);
x--;
mutex=signal(mutex);
}

#______________________________________________________________________

## Prac 4
# Aim: Implementation of Memory Management Algorithm: First Fit Memory 
Allocation.



#include<stdio.h>

void main()

{

int bsize[10], psize[10], bno, pno, flags[10], allocation[10], i, j;

for(i = 0; i < 10; i++)

{
flags[i] = 0;
allocation[i] = -1;
}
printf("Enter no. of blocks: ");
scanf("%d", &bno);
printf("\nEnter size of each block: ");
for(i = 0; i < bno; i++)
scanf("%d", &bsize[i]);
printf("\nEnter no. of processes: ");
scanf("%d", &pno);
printf("\nEnter size of each process: ");
for(i = 0; i < pno; i++)
scanf("%d", &psize[i]);
for(i = 0; i < pno; i++) //allocation as per first fit
for(j = 0; j < bno; j++)
if(flags[j] == 0 && bsize[j] >= psize[i])
{
allocation[j] = i;
flags[j] = 1;
break;
}
//display allocation details
printf("\nBlock no.\tsize\t\tprocess no.\t\tsize");
for(i = 0; i < bno; i++)
{
printf("\n%d\t\t%d\t\t", i+1, bsize[i]);
if(flags[i] == 1)
printf("%d\t\t\t%d",allocation[i]+1,psize[allocation[i]]);
else
printf("Not allocated");
}
}


#______________________________________________________________________
## Prac 5

# Aim: Implementation of Merge Sort.

#include<stdio.h>
void mergesort(int a[],int i,int j);
void merge(int a[],int i1,int j1,int i2,int j2);
int main()
{
int a[30],n,i;
printf("Enter no of elements:");
scanf("%d",&n);
printf("Enter array elements:");
for(i=0;i<n;i++)
scanf("%d",&a[i]);
mergesort(a,0,n-1);
printf("\nSorted array is :");
for(i=0;i<n;i++)
printf("%d ",a[i]);
return 0;
}
void mergesort(int a[],int i,int j)
{
int mid;
if(i<j)
{
mid=(i+j)/2;
mergesort(a,i,mid); //left recursion
mergesort(a,mid+1,j); //right recursion
merge(a,i,mid,mid+1,j); //merging of two sorted sub-arrays
}
}
void merge(int a[],int i1,int j1,int i2,int j2)
{
int temp[50]; //array used for merging
int i,j,k;
i=i1; //beginning of the first list
j=i2; //beginning of the second list
k=0;
while(i<=j1 && j<=j2) //while elements in both lists
{
if(a[i]<a[j])
temp[k++]=a[i++];
else
temp[k++]=a[j++];
}
while(i<=j1) //copy remaining elements of the first list
temp[k++]=a[i++];
while(j<=j2) //copy remaining elements of the second list
temp[k++]=a[j++];
//Transfer elements from temp[] back to a[]
for(i=i1,j=0;i<=j2;i++,j++)
a[i]=temp[j];
}

