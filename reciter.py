from fonctions import*


os.chdir("C:/Users/riioz/Desktop/questionnaire/logs")


fenetre = Tk()


menubar = Menu(fenetre)
menu1 = Menu(menubar,tearoff=0)
menu1.add_command(label="Importer",command=importer)
menu1.add_command(label="Créer",comman=creer)
menubar.add_cascade(label="Fichier", menu=menu1)
fenetre.config(menu=menubar)
bouton=Button(fenetre, text="lancer", command=lancer)
bouton.pack()

fenetre.mainloop()