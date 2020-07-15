from random import randrange
import os
import time
from math import ceil




def importer():
	global nom_questionnaire
	nom_questionnaire = input("quel questionnaire voulez vous ouvrir?")

	


def creer():
	global nom_questionnaire
	print ("Veuiller donner un nom à ce questionnaire")
	nom_questionnaire = input()
	file = open(nom_questionnaire+".txt","w")
	while 1:
		print ("Entrez une question sans virgule")
		question = input()
		print ("Entrez la réponse sans virgule")
		reponse = input()
		reponse = reponse.lower()
		file.write(question+","+reponse)
		print ("Continuer? O/N")
		ouinon = input()
		ouinon = ouinon.lower()
		if ouinon == "o":

			continue
		else:
			file.close()
			break

def lancer():
	file = open(nom_questionnaire+".txt","r")
	os.system("cls")
	time.sleep(1)
	print ("Voilà. Maintenant, c'est l'heure du test!")
	time.sleep(1)
	print ("Répondez simplement aux questions puis appuyez sur entrée.")
	time.sleep(2)
	qna = file.read()
	qna = qna.split('\n')
	print(qna)
	qnas = []
	for x in range(len(qna)):
		print(qna[x])
		ligne = qna[x].split(',')
		qnas.append(ligne)
	score = 0
	nombre_reponses = 0
	while 2:

		n = randrange(len(qnas))
		print (qnas[n][0])
		reponse = input("")
		reponse = reponse.lower()
		if reponse == qnas[n][1]:
		    print ("Bravo. Vous gagnez un point.")
		    score += 1
		else:
		    print ("Raté. C'était {0} et non {1}.".format(qnas[n][1], reponse))
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