import tkinter as tk
from shunting_yard import tokenize, infix_to_postfix, evaluate_postfix

def calculer():
    expression = entree.get()
    
    try:
        tokens = tokenize(expression)
        postfix = infix_to_postfix(tokens)
        resultat = evaluate_postfix(postfix)
        
        label_postfix.config(text="Postfix : " + " ".join(postfix))
        label_resultat.config(text="Résultat : " + str(resultat))
        label_erreur.config(text="")
        
    except Exception as e:
        label_postfix.config(text="Postfix : -")
        label_resultat.config(text="Résultat : -")
        label_erreur.config(text="Erreur : " + str(e))

fenetre = tk.Tk()
fenetre.title("TP1 - Interface Graphique")
fenetre.geometry("750x650")

label_instruction = tk.Label(fenetre, text="Entrez une expression mathématique :")
label_instruction.pack()

entree = tk.Entry(fenetre, width=40)
entree.pack()

bouton = tk.Button(fenetre, text="Convertir et évaluer", command=calculer)
bouton.pack()

label_postfix = tk.Label(fenetre, text="Postfix : ")
label_postfix.pack()

label_resultat = tk.Label(fenetre, text="Résultat : ")
label_resultat.pack()

label_erreur = tk.Label(fenetre, text="", fg="red")
label_erreur.pack()

fenetre.mainloop()