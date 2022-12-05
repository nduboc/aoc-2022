#include <stdio.h>
#include <stdlib.h>
#include <errno.h>
#include <string.h>

#define PATH "day5-input.txt"
// adjust NB_STACK for the input file:
#define NB_STACKS 9

void print_stacks(char (*stacks)[NB_STACKS][100], int (*stack_len)[NB_STACKS] ) {
    for (int i =0; i < NB_STACKS; i++) {
        printf("%d : ", i+1);
        for (int j = 0; j < (*stack_len)[i]; j++) {
            putchar((*stacks)[i][j]);
        }
        printf(" (%d)\n", (*stack_len)[i]);
    }
}

int main() {

    FILE* f = fopen(PATH, "r");
    if (f == NULL) {
        printf("error: %s: %s\n", PATH, strerror(errno));
        return 1;
    }
    
    char stacks[NB_STACKS][100];
    int stack_len[NB_STACKS] = {0};
    

    int ln = 0;
    char line[100];
    while (fscanf(f, "%[^\n]", &line[0]) != EOF) {
        fgetc(f); // read newline char
        ln += 1;
        int line_len = strlen(line);

        if (line[1] == '1') {
            break;
        }

        for (int i = 0; i < NB_STACKS; i++) {
            char crate = line[1 + i*4];  // assumes all lines have same length, filled with spaces
            if (crate != ' ') {
                stacks[i][stack_len[i]++] = crate;
            }
            // if stack_len[i] == 100 -> error
        }
    }
    // flip the stacks so that the base of the stack is at the start of the arrays
    for (int i = 0; i < NB_STACKS; i++) {
        char buf[100];
        strncpy(&buf[0], &stacks[i][0], stack_len[i]);
        for (int j = 0; j < stack_len[i]; j++) {
            stacks[i][j] = buf[stack_len[i]-j-1];
        }
        stacks[i][stack_len[i]]=0; // put a zero for printf ot the stacks below
    }

    print_stacks(&stacks, &stack_len);

    fgetc(f); // skip empty line
    ln += 1;

    int nbCrate, from, to;
    while (1) {
        int read = fscanf(f, "move %d from %d to %d\n", &nbCrate, &from, &to);
        ln += 1;
        if (read == EOF) {
            break;
        }
        if (read != 3) {
            printf("Not read 3 on line %d: %d\n", ln, read);
            break;
        }

        // stacks are indexed at 1 in file but at 0 in our array
        from --;
        to --;
        
        for (int i = nbCrate; i > 0; i--) {
            stacks[to][stack_len[to]++] = stacks[from][stack_len[from] - i];
        }
        stack_len[from] -= nbCrate;
    }

    printf("\n After all moves:\n");
    print_stacks(&stacks, &stack_len);

    printf("\nResult: ");
    for (int i = 0; i < NB_STACKS; i++) {
        // assuming no stack is empty...
        putchar(stacks[i][stack_len[i]-1]);
    }
    printf(", confirmed: MGDMPSZTM\n");
}