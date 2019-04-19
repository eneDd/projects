#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stddef.h>
#include <stdint.h>
#include <limits.h>
#include <math.h>
#include <time.h>

    unsigned long nnodes, ntotnsucc, nametotlen;
    unsigned long *allsuccessors, *idvector, *namelenvector;
    unsigned short *nsuccdim;
    double *nodelat, *nodelon;
    char *namevector;

    typedef enum whichQueue {NONE, OPEN, CLOSED} Queue;
    typedef struct
    {
    double g, h, f;
    unsigned long parent;
    Queue wqh;
    }AStarStatus;

    typedef struct node
    {
    unsigned long id; // Node identification
    char *name;
    double lat, lon; // Node position
    unsigned short nsucc; // Node successors: wighted edges
    unsigned long *successors;
    AStarStatus stat;
    }node;

    node *nodes;
