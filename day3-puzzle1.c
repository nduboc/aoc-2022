#include <stdio.h>
#include <stdlib.h>
#include <errno.h>
#include <string.h>

#define PATH "day3-input.txt"

int prio(char c) {
    if (c >= 'a') {
        return c - 'a' + 1;
    } else {
        return c - 'A' + 27;
    }
}

int main() {
    printf("--- TEST PRIO ----\n");
    printf("prio(a) = %d, expect 1\n", prio('a'));
    printf("prio(b) = %d, expect 2\n", prio('b'));
    printf("prio(z) = %d, expect 26\n", prio('z'));
    printf("prio(A) = %d, expect 27\n", prio('A'));
    printf("prio(Z) = %d, expect 52\n", prio('Z'));
    printf("--- TEST END  ----\n");

    FILE* f = fopen(PATH, "r");
    if (f == NULL) {
        printf("error: %s: %s\n", PATH, strerror(errno));
        return 1;
    }
    
    char line[100];
    int ln = 0;
    int sum = 0;
    while (fscanf(f, "%s", &line[0]) != EOF) {
        ln += 1;
        int len = strlen(line);
        if (len % 2 != 0) {
            printf("error: odd number of chars on line %d\n", ln);
            return 1;
        }

        int found = 0;
        for (int i = 0; i < len/2 && !found; i++) {
            for (int j = len/2; j < len && !found; j++) {
                if (line[i] == line[j]) {
                    printf("line %d: %c, index %i\n", ln, line[i], i);
                    found = 1;
                    sum += prio(line[i]);
                }
            }
        }
    }

    printf("%d, confirmed 7889\n", sum);
}