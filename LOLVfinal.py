import random

# Création de tous les dictionnaires nécessaires pour tout le programme(Objets, Champions, gain de niveaux)

Jax = {
    "Name": "Jax",
    "Level": 1,
    "Gold": 500,
    "Vie Max": 593,
    "Vie actuelle": 593,
    "Attaque": 68,
    "Armure": 36,
    "Mana Max": 338.8,
    "Mana actuel": 338.8,
    "Vitesse": 350,
    "NombreObjet": 0,
    "Inventaire": []
}

Olaf = {
    "Name": "Olaf",
    "Level": 1,
    "Gold": 500,
    "Vie Max": 597,
    "Vie actuelle": 597,
    "Attaque": 68,
    "Armure": 35,
    "Mana Max": 315.6,
    "Mana actuel": 152,
    "Vitesse": 350,
    "NombreObjet": 0,
    "Inventaire": []
}

Jax_LevelUp = {
    "Vie Max": 85,
    "Attaque": 3.38,
    "Armure": 3,
    "Mana Max": 52,
}

Olaf_LevelUp = {
    "Vie Max": 93,
    "Attaque": 3.5,
    "Armure": 3,
    "Mana Max": 42,
}

Lame_de_Doran = {
    "Name": "Lame de Doran",
    "Prix": 450,
    "Vie Max": 80,
    "Vie actuelle": 80,
    "Attaque": 8,
}

Coques_en_acier = {
    "Name": "Coques en acier",
    "Prix": 1100,
    "Armure": 20,
    "Vitesse de déplacement": 45,
}

Ange_Gardien = {
    "Name": "Ange Gardien",
    "Prix": 2800,
    "Armure": 40,
    "Attaque": 40,
}

Cotte_epineuse = {
    "Name": "Cotte épineuse",
    "Prix": 2700,
    "Vie Max": 350,
    "Armure": 60,
    "Vie actuelle": 350,
}

Potion = {
    "Name": "Potion",
    "Prix": 500,
    "Vie actuelle": 125,
    "Mana actuel": 75
}

# Question 2


def Afficher_Statistiques(Champion):
    """Description : Fonction permettant d'afficher les statistiques d'un champion.
       Paramètre : Champion - dictionnaire - In
       Précondition : Champion = dictionnaire
       Postcondition : Affiche les statistiques d'un champion"""

    print("Statistiques de", Champion["Name"], ":")
    print("Niveau", Champion["Level"])
    print("Or =", Champion["Gold"])
    print("Vie Maximale =", Champion["Vie Max"])
    print("Vie actuelle =", Champion["Vie actuelle"])
    print("Attaque =", Champion["Attaque"])
    print("Armure =", Champion["Armure"])
    print("Mana max =", Champion["Mana Max"])
    print("Mana actuel =", Champion["Mana actuel"])
    print("Vitesse de déplacment =", Champion["Vitesse"])
    print("Nombre d'objet du champion =", Champion["NombreObjet"])
    print("Inventaire =", Champion["Inventaire"], "\n")

# Tous les print permettent l'affichage de chaque caractéristique du champion.


# Question 3
def Augmenter_PO(Champion):
    """Description : Fonction permettant de faire gagner des Gold à un champion lorsqu'il élimine un sbire.
       Paramètre : Champion - dictionnaire - In
       Précondition : Champion = dictionnaire
       Postcondition : Affiche le nombre de Gold d'un champion après l'élimination d'un sbire"""

    nb_sbire = random.randint(5, 10)  # Nombre aléatoire de sbire tués
    # Nombre aléatoire de pièces gagnées par sbire
    gold_sbire = random.randint(125, 195)
    # Ajout du nombre de gold gagné au champion par rapport à ses éliminations.
    Champion["Gold"] += gold_sbire*nb_sbire
    print(Champion["Name"], "a maintenant", Champion["Gold"], "gold.")
    # affichage de son nouveau nombre de gold.

# Question 4


