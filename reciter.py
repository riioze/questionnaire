from fonctions import*
import tkinter

os.chdir("C:/Users/riioz/Desktop/questionnaire/logs")
compteur = 0
questions = []
solutions = []
ouinon = "o"
score = 0
nombre_reponses = 0

fenetre = tkinter.Tk()


menubar = tkinter.Menu(fenetre)
menu1 = tkinter.Menu(menubar,tearoff=0)
menu1.add_command(label="Importer",command=importer)
menu1.add_command(label="Créer",comman=creer)
menubar.add_cascade(label="Fichier", menu=menu1)
fenetre.config(menu=menubar)
bouton=tkinter.Button(fenetre, text="lancer", command=lancer)
bouton.pack()

fenetre.mainloop()