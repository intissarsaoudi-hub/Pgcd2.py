# Bonjour
# Mon programme est pour calculer le PGCD avec le langage Python
#la premiere chose que le programme:
# il va l'afficher a utilisateur combien de  nombre de couple veut calculer

def pgcd(a, b):
    print(f"\nCalcul du PGCD de {a} et {b} :")
    etape = 1
    while b != 0:
        q = a // b  # quotient
        r = a % b   # reste
        print(f"Étape {etape} : {a} = {b} × {q} + {r}")
        a, b = b, r
        etape += 1
    print(f"→ Le PGCD est {a}")
    return a


#Programme principal
nb_couples = int(input("Combien de couples de nombres souhaitez-vous calculer ? "))

for i in range(1, nb_couples + 1):
    print(f"\n--- Couple n°{i} ---")
    x = int(input("Entrez le premier nombre : "))
    y = int(input("Entrez le deuxième nombre : "))
    pgcd(x, y)

print("\n✅ Tous les calculs de PGCD sont terminés !")
