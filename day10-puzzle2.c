#include <stdio.h>
#include <strings.h>
#include <errno.h>
#include <stdlib.h>

#define INPUT_FILE "day10-input.txt"

int main() {
    FILE* f = fopen(INPUT_FILE, "r");
    if (f == NULL) {
        printf("error: %s: %s\n", INPUT_FILE, strerror(errno));
        return 1;
    }
    
    char line[100];
    int ln = 0;
    int x = 1;
    int cycle = 0;
    int add_cycles = 0;
    int add_operand = 0;

    for (;;) {
        cycle++;

        int pixel = (cycle -1)%40;
        if (pixel >= x-1 && pixel <= x+1) {
            putchar('#');
        } else {
            putchar('.');
        }
        if (cycle % 40 == 0) {
            putchar('\n');
        }


        if (add_cycles > 0) {
            if (add_cycles == 1) {
                x += add_operand;
            }
            
            add_cycles--;
        } else {

        if (feof(f)) {
            break;
        }

        fscanf(f, "%[^\n]", &line[0]);
        fgetc(f); // read newline char
        line[4] = 0; // works because addx and noop are the only instructions

        if (strcmp("addx", line) == 0) {
            add_operand = atoi(&line[5]);
            add_cycles = 1; // 1 cycle remaining for add
        } else if (strcmp("noop", line)==0) {
            // do nothing
        } else {
            printf("ERROR, unknown instr %s\n", line);
            return 1;
        }
        }

    }
    printf("Confirmed result EGJBGCFK\n");
}