def Utiliser_Potion(Champion):
    """Description : Fonction permettant d'utiliser une potion augmentant le mana actuel et le vie actuelle d'un champion.
       Paramètres : Champion - dictionnaire - In
                   InventaireChampion - dictionnaire - In
       Préconditions : Champion = dictionnaire
                       InventaireChampion = dictionnaire
       Postconditions : Augmente la vie actuelle et le mana d'un champion
    """
    reponse = False
    if Potion["Name"] in Champion["Inventaire"]:
        while reponse == False:
            acceptation = input("Voulez-vous utiliser la potion ? ( oui ou non ) :")
            if acceptation == "oui":
                reponse = True
                Champion["Inventaire"].remove(Potion["Name"])
                Champion["NombreObjet"] -= 1
                if Champion["Vie actuelle"] + Potion["Vie actuelle"] > Champion["Vie Max"]:
                    Champion["Vie actuelle"] = Champion["Vie Max"]
                    # if permettant de bloquer le nombre de points de vie du champion à sa vie max si la potion plus sa vie actuelle depasse sa vie max et de print un petit message d'alerte
                    print(Champion["Name"], "a dépassé ses pv maximum en utilisant sa potion, donc ses pv sont définis au maximum soit", Champion["Vie Max"], "pv")
                    
                else:
                    Champion["Vie actuelle"] += Potion["Vie actuelle"]
                    print(Champion["Name"], "a maintenant",
                        Champion["Vie Max"], "pv")
                    # else permettant l'effet de la potion sur le Champion.

                if Champion["Mana actuel"] + Potion["Mana actuel"] > Champion["Mana Max"]:
                    Champion["Mana actuel"] = Champion["Mana Max"]
                    # if permettant de faire le meme principe que pour la vie mais pour le mana cette fois-ci.
                    print(Champion["Name"], "a dépassé son mana maximum en utilisant sa potion, donc son mana est défini au maximum soit",Champion["Mana Max"], "de mana\n")
                else:
                    Champion["Mana actuel"] += Potion["Mana actuel"]
                    print(Champion["Name"], "a maintenant",Champion["Mana Max"], "de mana\n")
                    # ajout de mana normalement au champion.

            elif acceptation == "non":
                print(Champion["Name"],"n'a pas accepté l'utilisation de la potion")
                reponse = True
            else:
                print("Vous devez répondre par oui ou non !!")

    else:
        print(
            Champion["Name"], "n'a pas de potion actuellement dans l'inventaire, il ne peut donc pas l'utiliser !!! \n")
# Question 5


def Augmenter_Niveau(Champion, Champion_LevelUp):
    """
        Description : Fonction permettant d'augmenter le niveau d'un champion à un niveau aléatoire entre 1 et 18.
       Paramètres : Champion - dictionnaire - In
                   ChampionLevelUp - dictionnaire - In
       Préconditions : Champion = dictionnaire
                       ChampionLevelUp = dictionnaire
       Postconditions : Augmente le niveau d'un champion à un niveau aléatoire entre 1 et 18
    """

    level_gagné = random.randint(1, 17)  # goin de niveau aléatoire
    # ajout au niveau du Champion son gain de niveau(x).
    Champion["Level"] += level_gagné
    if Champion["Level"] == 18:
        Champion["Vie Max"] += Champion_LevelUp["Vie Max"] * level_gagné
        Champion["Attaque"] += Champion_LevelUp["Attaque"] * level_gagné
        Champion["Armure"] += Champion_LevelUp["Armure"] * level_gagné
        Champion["Mana Max"] += Champion_LevelUp["Mana Max"] * level_gagné
        Champion["Vie actuelle"] = Champion["Vie Max"]
        Champion["Mana actuel"] = Champion["Mana Max"]
        print(Champion["Name"], "a atteint le niveau 18, c'est le niveau maximum, voici ses nouvelles statistiques :", "\nVie Max :",
              Champion["Vie Max"], "\nAttaque :", Champion["Attaque"], "\nArmure :", Champion["Armure"], "\nMana Max :", Champion["Mana Max"], "\n")
        # attribution des nouvelles statistiques en fonction du niveau(ici 18), puis affichage de ses nouvelles statistiques plus phrase d'alerte.
    else:
        Champion["Vie Max"] += Champion_LevelUp["Vie Max"] * level_gagné
        Champion["Attaque"] += Champion_LevelUp["Attaque"] * level_gagné
        Champion["Armure"] += Champion_LevelUp["Armure"] * level_gagné
        Champion["Mana Max"] += Champion_LevelUp["Mana Max"] * level_gagné
        Champion["Vie actuelle"] = Champion["Vie Max"]
        Champion["Mana actuel"] = Champion["Mana Max"]
        print(Champion["Name"], "est maintenant niveau", Champion["Level"])
        print("Voici les nouvelles statistiques de", Champion["Name"], ":", "\nVie Max :", Champion["Vie Max"],
              "\nAttaque :", Champion["Attaque"], "\nArmure :", Champion["Armure"], "\nMana Max :", Champion["Mana Max"], "\n")
        # et ici tous les niveaux sauf 18.

