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

void clear_counts(int (*t)[128][3]) {
    for (int i = 0; i < 128; i++)
        for (int j = 0; j < 3; j++)
            (*t)[i][j] = 0;
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
    int counts[128][3]; // presence (0/1) for each character on each 3 lines of the group
    clear_counts(&counts);
    while (fscanf(f, "%s", &line[0]) != EOF) {
        ln += 1;
        for (int i = 0; line[i] != 0; i++) {
            counts[line[i]][(ln-1)%3] = 1;
        }
        
        if (ln % 3 == 0) {
            char badge_letter = -1;
            for (int i = 0; i < 128; i++) {
                if (counts[i][0] == 1 && counts[i][1] == 1 && counts[i][2] == 1) {
                    badge_letter = i;
                    break;
                }
            }
            if (badge_letter == -1) {
                printf("ERROR: no badge found on line %d\n", ln);
                return 1;
            }
            sum += prio(badge_letter);
            clear_counts(&counts);
        }
    }

    printf("%d, confirmed 2825\n", sum);
}