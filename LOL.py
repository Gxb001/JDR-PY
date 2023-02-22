import random 
#Création de tous les dictionnaires nécessaires pour tout le programme
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
    "Vitesse": 350
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
    "Vitesse": 350
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
    "Prix": 450,
    "Vie Max": 80,
    "Vie actuelle": 80,
    "Attaque": 8,
}
Coques_en_acier = {
    "Prix": 1100,
    "Armure": 20,
    "Vitesse de déplacement": 45,
}

Ange_Gardien = {
    "Prix": 2800,
    "Armure": 40,
    "Attaque": 40,
}

Cotte_epineuse = {
    "Prix": 2700,
    "Vie Max": 350,
    "Armure": 60,
    "Vie actuelle": 350,
}


#Question 2
def Afficher_Stat(Champion):
    print("Statistiques de", Champion["Name"],":")
    print("Or", "=",Champion["Gold"])
    print("Vie Maximale", "=", Champion["Vie Max"])
    print("Vie actuelle", "=", Champion["Vie actuelle"])
    print("Attaque", "=", Champion["Attaque"])
    print("Armure", "=", Champion["Armure"])
    print("Mana max", "=", Champion["Mana Max"])
    print("Mana actuel", "=", Champion["Mana actuel"])
    print("vitesse de déplacment", "=", Champion["Vitesse"],"\n")
    
#Question 3
def Augmenter_PO(Champion):
    nb_sbire = random.randint(5, 10) # Nombre aléatoire de sbire tués
    gold_sbire = random.randint(14, 69)
    Champion["Gold"] += gold_sbire*nb_sbire
    print(Champion["Name"],"a maintenant",Champion["Gold"],"golds.")

#Question 4
def Utiliser_Potion(Champion):
    
    effet_mana = 75
    effet_pv = 125

    if Champion["Vie actuelle"] + effet_pv > Champion["Vie Max"]:
        Champion["Vie actuelle"] = Champion["Vie Max"]
        print(Champion["Name"],"a dépassé ses pv maximum en utilisant sa potion, donc ses pv sont définis au maximum soit", Champion["Vie Max"],"pv")
    else :
        Champion["Vie actuelle"] += effet_pv
        print(Champion["Name"],"a maintenant",Champion["Vie Max"],"pv")

    if Champion["Mana actuel"] + effet_mana > Champion["Mana Max"]:
        Champion["Mana actuel"] = Champion["Mana Max"]
        print(Champion["Name"],"a dépassé son mana maximum en utilisant sa potion, donc son mana est défini au maximum soit", Champion["Mana Max"],"de mana\n")
    else :
        Champion["Mana actuel"] += effet_mana
        print(Champion["Name"],"a maintenant",Champion["Mana Max"],"de mana\n")

#Question 5
def Augmenter_Niveau(Champion, Champion_LevelUp):
    level_gagné =  random.randint(1, 18)
    Champion["Level"] = level_gagné
    if Champion["Level"] == 18:
        Champion["Vie Max"] += Champion_LevelUp["Vie Max"] * level_gagné
        Champion["Attaque"] += Champion_LevelUp["Attaque"] * level_gagné
        Champion["Armure"] += Champion_LevelUp["Armure"] * level_gagné
        Champion["Mana Max"] += Champion_LevelUp["Mana Max"] * level_gagné
        Champion["Vie actuelle"] = Champion["Vie Max"]
        print(Champion["Name"],"a atteint le niveau 18, c'est le niveau maximum, voici ses nouvelles statistiques :","\nVie Max :",Champion["Vie Max"],"\nAttaque :",Champion["Attaque"],"\nArmure :",Champion["Armure"],"\nMana Max :",Champion["Mana Max"],"\n")
    else: 
        Champion["Vie Max"] += Champion_LevelUp["Vie Max"] * level_gagné
        Champion["Attaque"] += Champion_LevelUp["Attaque"] * level_gagné
        Champion["Armure"] += Champion_LevelUp["Armure"] * level_gagné
        Champion["Mana Max"] += Champion_LevelUp["Mana Max"] * level_gagné
        Champion["Vie actuelle"] = Champion["Vie Max"]
        print(Champion["Name"],"est maintenant niveau",Champion["Level"])
        print("Voici les nouvelles statistiques de",Champion["Name"],":","\nVie Max :",Champion["Vie Max"],"\nAttaque :",Champion["Attaque"],"\nArmure :",Champion["Armure"],"\nMana Max :",Champion["Mana Max"],"\n")
            
