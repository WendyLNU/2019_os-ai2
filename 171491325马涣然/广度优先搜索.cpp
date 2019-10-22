#include<stdio.h>
#define OK 1
#define ERROR 0
#define TRUE 1
#define FALSE 0
#define MAXVEX 9
#define MAXSIZE 9
typedef int Status;
typedef int Boolean;
typedef int EdgeType;
struct Graph
{ char vexs[MAXVEX];
int arc[MAXVEX][MAXVEX];
int vexNum;
int arcNum;
};
typedef struct{
int data[MAXSIZE];
int front;
int rear;
}Queue;
void InitQueue(Queue *Q)
{Q->front=0;
Q->rear=0;
}
Status QueueEmpty(Queue Q)
{if(Q.front==Q.rear)
{return TRUE;}
return FALSE;
}
Status EnQueue(Queue *Q,int e)
{
if((Q->rear+1)%MAXSIZE==Q->front)
{ return ERROR;}
Q->data[Q->rear]=e;
Q->rear=(Q->rear+1)%MAXSIZE;
return OK;
}
Status DeQueue(Queue *Q,int *e)
{if(Q->front==Q->rear)
{return ERROR;
}
*e=Q->data[Q->front];
Q->front=(Q->front+1)%MAXSIZE;
return OK;
}
void CreateGraph(Graph *G)
{
G->arcNum=15;
G->vexNum=9;
G->vexs[0]='A';
G->vexs[1]='B';
G->vexs[2]='C';
G->vexs[3]='D';
G->vexs[4]='E';
G->vexs[5]='F';
G->vexs[6]='G';
G->vexs[7]='H';
G->vexs[8]='I';
int i,j;
for(i=0;i<G->vexNum;i++)
{for(j=0;j<G->vexNum;j++)
{G->arc[i][j]=0;
}
}
G->arc[0][1]=1;
G->arc[0][5]=1;
G->arc[1][2]=1;
G->arc[1][6]=1;
G->arc[1][8]=1;
G->arc[2][3]=1;
G->arc[2][8]=1;
G->arc[3][4]=1;
G->arc[3][6]=1;
G->arc[3][7]=1;
G->arc[3][8]=1;
G->arc[4][5]=1;
G->arc[4][7]=1;
G->arc[5][6]=1;
G->arc[6][7]=1;
for(i=0;i<G->vexNum;i++)
{for(j=i;j<G->vexNum;j++)
{ G->arc[j][i]=G->arc[i][j];
}
}
}
Boolean visited[MAXVEX];
void BFSTraverse(Graph G)
{int i,j;
Queue Q;
for(i=0;i<G.vexNum;i++)
{ visited[i]=FALSE;
}
InitQueue(&Q);
for(i=0;i<G.vexNum;i++)
{if(!visited[i])
{ visited[i]=TRUE;
printf("%c",G.vexs[i]);
EnQueue(&Q,i);
while(!QueueEmpty(Q))
{ DeQueue(&Q,&i);
for(j=0;j<G.vexNum;j++)
{
if(G.arc[i][j]==1&&!visited[j])
{visited[j]=TRUE;
printf("%c",G.vexs[j]);
EnQueue(&Q,j);
} } } } } }
int main()
{Graph graph;
CreateGraph(&graph);
printf("¹ã¶È±éÀú:");
BFSTraverse(graph);
printf("\n");
return 0;
}
