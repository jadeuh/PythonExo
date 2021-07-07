# -*-coding:Utf-8 -*

print("Hello")
#RQ: on surligne et on fait Ctrl+/ pour mettre en commentaire et que ca ne Run pas depuis le début

#1 Écrire un algorithme qui demande un entier à l’utilisateur, teste si ce nombre est positif (>= 0) ou non, et affiche
#“positif” ou “négatif”.

# a=int(input("1.1 Veuillez rentrer un nombre entier : "))      #on met int pour le forcer a prendre en compte un nb
# if a>=0:
#     print("positif")
# else :
#     print("negatif")


#2. Écrire un algorithme qui demande un entier à l’utilisateur, teste si ce nombre est strictement positif, nul ou strictement
#négatif, et affiche ce résultat.

# a=int(input("1.2 Veuillez rentrer un nombre entier :\n"))          #/n pour le retour a la ligne
# if a>0:
#     print("strictement positif")
# elif a==0:
#     print("nul")
# else :
#     print("strictement negatif")


#3. Écrire un algorithme qui demande un réel à l’utilisateur et affiche sa valeur absolue (sans utiliser de fonction
#prédéfinie évidemment).

# a=float(input("1.3 Veuillez rentrer un nombre réel pour connaitre sa valeur absolue :\n"))
# if a<0 :
#     print(-a)
# else :
#     print(a)

#4. Écrire un algorithme qui demande un réel à l’utilisateur et l’arrondit à l’entier le plus proche (les x,5 seront arrondis
#à l’entier supérieur).

# a=float(input("1.4 Veuillez rentrer un nombre réel à arrondir :\n "))
# a_tronque=int(a)
# if a<0:
#     if a_tronque-a >= 0.5:
#         print(int(a)-1)
#     else :
#         print(int(a))
# elif a-a_tronque>=0.5 :
#     print(int(a_tronque+1))
# else :
#     print(int(a))

#5. Écrire un algorithme qui demande le numéro d’un mois et affiche le nombre jours que comporte ce mois (sans tenir
#compte des années bissextiles).

# mois=int(input("1.5 Veuillez rentrer un numéro de mois : "))
# if mois in [1,3,5,7,8,10,12] :
#     print("Ce mois a 31 jours")
# elif mois==2 :
#     print("Ce mois a 28 ou 29 jours")
# else :
#     print("Ce mois a 30 jours")

#6. Écrire un algorithme qui vérifie si une année est bissextile. On rappelle qu’il y a des années bissextiles tous les
#4 ans, mais la première année d’un siècle ne l’est pas (1800, 1900 n’étaient pas bissextiles) sauf tous les 400 ans
#(2000 était une année bissextile).

# annee=int(input("1.6 Veuillez rentrer une année pour savoir si elle est bissextile ou non : "))
# modulo=annee%4
# if (annee%4==0 and annee%100 !=0) or annee%400==0 :
#     print("L'année", annee, "est bissextile")
# else :
#     print("L'année", annee, "n'est pas bissextile")


#7. Écrire un algorithme qui demande une date sous la forme de 2 nombres entiers (numéro du jour et numéro du mois)
#et affiche la saison (ex : 12/02; hiver). On supposera que le premier jour de la saison est toujours le 21.

jour=int(input("1.7 Veuillez rentrer un jour entre 1 et 31 : "))
mois=int(input("Veuillez rentre un numero de mois : "))
if mois%3==0 and jour>=21 and mois!=12 :
    mois=mois+1
elif mois==12 and jour>=21 :
    mois=1
if mois==1 or mois==2 or mois==3 :
    print("Le", jour, "/", mois, "c'est l'hiver glaglagla !")
elif mois==4 or mois==5 or mois==6 :
    print("Le", jour, "/", mois, "c'est le printemps !")
elif mois==7 or mois==8 or mois==9 :
    print("Le", jour, "/", mois, "c'est l'été !")
elif mois==10 or mois==11 or mois==12 :
    print("Le", jour, "/", mois, "c'est l'automne !")