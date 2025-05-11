def analyse_phrase(phrase):
    # Initialisation des compteurs
    longueur = 0
    nb_mots = 1  # Il y a au moins un mot dans la phrase
    nb_voyelles = 0
    
    # Liste des voyelles
    voyelles = "aeiouAEIOU"
    
    # Parcourir chaque caractère de la phrase
    for caractere in phrase:
        longueur += 1  # Comptabiliser la longueur de la phrase
        
        # Comptabiliser le nombre de voyelles
        if caractere in voyelles:
            nb_voyelles += 1
        
        # Comptabiliser le nombre de mots (un mot commence après un espace)
        if caractere == ' ':
            nb_mots += 1
    
    # Affichage des résultats
    print(f"Longueur de la phrase : {longueur}")
    print(f"Nombre de mots : {nb_mots}")
    print(f"Nombre de voyelles : {nb_voyelles}")

# Exemple d'appel à la fonction
phrase = input("Entrez une phrase se terminant par un point : ")
analyse_phrase(phrase)