#include <stdio.h>
#include <stdlib.h>
#include <errno.h>
#include <string.h>

#define PATH "day4-input.txt"

int main() {

    FILE* f = fopen(PATH, "r");
    if (f == NULL) {
        printf("error: %s: %s\n", PATH, strerror(errno));
        return 1;
    }
    
    char line[100];
    int ln = 0;

    int start1, end1, start2, end2;
    int overlaps = 0;
    while (fscanf(f, "%d-%d,%d-%d", &start1, &end1, &start2, &end2) != EOF) {
        ln += 1;

        if (start2 <= end1 && end2 >= start1) { 
            overlaps++;
        }
    }


    printf("%d, confirmed 852\n", overlaps);
}

// .  5-7, 7-9
// .  6-9, 5-7