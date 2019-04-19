#include "astar.h"



void readBinary(void){

    FILE *fin;

if ((fin = fopen ("file.bin", "rb")) == NULL) printf("the data file does not exist \n");

/* Global data --- header */

if( fread(&nnodes, sizeof(unsigned long), 1, fin) + fread(&ntotnsucc, sizeof(unsigned long), 1, fin) + fread(&nametotlen, sizeof(unsigned long), 1, fin) != 3 ) printf("Error when reading the header of the binary data file\n");

/* Allocate memory for all data */

if((idvector = malloc(nnodes*sizeof(unsigned long))) == NULL) printf("1\n");
if((nodelat = malloc(nnodes*sizeof(double))) == NULL) printf("2\n");
if((nodelon = malloc(nnodes*sizeof(double))) == NULL) printf("3\n");
if((nsuccdim = malloc(nnodes*sizeof(unsigned short))) == NULL) printf("4\n");
if((namelenvector = malloc(nnodes*sizeof(unsigned long))) == NULL) printf("5\n");
if((namevector = malloc(nametotlen*sizeof(char))) == NULL) printf("6\n");
if((nodes = malloc(nnodes*sizeof(node))) == NULL) printf("7\n");
if((allsuccessors = malloc(ntotnsucc*sizeof(unsigned long))) == NULL) printf("when allocating memory for the edges vector\n");

/*reading all data*/

if(fread(idvector, sizeof(unsigned long), nnodes, fin) != nnodes) printf("idvector\n");

if(fread(nodelat, sizeof(double), nnodes, fin) != nnodes) printf("nodelat\n");

if(fread(nodelon, sizeof(double), nnodes, fin) != nnodes) printf("nodelon\n");

if(fread(nsuccdim, sizeof(unsigned short), nnodes, fin) != nnodes) printf("nsuccdim\n");

if(fread(namelenvector, sizeof(unsigned long), nnodes, fin) != nnodes) printf("error namelenvector\n");

if(fread(namevector, sizeof(char), nametotlen, fin) != nametotlen) printf("namevector\n");

if(fread(allsuccessors, sizeof(unsigned long), ntotnsucc, fin) != ntotnsucc ) printf("when reading sucessors from the binary data file\n");

fclose(fin);

/* Allocating memory for node structures and filling in the values, successors, names*/

nodes = malloc(nnodes*sizeof(node));

unsigned long i, k;
unsigned long ii = 0 , kk = 0;

for(i=0; i < nnodes; i++) {
    nodes[i].id = idvector[i];
    nodes[i].lat = nodelat[i];
    nodes[i].lon = nodelon[i];
    nodes[i].nsucc = nsuccdim[i];
}

for(i=0; i<nnodes; i++){
    unsigned long a=namelenvector[i];
    unsigned long b=nsuccdim[i];
    nodes[i].name = malloc(a*sizeof(char));
    nodes[i].successors = malloc(b*sizeof(unsigned long));
}
for(i=0; i < nnodes; i++){
    if(nodes[i].nsucc>0) {
        for(k=0; k<nodes[i].nsucc; k++){
            nodes[i].successors[k] = allsuccessors[kk+k];
        }
        kk = kk+nodes[i].nsucc;
        }
    else continue;
}

for(i=0; i < nnodes; i++) if(namelenvector[i]>0) {
    for(k=0; k<namelenvector[i]; k++){
        nodes[i].name[k] = namevector[ii+k];
    }
    ii= ii + namelenvector[i];
}

}

int main()
{
    unsigned long startId, endId, strt, gl, i;
    double final_result;
    printf("Reading binary file...\n\n\n");
    readBinary();
    printf("End of reading Binary File.\n");
    printf("Please enter start node:");
    scanf("%lu",&startId);
    printf("\n");
    printf("Please enter end node:");
    scanf("%lu",&endId);
    printf("\n");
    printf("Initializing A*...\n\n");
    strt = binarysearch(startId, nodes, nnodes);
    gl = binarysearch(endId, nodes, nnodes);
    final_result = AStarAlgorithm(strt, gl);
    printf("Ultimate Final Resulting Distance = %lf meters.\n", final_result);

/*writing down the path backwards in a vector and then rearranging it to be from start to end in a vector*/
    unsigned long b, a = gl;
    unsigned long l = 1;
    unsigned long *v1, *v2;
    v1 = malloc(2*sizeof(unsigned long));

    while (a != strt){
        v1=realloc(v1, (l)*sizeof(unsigned long));
        v1[l-1] = a;
        b = nodes[a].stat.parent;
        a = b;
        l=l+1;
       }
    v1=realloc(v1, (l)*sizeof(unsigned long));
    v1[l-1] = strt;

    v2 = malloc((l)*sizeof(unsigned long));
    for (i=0;i<l; i++) v2[i] = v1[l-i-1];

/* Writing correct path to .txt file*/
    FILE *text;
    text = fopen("path.txt", "w");
    fprintf(text, "Optimal path found:\n");
    for (i=0;i<l; i++)fprintf(text,"Node id: %lu  | Distance: %lf  | Name: %s\n", nodes[v2[i]].id, nodes[v2[i]].stat.g, nodes[v2[i]].name);
    fclose(text);

    return 0;
}
