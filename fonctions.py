from random import randrange
import os
import time
from math import ceil
from tkinter import *
from tkinter.filedialog import *

def continuer():
	global ouinon
	fcreer.quit()
	ouinon="o"
def terminer():
	global ouinon
	fcreer.quit()
	ouinon="n"

def importer():
	global filename
	filename = askopenfilename(title="Ouvrir votre document",filetypes=[('txt files','.txt'),('all files','.*')])

	


def creer():
	global fcreer
	global filename
	fcreer = Tk()
	lNom = Label(fcreer,text="Veuiller donner un nom à ce questionnaire",width=20)
	stringvar = StringVar()
	entryNom = Entry(fcreer,textvariable=stringvar,width=5)
	Valider = Button(fcreer,text="Valider",command=fcreer.quit)
	lNom.pack()
	entryNom.pack()
	Valider.pack()
	
	fcreer.mainloop()
	filename = entryNom.get()+".txt"	
	print(entryNom.get())
	file = open(filename,"w")
	while 1:
		lQuestion = Label(fcreer,text = "Veuillez entrer une question sans utiliser de virgule",width=30)
		q = StringVar()
		questionEntry = Entry(fcreer,textvariable=q,width=30)
		lReponse = Label(fcreer,text = "Veuillez entrer la réponse sans utiliser de virgule")
		r = StringVar()
		reponseEntry = Entry(fcreer,textvariable=r,width=30)
		c = Button(fcreer,text="Continuer",command=continuer)
		t = Button(fcreer,text="Terminer",command=terminer)
		lQuestion.pack()
		questionEntry.pack()
		lReponse.pack()
		reponseEntry.pack()
		c.pack()
		t.pack()
		fcreer.mainloop()
		question=questionEntry.get()
		reponse = reponseEntry.get().lower()
		file.write(question+","+reponse)
		if ouinon == "o":

			continue
		else:
			file.close()
			break

def lancer():
	file = open(filename,"r")
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