# Question 6


def Combat():
    """Description : Fonction simulant un combat entre deux Champions, le premier champion est choisis aléatoirement.
       Préconditions : Deux dictionnaire pour deux champions
       Postconditions : Affiche le vainqueur du combat
    """
    Liste_Champion = (Olaf, Jax)  # liste des Champions
    Premier_Attaquant = random.choice(Liste_Champion)  # Premier attaquant
    # Second attaquant, liste qui sera remplie en fonction du premier attaquant.
    Second_Attaquant = ""

    if Premier_Attaquant == Liste_Champion[0]:
        Second_Attaquant = Liste_Champion[1]
    else:
        Second_Attaquant = Liste_Champion[0]
    # système d'aléatoire pour le premier attaquant.

    print("Le premier attaquant est", Premier_Attaquant["Name"], "et possède comme statistiques \n", "niveau", Premier_Attaquant["Level"],
          "\n", Premier_Attaquant["Vie Max"], "pv\n", Premier_Attaquant["Attaque"], "d'attaque\n", Premier_Attaquant["Armure"], "d'armure\n")
    print("Le second attaquant est", Second_Attaquant["Name"], "et possède comme statistiques :\n", "niveau", Second_Attaquant["Level"],
          "\n", Second_Attaquant["Vie Max"], "pv\n", Second_Attaquant["Attaque"], "d'attaque\n", Second_Attaquant["Armure"], "d'armure\n")
    # Affichage du premier attaquant et ses stats ainsi que le deuxieme et ses stats.

    while Premier_Attaquant["Vie actuelle"] > 0 and Second_Attaquant["Vie actuelle"] > 0:
        # round permettant d'arrondir la valeur des dégats.
        AttaqueChampion1 = round(
            (100/(Second_Attaquant["Armure"]+100))*Premier_Attaquant["Attaque"])
        # Phrase d'information du combat sur les dégats infligé du 1er attaquant au deuxième.
        print(Premier_Attaquant["Name"], "vient d'infliger",
              AttaqueChampion1, "dégats à", Second_Attaquant["Name"])
        # perte de vie du second attaquant par les dégats du 1er.
        Second_Attaquant["Vie actuelle"] -= AttaqueChampion1
        # affichage des pv du 2nd champion ainsi que ses nouveaux(si il en a plus que 0)
        if Second_Attaquant["Vie actuelle"] > 0:
            print("La vie de", Second_Attaquant["Name"], "est passé de", Second_Attaquant["Vie actuelle"] +
                  AttaqueChampion1, "à", Second_Attaquant["Vie actuelle"], "pv")
        elif Second_Attaquant["Vie actuelle"] <= 0:
            Second_Attaquant["Vie actuelle"] = 0
            print("La vie de", Second_Attaquant["Name"], "est passé de",
                  Second_Attaquant["Vie actuelle"]+AttaqueChampion1, "à 0 pv")
            break
        # elif pour permettre d'afficher 0 à la place d'un nombre négatif et afficher sa vie comme pour le if.

        # round permettant d'arrondir la valeur des dégats.
        AttaqueChampion2 = round(
            (100/(Premier_Attaquant["Armure"]+100))*Second_Attaquant["Attaque"])
        # Phrase d'information du combat sur les dégats infligé du 2nd attaquant au 1er.
        print(Second_Attaquant["Name"], "vient d'infliger",
              AttaqueChampion2, "dégats à", Premier_Attaquant["Name"])
        # perte de vie du 1er attaquant par les dégats du 2nd.
        Premier_Attaquant["Vie actuelle"] -= AttaqueChampion2
        # affichage des pv du 1er champion ainsi que ses nouveaux(si il en a plus que 0)
        if Premier_Attaquant["Vie actuelle"] > 0:
            print("La vie de", Premier_Attaquant["Name"], "est passé de", Premier_Attaquant["Vie actuelle"] +
                  AttaqueChampion2, "à", Premier_Attaquant["Vie actuelle"], "pv")
        elif Premier_Attaquant["Vie actuelle"] <= 0:
            Premier_Attaquant["Vie actuelle"] = 0
            print("La vie de", Premier_Attaquant["Name"], "est passé de",
                  Premier_Attaquant["Vie actuelle"]+AttaqueChampion2, "à 0 pv")
            break
        # elif pour permettre d'afficher 0 à la place d'un nombre négatif et afficher sa vie comme pour le if.

    # affichage du vainqueur en fonction du premier à 0 PV.
    if Premier_Attaquant["Vie actuelle"] <= 0:
        print(Second_Attaquant["Name"], "a gagné !!!!")
    else:
        print(Premier_Attaquant["Name"], "a gagné !!!")

