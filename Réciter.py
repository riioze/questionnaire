from random import randrange
import os
import time
from math import ceil
import pickle

os.chdir("C:/Users/riioz/Desktop/questionnaires")
compteur = 0
questions = []
solutions = []
ouinon = "o"
score = 0
nombre_reponses = 0

time.sleep(1)
print ("Bonjour.")
time.sleep(1)
print ("Ce programme vous sert à vous faire réciter des choses.")
time.sleep(2)
print ("Donc, lorsque vous répondrez, il convient de garder les mêmes espaces et les mêmes accents.")
time.sleep(2.5)
print ("Désirez-vous importer un questionnaire déjà existant? O/N")
ouinon = input()
ouinon = ouinon.lower()

if ouinon == "o":
    print ("Bien.Veuillez entrer le nom du questionnaire")
    nom_questionnaire = input()
    nom_questionnaire0 = nom_questionnaire + "questions"
    nom_questionnaire1 = nom_questionnaire + "solutions"
    nom_questionnaire2 = nom_questionnaire + "compteur"
else:
    while 1:
        print ("Entrez une question.")
        questions.append(input())
        print ("Entrez la réponse.")
        solution = input()
        solution = solution.lower()
        solutions.append(solution)
        compteur += 1
        print ("Continuer? O/N")
        ouinon = input()
        ouinon = ouinon.lower()
        if ouinon == "o":
            
            continue
        else:
            print ("Veuiller donner un nom à ce questionnaire")
            nom_questionnaire = input()
            nom_questionnaire0 = nom_questionnaire + "questions"
            nom_questionnaire1 = nom_questionnaire + "solutions"
            nom_questionnaire2 = nom_questionnaire + "compteur"

            with open (nom_questionnaire0, "wb") as ecriture:
                ecriture = pickle.Pickler(ecriture)
                ecriture.dump(questions)

            with open (nom_questionnaire1, "wb") as ecriture:
                ecriture = pickle.Pickler(ecriture)
                ecriture.dump(solutions)

            with open (nom_questionnaire2, "wb") as ecriture:
                ecriture = pickle.Pickler(ecriture)
                ecriture.dump(compteur)

            break



with open (nom_questionnaire0, "rb") as recevoir:
        recevoir = pickle.Unpickler(recevoir)
        questions = recevoir.load()

with open (nom_questionnaire1, "rb") as recevoir:
        recevoir = pickle.Unpickler(recevoir)
        solutions = recevoir.load()

with open (nom_questionnaire2, "rb") as recevoir:
        recevoir = pickle.Unpickler(recevoir)
        compteur = recevoir.load()

os.system("cls")
time.sleep(1)
print ("Voilà. Maintenant, c'est l'heure du test!")
time.sleep(1)
print ("Répondez simplement aux questions puis appuyez sur entrée.")
time.sleep(2)

while 2:
    nombre = randrange(compteur)
    print (questions[nombre])
    reponse = input("")
    reponse = reponse.lower()
    if reponse == solutions[nombre]:
        print ("Bravo. Vous gagnez un point.")
        score += 1
    else:
        print ("Raté. C'était {0} et non {1}.".format(solutions[nombre], reponse))
    nombre_reponses += 1
    time.sleep(1)
    print ("Votre score actuel est de {0} sur {1}.".format(score, nombre_reponses))
    time.sleep(1)
    print ("Voulez-vous continuer? O/N")
    ouinon = input()
    ouinon = ouinon.lower()
    if ouinon == "o":
        os.system("cls")
        time.sleep(1)
        continue
    else:
        os.system("cls")
        time.sleep(1)
        break

pourcentage = ceil((score/nombre_reponses)*100)
print ("Votre score final est de {0} sur {1}, ce qui fait une réussite d'environ {2}%.".format(score, nombre_reponses, pourcentage))
time.sleep(3)
print ("Au revoir.")
time.sleep(3)
os.system("pause")