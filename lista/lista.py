

maior_idade=0

idades=[int(input("idade1:")),
        int(input("idade2:")),
        int(input("idade3:"))]

for idade in idades:

    if idade>maior_idade:
        maior_idade=idade

print("maior  idade: ", maior_idade)
