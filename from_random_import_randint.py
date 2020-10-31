from random import randint

# un tirage contient 4 emplacements pour stocker la valeur de dés
# ici ils sont initialisés avec quatre 0
# qui signifient que les dés n'ont pas été encore tirés.

tirage_j1 = [0, 0, 0, 0]
tirage_j2 = [0, 0, 0, 0]

# 
def score(tirage):
    """Renvoie le score associé au tirage "tirage"."""
    return tirage[0] + tirage[1] + tirage[2] + tirage[3]


def afficher(tirage):
    """Affiche le tirage

    Affiche pour chaque dé de "tirage"
    son numéro (ou position) et sa valeur.
    La valeur 0 code un dé non tiré.
    """
# 
    de0=str(tirage[0])
    de1=str(tirage[1])
    de2=str(tirage[2])
    de3=str(tirage[3])
    print("Dé n°0: " +de0+ ", Dé n°1: " +de1+ ", Dé n°2: " +de2+ ", Dé n°3 " +de3)


# 
def tirer(tirage):
    """Effectue un tirage de 4 dés et modifie la liste "tirage". """
    for i in range (0,4) :
        tirage[i] = randint(1,6)
    return tirage


def test_score():
    """Teste la fonction score()

    On teste la fonction score avec le tirage 6, 5 ,4 ,3.
    Le score affiché dans la console doit être 6+5+4+3=18.
    """
    print("Test score")
    print(score([6, 5, 4, 3]))
    print("Fin Test score\n")


def test_afficher():
    """Teste la fonction afficher()

    On teste la fonction afficher avec le tirage 6, 5, 4, 3.
    On doit obtenir dans la console :
    Dé n°0 : 6 Dé n°1 : 5 Dé n°2 : 4 Dé n°3 : 3
    """
    print("Test afficher")
    afficher([6, 5, 4, 3])
    print("Fin Test afficher\n")


def test_tirer():
    """Teste la fonction tirage()
    
    On affiche ensuite le tirage dans la console puis son score.
    Le tirage étant aléatoire les résulats ne sont pas fixes.

    Exemple possible :
    Dé n°0 : 6 Dé n°1 : 5 Dé n°2 : 1 Dé n°3 : 6
    18
    """
    print("Test tirer")
    tirer(tirage_j1)
    afficher(tirage_j1)
    print(score(tirage_j1))
    print("Fin Test tirer\n")


def main():
    """Programme principal

    Habituellement, le programme principal est appelé main()
    Ici, pour chaque joueur,
    on effectue un tirage de 4 dés, on affiche ce tirage,
    on calcule le score.
    Puis on détermine lequel des deux joueurs a gagné.
    """
    print("### Debut du main ###")
    tirer(tirage_j1)
    afficher(tirage_j1)
    score_j1 = score(tirage_j1)
    print("\nLe score du joueur 1 est : " + str(score_j1) + ".")
    print("")

    tirer(tirage_j2)
    afficher(tirage_j2)
    score_j2 = score(tirage_j2)
    print("\nLe score du joueur 2 est : " + str(score_j2) + ".")
    print("")

    if score_j1 > score_j2:
        print("C'est le joueur 1 qui a gagné !")
    else:
        if score_j1 == score_j2:
            print("Match nul.")
        else:
            print("C'est le joueur 2 qui a gagné !")

    print("### Fin du main ###")


"""
# Début des appels de tests
# Décommenter les lignes des tests que vous voulez effectuer
"""

# test_score()
# test_afficher()
# test_tirer()

"""
# Appel de la fonction principale
# Décommenter la ligne main pour lancer le programme principal.
"""
main()