# Question 7


def Ressusciter(Champion):
    """
    Description : Fonction permettant de réssucite un champion
    Paramètre : Champion - dictionnaire - In
    Préconditions : Champion = dictionnaire
    Postconditions : Réssucite un Champion
    """
    if Champion["Vie actuelle"] == 0:
        # dans ce cas attribution de ses points de vie max.
        Champion["Vie actuelle"] = Champion["Vie Max"]
        print(Champion["Name"], "a bien été réssucité et a reçu",
              Champion["Vie Max"], "pv")  # phrase d'alerte
    else:
        print(Champion["Name"], "n'est pas mort !!")
        # phrase d'alerte indiquant que le champion n'est pas décédé.

# Question 8


def Acheter_Objet(Champion, Objet):
    """Description : Fonction permettant l'achat d'objets
     Paramètres : Champion - dictionnaire - In
                  Objet - dictionnaire - In
     Préconditions : Champion = dictionnaire
                     Objet = dictionnaire
     Postconditions : Stocke l'objet dans un tableau InventaireChampion
    """
    if Champion["NombreObjet"] < 6:  # inventaire max = 6, il peut alors acheter.
        # vérification si le champion a assez de gold
        if Champion["Gold"] > Objet["Prix"]:
            Champion["Gold"] -= Objet["Prix"]  # acheter l'objets si oui.

            # attribution des stats par rapport à l'objet acheté(Lame de Doran)
            if Objet["Name"] == "Lame de Doran":
                Champion["Vie Max"] += Objet["Vie Max"]
                Champion["Vie actuelle"] += Objet["Vie actuelle"]
                Champion["Attaque"] += Objet["Attaque"]
                # phrase d'alerte indiquant qui a acheté l'objet.
                print(Champion["Name"],"a acheté l'objet <<", Objet["Name"], ">>")
                # affichage du nouveau nombre de gold  du champion ayant acheté l'objet.
                print(Champion["Name"], "a maintenant",Champion["Gold"], "gold\n")
                # ajout de l'objet dans l'inventaire de l'acheteur.
                Champion["Inventaire"].append(Objet["Name"])
                # inventaire plus 1 car il possède une limite de 6.
                Champion["NombreObjet"] += 1

                # pareil pour les autres objets possibles à l'achat.

            elif Objet["Name"] == "Coques en acier":
                Champion["Armure"] += Objet["Armure"]
                Champion["Vitesse"] += Objet["Vitesse de déplacement"]
                Champion["NombreObjet"] += 1
                Champion["Inventaire"].append(Objet["Name"])
                print(Champion["Name"],"a acheté l'objet <<", Objet["Name"], ">>")
                print(Champion["Name"], "a maintenant",Champion["Gold"], "gold\n")

            elif Objet["Name"] == "Ange Gardien":
                Champion["Armure"] += Objet["Armure"]
                Champion["Attaque"] += Objet["Attaque"]
                Champion["Inventaire"].append(Objet["Name"])
                Champion["NombreObjet"] += 1
                print(Champion["Name"],"a acheté l'objet <<", Objet["Name"], ">>")
                print(Champion["Name"], "a maintenant",Champion["Gold"], "gold\n")

            elif Objet["Name"] == "Cotte épineuse":
                Champion["Armure"] += Objet["Armure"]
                Champion["Vie Max"] += Objet["Vie Max"]
                Champion["Vie actuelle"] += Objet["Vie actuelle"]
                Champion["NombreObjet"] += 1
                Champion["Inventaire"].append(Objet["Name"])
                print(Champion["Name"],"a acheté l'objet <<", Objet["Name"], ">>")
                print(Champion["Name"], "a maintenant",
                Champion["Gold"], "gold\n")

            elif Objet["Name"] == "Potion":
                Champion["NombreObjet"] += 1
                Champion["Inventaire"].append(Objet["Name"])
                print(Champion["Name"],"a acheté l'objet <<", Objet["Name"], ">>")
                print(Champion["Name"], "a maintenant",Champion["Gold"], "gold\n")

        else:
            print(Champion["Name"], "n'a pas assez de gold pour acheter <<", Objet["Name"], ">> qui coûte <<", Objet["Prix"], ">> de gold, il lui en manque",
            Objet["Prix"]-Champion["Gold"])  # Affichage d'une alerte disant que le héro n'a pas assez de gold pour effectuer l'achat

    else:
            # Affichage d'une alerte indiquant que l'inventaire du champion est plein.
        print("\nL'inventaire du champion",
        Champion["Name"], "est plein, sa limite est de 6 emplacements !!\n")