#Question 6
def Combat():
    terminé = False
    Gl = (Olaf,Jax)   #liste champ
    Premier_Attaquant = random.choice(Gl)         #First Champion
    Second_Attaquant = ""                         #Second champion

    if Premier_Attaquant == Gl[0]:
        Second_Attaquant = Gl[1]
    else :
        Second_Attaquant = Gl[0]

    print("Le premier attaquant est",Premier_Attaquant["Name"],"et possède comme statistiques \n","niveau",Premier_Attaquant["Level"],"\n",Premier_Attaquant["Vie Max"],"pv\n",Premier_Attaquant["Attaque"],"d'attaque\n",Premier_Attaquant["Armure"],"d'armure\n")
    print("Le second attaquant est",Second_Attaquant["Name"],"et possède comme statistiques :\n","niveau",Second_Attaquant["Level"],"\n",Second_Attaquant["Vie Max"],"pv\n",Second_Attaquant["Attaque"],"d'attaque\n",Second_Attaquant["Armure"],"d'armure\n")
    
    while Premier_Attaquant["Vie actuelle"] > 0 and Second_Attaquant["Vie actuelle"] > 0:
        AttaqueChampion1 = round((100/(Second_Attaquant["Armure"]+100))*Premier_Attaquant["Attaque"])
        print(Premier_Attaquant["Name"],"vient d'infliger",AttaqueChampion1,"dégats à",Second_Attaquant["Name"])
        Second_Attaquant["Vie actuelle"] -= AttaqueChampion1
        if Second_Attaquant["Vie actuelle"] > 0:
            print("La vie de",Second_Attaquant["Name"],"est passé de",Second_Attaquant["Vie actuelle"]+AttaqueChampion1,"à",Second_Attaquant["Vie actuelle"],"pv")
        elif Second_Attaquant["Vie actuelle"] <= 0:
            Second_Attaquant["Vie actuelle"] = 0
            print("La vie de",Second_Attaquant["Name"],"est passé de",Second_Attaquant["Vie actuelle"]+AttaqueChampion1,"à 0 pv") 
            break
        
        AttaqueChampion2 = round((100/(Premier_Attaquant["Armure"]+100))*Second_Attaquant["Attaque"])
        print(Second_Attaquant["Name"],"vient d'infliger",AttaqueChampion2,"dégats à",Premier_Attaquant["Name"])
        Premier_Attaquant["Vie actuelle"] -= AttaqueChampion2
        if Premier_Attaquant["Vie actuelle"] > 0:
            print("La vie de",Premier_Attaquant["Name"],"est passé de",Premier_Attaquant["Vie actuelle"]+AttaqueChampion2,"à",Premier_Attaquant["Vie actuelle"],"pv")
        elif Premier_Attaquant["Vie actuelle"] <= 0:
            Premier_Attaquant["Vie actuelle"] = 0
            print("La vie de",Premier_Attaquant["Name"],"est passé de",Premier_Attaquant["Vie actuelle"]+AttaqueChampion2,"à 0 pv")
            break

    if Premier_Attaquant["Vie actuelle"] <= 0:
        print(Second_Attaquant["Name"],"a gagné !!!!")
    else:
        print(Premier_Attaquant["Name"],"a gagné !!!")

#Question 7
def Ressusciter(Champion):
    if Champion["Vie actuelle"] == 0 :
        Champion["Vie actuelle"] = Champion["Vie Max"]
        print(Champion["Name"],"a bien été réssucité et a reçu",Champion["Vie Max"],"pv")
    else:
        print(Champion["Name"],"n'est pas mort !!")

#Question 8
        

#Question 9
def Appel_des_fonctions():
    print("\nQuestion 2 :\n")
    Afficher_Stat(Jax)
    Afficher_Stat(Olaf)
    print("\nQuestion 3 :\n")
    Augmenter_PO(Jax)
    Augmenter_PO(Olaf)
    print("\nQuestion 4 :\n")
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

    
Appel_des_fonctions()
