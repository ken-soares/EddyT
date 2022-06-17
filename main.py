from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import asksaveasfile
from tkinter import messagebox
from PIL import Image, ImageTk

hello_kitty ={"text_area_fg":"#000000","text_area":"#FFE5EC","button":"#FB6F92","background":"#FFC2D1","display_path":"#FFB3C6","text_button_path":"#FFFFFF"}
batman ={"text_area_fg":"#ffffff","text_area":"#383033","button":"#4a3540","background":"#171415","display_path":"#211C1E","text_button_path":"#FFFFFF"}

def dark(popup):
    global window
    popup.iconify()
    window = Tk()
    create_gui(window,isNew,batman)

def pink(popup):
    global window
    popup.iconify()
    window = Tk()
    
    create_gui(window,isNew,hello_kitty)  


def demande_theme():
    '''
    appelle la fonction de changement de theme
    entrer : Rien
    sortie : True
    '''
    global popup
    popup = Tk()
    popup.geometry("260x120")
    popup.resizable(False,False)
    popup.title("Select a theme")
    texte = Label(popup,text = "Create an instance of Eddy T\nwith theme:",font = ("Courier",10)).place(x=10,y = 8)
    bouton_dark = ""
    bouton_dark = Button(popup,text = "Batman",width = 10,command =lambda:dark(popup), bg = "grey").place(x=40,y = 80)
    bouton_pink = ""
    bouton_pink = Button(popup,text = "Hello Kitty",width = 10,command =lambda:pink(popup), bg = "pink").place(x=130,y = 80)
    popup.mainloop()
    return True


isNew = True

def create_gui(window,isNew:bool,theme):
    '''
    Crée l'interface graphique de l'éditeur de texte
    entrée: window: la fenêtre Tkinter,  isNew =>bool :déclare si fichier nouveau ou pas, theme=>dictionnaire: choix du theme 
    sortie: un bool (True = pas d'erreur dans la création de l'interface)
    '''
    window.geometry("1280x720")
    window.title("Eddy T")
    window.resizable(False, False)
    window.configure(bg=theme["background"])
    title = Label(window,bg = theme ["background"],fg = theme["text_button_path"], text="Eddy T",font=("Courier",15)).place(x=55,y=20)
    text_area = Text(window,width=130,height=39, bg = theme["text_area"],fg=theme["text_area_fg"])
    text_area.pack(side='right',padx=10)
    path = Label(window,fg = theme["text_button_path"],bg = theme["display_path"],text='click on "open" or "save as" to display file path',width=150,font=("Courier", 10))
    path.place(x=100,y=680)
    new = Button(window,bg = theme["button"],fg = theme["text_button_path"],text="New",font=("Courier",15),width=10,command=lambda:clear_buffer(text_area)).place(x=30,y=100)
    open_file = Button(window,bg = theme["button"],fg = theme["text_button_path"],text="Open",font=("Courier",15),width=10,command=lambda: open_action(text_area,path)).place(x=30,y=150)
    #lambda is used to pass the data to a callback function
    save_file = Button(window,bg = theme["button"],fg = theme["text_button_path"],text="Save",font=("Courier",15),width=10,command=lambda:save(text_area.get("1.0","end"),path["text"])).place(x=30,y=200)
    saveas = Button(window,bg = theme["button"],fg = theme["text_button_path"],text="Save as",font=("Courier",15),width=10,command=lambda: save_as(text_area.get("1.0","end"),path)).place(x=30,y=250)
    about = Button(window,bg = theme["button"],fg = theme["text_button_path"],text="About",font=("Courier",15),width=10,command=lambda:aboutfct(theme)).place(x=30,y=300)
    window.mainloop()
    return True

def open_action(text_area:Text,path_label:Label):
    '''
    Permet d'ouvrir un fichier dans l'éditeur de texte
    entree: text_area: zone ou le texte est ecrit, path_label=>Label tkinter: affiche chemin d'acces fichier 
    sortie: bool: True si réussite
    '''
    global isNew
    isEmpty = text_area.get("1.0","end-1c") == ""
    if isEmpty:
        NomDuFichier = filedialog.askopenfilename()
        fichier = open(NomDuFichier,'r',encoding = 'utf8')
        content = fichier.read()
        text_area.insert(INSERT,content)
        fichier.close()
    else:
        clear_buffer(text_area)
        NomDuFichier = filedialog.askopenfilename()
        fichier = open(NomDuFichier,'r',encoding = 'utf-8')
        content = fichier.read()
        text_area.insert(INSERT,content)
        fichier.close()
        
    isNew = False
    path_label["text"] = NomDuFichier
    return True

def clear_buffer(text_area:Text):

    """
    supprime le contenu de la zone de texte
    entree: text_area:la zone de texte 
    sortie: True
    """
    global isNew
    text_area.delete("1.0","end")
    isNew = True
    return True
    
def save_as(content:str,path_label):
    """cette fontion permet d'enregistrer en tant que nouveau fichier le texte
    entree: content=>string: contenu du text area ,path_label=>Label tkinter: affiche chemin d'acces fichier
    sortie: string:chemin d'acces du fichier """
    global isNew
    fichier = filedialog.asksaveasfile(mode = 'w')
    fichier.write(content)
    fichier.close()
    isNew = False
    path_label["text"] = fichier.name
    return fichier.name


def save(content,file_name):
    """cette fonction permet de sauvegarder le fichier en cours de modification
    entree: content => string: le texte écrit qui doit etre sauvegardé   file_name =>string: nom du fichier dans lequel le texte est enregistré
    sortie: string:chemin d'accès du fichier"""
    if isNew == False:
        fichier = open(file_name,"w")
        fichier.write(content)
        fichier.close()
        messagebox.showinfo(title="File saved", message="File was saved successfully")
    else:
        messagebox.showerror(title= "wrong operation",message = 'in order to save a new file, click on "save as"')
    return fichier.name

def aboutfct(theme):
    """cette fonction permet d'ouvrir une fenetre about
    entree: dictionnaire => theme choisi
    sortie: bool=> True si réussite"""
    root = Toplevel()
    root.geometry("550x250")
    root.configure(bg=theme["background"])
    root.title("About Eddy T.")
    root.resizable(False,False)
    can1 = Canvas(root, width=180, height=260,bg=theme['background'],highlightthickness=0)
    image = PhotoImage(file='logo.png')
    item = can1.create_image(100,125, image=image)
    can1.image = image
    can1.pack(side=LEFT)
    title = Label(root, text="Eddy T\n\tby Kenneth Soares, Melusine Puliero, Alexis Nobilet",fg="#ffffff",bg=theme['background'])
    specs = Label(root, text="Written in Python using Tkinter and pillow",fg="#ffffff",bg=theme['background'])
    where = Label(root, text="Made at NDO in Computer Science (NSI) class",fg="#ffffff",bg=theme['background'])
    when = Label(root, text="May 2022 and still striving to improve ^-^",fg="#ffffff",bg=theme['background']) # <3
    title.pack()
    specs.pack()
    where.pack()
    when.pack(side=BOTTOM)
    root.mainloop()
    return True

window = demande_theme()


