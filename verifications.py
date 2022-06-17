###AFIN DE TESTER LES FONCTIONS, NOUS AVONS MODIFIER CELLES SI AFIN QU'ELLES N'UTILISENT AUCUNE VARIABLE SPECIFIQUE A L'INTERFACE GRAPHIQUE. CEPENDANT, LE FONCTIONNEMENT EST IDENTIQUE



from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import asksaveasfile
from tkinter import messagebox


def save_as(content:str):
    """cette fontion permet d'enregistrer en tant que nouveau fichier le texte
    entree: content=>string: contenu du text area ,path_label=>Label tkinter: affiche chemin d'acces fichier, isNew=>bool : déclare si fichier nouveau ou pas 
    sortie: string:chemin d'acces du fichier """
    global isNew
    fichier = filedialog.asksaveasfile(mode = 'w')
    fichier.write(content)
    fichier.close()
    isNew = False
    return fichier.name


def save(content,file_name):
    """cette fonction permet de sauvegarder le fichier en cours de modification
    entree: content => string: le texte écrit qui doit etre sauvegardé   file_name =>string: nom du fichier dans lequel le texte est enregistré, isNew =>bool :déclare si fichier nouveau ou pas
    sortie: string:chemin d'accès du fichier"""
    if isNew == False:
        fichier = open(file_name,"w")
        fichier.write(content)
        fichier.close()
        messagebox.showinfo(title="File saved", message="File was saved successfully")
    else:
        messagebox.showerror(title= "wrong operation",message = 'in order to save a new file, click on "save as"')
    return fichier.name



#verification des fonctions

nom_de_fichier= save_as("hello world")

#un fichiercontenant "hello world" a été créé et le nom du fichier est dans la variable nom_de_fichier

save("bonjour!",nom_de_fichier)

#ce fichier a ete modifier, il y a maintenant ecrit "bonjour" a l'interieur 



#verification de la fonction create_gui()
if create_gui(window,isNew,theme)==True:
    print("la fonction create_gui marche")
######################################
 
