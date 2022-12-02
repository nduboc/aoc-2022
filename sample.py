

path="day1-input.txt"

nbLignes=0
with open(path) as fIn:
    while True:
        line = fIn.readline()

        if line == "":
            # on a atteint la fin du fichier
            print("EOF. nb lignes:", nbLignes)
            break
        elif line == "\n":
            # ligne vide
            print("# Ligne vide")
            nbLignes += 1
        else:
            print("Ligne: ", line[:-1])
            nbLignes += 1

