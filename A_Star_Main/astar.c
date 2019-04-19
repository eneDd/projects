#include "astar.h"

// Functions 

 unsigned long lowestfID(unsigned long olistvalue, unsigned long *oplist){
    unsigned long i, id;
    id = oplist[0];
    for(i=0; i<olistvalue; i++){
        if ((nodes[oplist[i]].stat.g + nodes[oplist[i]].stat.h) < (nodes[id].stat.g + nodes[id].stat.h)) id = oplist[i];
    }
    return id;
}


unsigned long binarysearch(unsigned long key, node *list, unsigned long listlen){

    register unsigned long start=0UL, afterend=listlen, middle;
    register unsigned long try;
    while(afterend > start){
        middle = start + ((afterend-start-1)>>1);
        try = list[middle].id;
        if (key == try) return middle;
        else if ( key > try ) start=middle+1;
        else afterend=middle;
    }
    return ULONG_MAX;
}

/*  Distance
 *
 *  Since we are on the geoid surface, we will use the great circle distance. In
 *  particular, i use the haversine formula. 
 *
 *
 *  Return: d approximate distance.
 */


//Haversine Distance

double distance(double latst, double latend, double lonst, double lonend){
    double R = 6371000;
    double x = latend-latst;
    double y = lonend-lonst;
    double a = sin(x*M_PI/(180*2)) * sin(x*M_PI/(180*2)) + cos(latend*M_PI/180)*cos(latst*M_PI/180)*sin(y*M_PI/(180*2))*sin(y*M_PI/(180*2));
    double c = 2*atan2(sqrt(a),sqrt(1-a));
    double d = R*c;
    return d;
}

 double calculateDist(unsigned long crnt, unsigned long succ){
    double dist;
    double lat1 = nodes[crnt].lat;
    double lat2 = nodes[succ].lat;
    double lon1 = nodes[crnt].lon;
    double lon2 = nodes[succ].lon;
    dist = distance(lat1, lat2, lon1, lon2);
    return dist;
}

//Heuristic Distance

double calculateHeuristic(unsigned long curr, unsigned long goal){
    double dist;
    double lat1 = nodes[curr].lat;
    double lat2 = nodes[goal].lat;
    double lon1 = nodes[curr].lon;
    double lon2 = nodes[goal].lon;
    dist = distance(lat1, lat2, lon1, lon2);
    return dist;
}


double AStarAlgorithm(unsigned long startnode, unsigned long endnode){

double succcost;
unsigned long openlistvalue=1;
unsigned long closedlistvalue = 0;
unsigned long current, currentsuccessor;
unsigned long *openlist, *closedlist;

openlist = malloc(1*sizeof(unsigned long));
closedlist = malloc(1*sizeof(unsigned long));

openlist[0] = startnode;
nodes[startnode].stat.g = 0;
nodes[startnode].stat.h = calculateHeuristic(startnode, endnode);
nodes[startnode].stat.parent = startnode;


while(openlistvalue>0){
unsigned long i;
unsigned long k =0;
current = lowestfID(openlistvalue, openlist);

// Main Loop

while (current!= openlist[k]){
    k++;
}
for (i=k; i<openlistvalue; i++) openlist[i] = openlist[i+1];
openlistvalue = openlistvalue-1;
nodes[current].stat.wqh = CLOSED;

if(nodes[current].id == nodes[endnode].id) break;

    for(i=0; i<nodes[current].nsucc; i++){

        currentsuccessor = nodes[current].successors[i];
        succcost = nodes[current].stat.g + calculateDist(current, currentsuccessor);

        if((nodes[currentsuccessor].stat.wqh == OPEN) && (nodes[currentsuccessor].stat.g <= succcost)) {
                continue;
        }
        else if((nodes[currentsuccessor].stat.wqh == OPEN) && (nodes[currentsuccessor].stat.g > succcost)){
            nodes[currentsuccessor].stat.g = succcost;
            nodes[currentsuccessor].stat.parent = current;

        }
        else if((nodes[currentsuccessor].stat.wqh == CLOSED) && (nodes[currentsuccessor].stat.g <= succcost)) {
                continue;
        }
        else if((nodes[currentsuccessor].stat.wqh == CLOSED) && (nodes[currentsuccessor].stat.g > succcost)){
            nodes[currentsuccessor].stat.wqh = OPEN;
            nodes[currentsuccessor].stat.g = succcost;
            nodes[currentsuccessor].stat.h = calculateHeuristic(currentsuccessor, endnode);
            nodes[currentsuccessor].stat.parent = current;
            int a,w=0;
            while (currentsuccessor!=closedlist[w]){
                w++;
            }
            for(a=w; a<closedlistvalue; a++) closedlist[a] = closedlist[a+1];
            closedlistvalue=closedlistvalue-1;

            openlist = realloc(openlist, (openlistvalue+1)*sizeof(unsigned long));
            openlist[openlistvalue] = currentsuccessor;
            openlistvalue = openlistvalue+1;
        }
        else{

            openlist = realloc(openlist, (openlistvalue+1)*sizeof(unsigned long));
            openlist[openlistvalue] = currentsuccessor;
            openlistvalue = openlistvalue+1;

            nodes[currentsuccessor].stat.wqh = OPEN;
            nodes[currentsuccessor].stat.g = succcost;
            nodes[currentsuccessor].stat.h = calculateHeuristic(currentsuccessor, endnode);
            nodes[currentsuccessor].stat.parent = current;
        }
    }

    nodes[current].stat.wqh = CLOSED;
    closedlist = realloc(closedlist, (closedlistvalue+1)*sizeof(unsigned long));
    closedlist[closedlistvalue] = current;
    closedlistvalue = closedlistvalue+1;

}
if (nodes[current].id != nodes[endnode].id){
    printf("OPEN LIST EMPTY, ERROR\n");
    return 0;
}
else return nodes[current].stat.g;

}