def Vendre_Objet(Champion, Objet):
    """
    Description : Fonction permettant la vente d'objets.
    Paramètres : Champion - dictionnaire - In 
                 Objet - dictionnaire - In
    Préconditions : Champion = dictionnaire 
                    Objet = dictionnaire
    Postconditions : Retire l'objet de l'inventaire d'un champion
    """
    if Objet["Name"] in Champion["Inventaire"]:#vérification si l'objet est possédé par le champion
        Champion["Inventaire"].remove(Objet["Name"])#on le retire si oui
        Champion["Gold"] += round(Objet["Prix"]*0.70)#il récupere que 70% du prix de base
        if Objet["Name"] == "Lame de Doran":
            Champion["Vie Max"] -= Objet["Vie Max"]
            Champion["Vie actuelle"] -= Objet["Vie actuelle"]
            Champion["Attaque"] -= Objet["Attaque"]
            Champion["NombreObjet"] -= 1
            # puis ensuite on retire les statistiques ajouté au champion lors de l'achat
            print(Champion["Name"],"a vendu l'objet <<",Objet["Name"],">>")#phrase d'alerte de vente d'objet 
            print(Champion["Name"],"a maintenant",Champion["Gold"],"gold\n")#affichage du nouveau montant de gold du champion.

            # puis meme systeme pour les autres items

        elif Objet["Name"] == "Coques en acier":
            Champion["Armure"] -= Objet["Armure"]
            Champion["Vitesse"] -= Objet["Vitesse de déplacement"]
            Champion["NombreObjet"] -= 1
            print(Champion["Name"],"a vendu l'objet <<",Objet["Name"],">>")
            print(Champion["Name"],"a maintenant",Champion["Gold"],"gold\n")

        elif Objet["Name"] == "Ange Gardien":
            Champion["Armure"] -= Objet["Armure"]
            Champion["Attaque"] -= Objet["Attaque"]
            Champion["NombreObjet"] -= 1
            print(Champion["Name"],"a vendu l'objet <<",Objet["Name"],">>")
            print(Champion["Name"],"a maintenant",Champion["Gold"],"gold\n")

        elif Objet["Name"] == "Cotte épineuse":
            Champion["Armure"] -= Objet["Armure"]
            Champion["Vie Max"] -= Objet["Vie Max"]
            Champion["Vie actuelle"] -= Objet["Vie actuelle"]
            Champion["NombreObjet"] -= 1
            print(Champion["Name"],"a vendu l'objet <<",Objet["Name"],">>")
            print(Champion["Name"],"a maintenant",Champion["Gold"],"gold\n")

    else:
        print("L'objet <<",Objet["Name"],">> n'est pas contenu dans l'inventaire du champion",Champion["Name"],"\n")#affichage d'alerte si le champion ne possède pas l'objet

