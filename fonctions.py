from random import randrange
import os
import time
from math import ceil
from tkinter import *
from tkinter.filedialog import *

def continuertest():
	global ouinon
	global reponse
	reponse = rEntry.get()
	reponse = reponse.lower()
	ftest.quit()
	ouinon="o"

def terminertest():
	global ouinon
	global reponse
	reponse = rEntry.get()
	reponse = reponse.lower()
	ftest.quit()
	ouinon="n"



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
		file.write(question+","+reponse+"\n")
		if ouinon == "o":
			for c in fcreer.winfo_children():
				c.destroy()
			continue
		else:
			file.close()
			break

def lancer():
	global ftest
	global rEntry
	ftest = Tk()
	file = open(filename,"r")
	Intro1 = Label(ftest,text="C'est l'heure du test veuillez répondre aux questions.",width = 50)

	qna = file.read()
	qna = qna.split('\n')
	qnas = []
	for x in range(len(qna)):
		ligne = qna[x].split(',')
		qnas.append(ligne)
	score = 0
	nombre_reponses = 0
	while 2:

		n = randrange(len(qnas))
		question = Label(ftest,text=qnas[n][0],width=50)
		rtest = StringVar()
		rEntry = Entry(ftest,textvariable=rtest,width=30)
		Continuer = Button(ftest,text="Continuer",command=continuertest)
		Terminer = Button(ftest,text="Terminer",command=terminertest) 
		question.pack()
		rEntry.pack()
		Continuer.pack()
		Terminer.pack()
		ftest.mainloop()
		if reponse == qnas[n][1]:
			message = Label(ftest,text="Bravo. Vous  gagnez un point.",width=30)
			score += 1
		else:
			message = Label(ftest,text="Raté. C'était {0} et non {1}.".format(qnas[n][1], reponse),width=30)
		mscore = Label(ftest,text="Votre score actuel est de {0} sur {1}.".format(score, nombre_reponses),width=30)
		OK = Button(ftest,text="OK",command=ftest.quit)
		message.pack()
		mscore.pack()
		OK.pack()
		nombre_reponses += 1
		ftest.mainloop()
		if ouinon == "o":
			for c in ftest.winfo_children():
				c.destroy()
			time.sleep(1)
			continue
		else:
			pourcentage = ceil((score/nombre_reponses)*100)
			mscorefinal=Label(ftest,text="Votre score final est de {0} sur {1}, ce qui fait une réussite d'environ {2}%.".format(score, nombre_reponses, pourcentage))
			time.sleep(2)
			ftest.quit()
			ftest.mainloop()
			break