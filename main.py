colonne = int(input("Choisir une colonne :"))
ligne = int(input("Chosir une ligne :"))

if colonne==4 and ligne==4:
    print("Touché")
elif colonne==4 or ligne==4:
    print("En vue")
else:
     print("A l'eau")