# Question 9
def Appel_des_fonctions():
    """Description : Fonction effectuant toutes les fonctions du programme.
         Postconditions : effectue toutes les fonctions du programme
    """
    print("\nQuestion 2 :\n")#affichage de la question affichée
    Afficher_Statistiques(Jax)
    Afficher_Statistiques(Olaf)
    print("Question 3 :\n")
    Augmenter_PO(Jax)
    Augmenter_PO(Olaf)
    print("\nQuestion 4 :\n")
    Utiliser_Potion(Jax)
    Utiliser_Potion(Olaf)
    Acheter_Objet(Olaf, Potion)
    Utiliser_Potion(Jax)
    Utiliser_Potion(Olaf)
    print("Question 5 :\n")
    Augmenter_Niveau(Jax, Jax_LevelUp)
    Augmenter_Niveau(Olaf, Olaf_LevelUp)
    print("Question 6 :\n")
    Combat()
    print("\nQuestion 7 : \n")
    Ressusciter(Jax)
    Ressusciter(Olaf)
    print("\nQuestion 8 : \n")
    # Pour augmenter l'argent de chacun pour tester le fait qu'il y ait plus de 6 objets ou bien de la vente enlever les '' du prochain paragraphe
    ""
    # for i in range(20):
    #     Augmenter_PO(Olaf)
    #     Augmenter_PO(Jax)
    # ""

    print("")
    Acheter_Objet(Olaf, Lame_de_Doran)#teste de tous les achats pour Olaf
    Acheter_Objet(Olaf, Lame_de_Doran)
    Acheter_Objet(Olaf, Coques_en_acier)
    Acheter_Objet(Olaf, Ange_Gardien)
    Acheter_Objet(Olaf, Cotte_epineuse)
    Acheter_Objet(Olaf, Cotte_epineuse)
    Acheter_Objet(Olaf, Ange_Gardien)
    print("")
    Acheter_Objet(Jax, Lame_de_Doran)#teste de tous les achats pour Jax
    Acheter_Objet(Jax, Lame_de_Doran)
    Acheter_Objet(Jax, Coques_en_acier)
    Acheter_Objet(Jax, Ange_Gardien)
    Acheter_Objet(Jax, Cotte_epineuse)

    Afficher_Statistiques(Olaf)
    Afficher_Statistiques(Jax)

    print("\nQuestion 8 Partie D : \n")
    Vendre_Objet(Olaf, Lame_de_Doran)#Teste de touts les ventes d'obets
    Vendre_Objet(Olaf, Cotte_epineuse)
    Vendre_Objet(Olaf, Ange_Gardien)
    Vendre_Objet(Olaf, Coques_en_acier)
    Vendre_Objet(Jax, Lame_de_Doran)
    Vendre_Objet(Jax, Cotte_epineuse)
    Vendre_Objet(Jax, Ange_Gardien)
    Vendre_Objet(Jax, Coques_en_acier)

    Afficher_Statistiques(Olaf)
    Afficher_Statistiques(Jax)

Appel_des_fonctions()
