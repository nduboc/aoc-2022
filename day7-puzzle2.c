#include <stdio.h>
#include <stdlib.h>
#include <errno.h>
#include <string.h>
#include <limits.h>

#define INPUT_FILE "day7-input.txt"

typedef struct Dir {
    char *name;
    struct Dir *parent;
    long ownSize;
    struct Dir *subdirs;
    struct Dir *siblings;
} Dir;

Dir* new_dir(char* name, Dir* parent) {
    Dir *r = malloc(sizeof(Dir));
    r->name = malloc(strlen(name)); // no NULL check
    r->parent = parent;
    strcpy(r->name, name);
    r->ownSize = -1;
    r->subdirs = NULL;
    r->siblings = NULL;
    return r;
}

Dir *find_dir(char *name, Dir *siblings) {
    Dir *result = NULL;
    while (siblings != NULL) {
        if (strcmp(name, siblings->name) != 0) {
            siblings = siblings->siblings;
        }
    }
    return result;
}

void print_dir(Dir *dir, int indent) {
    for (int i = 0; i < indent; i++) {
        putchar(' '); putchar(' ');
    }
    printf("- %s (size %ld)\n", dir->name, dir->ownSize);
}

void print_tree(Dir *tree, int indent) {
    print_dir(tree, indent);
    for (Dir *subdir = tree->subdirs; subdir != NULL; subdir = subdir->siblings) {
        print_tree(subdir, indent+1);
    }
}

long compute_rec_sizes(Dir *tree, long minimum, long *result) {
    long recSize = tree->ownSize;
    for (Dir *subdir = tree->subdirs; subdir != NULL; subdir = subdir->siblings) {
        recSize += compute_rec_sizes(subdir, minimum, result);
    }
    if (recSize >= minimum && recSize < *result) {
        *result = recSize;
    }
    return recSize;
}

int main() {
    FILE* f = fopen(INPUT_FILE, "r");
    if (f == NULL) {
        printf("error: %s: %s\n", INPUT_FILE, strerror(errno));
        return 1;
    }
    
    char line[100];
    int reading_ls = 0; // 1 if we're reading the output of ls, 0 if we're at the prompt level
    int ln = 0;
    Dir *root = NULL;
    Dir *current = NULL;
    long total_size = 0;

    while (fscanf(f, "%[^\n]", &line[0]) != EOF) {
        fgetc(f); // read newline char
        ln++;

        if (reading_ls) {
            if (line[0] == '$') {
                reading_ls = 0;
            } else {
                if (line[0] != 'd') {
                    char *end;
                    long f_size = strtol(&line[0], &end, 10);
                    if (end == &line[0]) {
                        printf("ERROR: failed to read an int on line %d\n", ln);
                        return 1;
                    }
                    current->ownSize += f_size;
                    total_size += f_size;
                }
            }
        }

        if (!reading_ls) {
            if (line[0] != '$') {
                printf("ERROR: expected a $ on line %d\n", ln);
                return 1;
            }

            if (line[2] == 'c') {
                char *target = &line[5];

                if (target[0] == '/' && target[1] != 0) {
                    printf("ERROR: unexpected move to absolute dir %s\n", target);
                    return 1;
                }

                if (target[0] == '/' && root == NULL) {
                    root = new_dir("ROOT", NULL);
                    current = root;
                } else if (target[0] == '/') {
                    current = root;
                } else if (target[0] == '.' && target[1] == '.') {
                    current = current->parent;
                } else {
                    Dir* next = find_dir(target, current->subdirs);
                    if (next != NULL) {
                        current = next;
                    } else {
                        next = new_dir(&line[5], current);
                        next->siblings = current->subdirs;
                        current->subdirs = next;
                        current = next;
                    }
                }

            } else if (line[2] == 'l') {
                reading_ls = 1;
                if (current->ownSize != -1) {
                    printf("ERROR: double ls on dir %s, line %d\n", current->name, ln);
                    return 1;
                }
                current->ownSize = 0;
            }
        }
    }

    print_tree(root, 0);


    long total = 70000000L;
    printf("Root size: %ld\n", total_size); // 44376732
    long need_to_free = total_size - (70000000L - 30000000L);
    printf("Need to free: %ld\n", need_to_free);

    long result = LONG_MAX;
    long root_size = compute_rec_sizes(root, need_to_free, &result);
    
    printf("Result: %ld, confirmed: 4443914\n", result);
}