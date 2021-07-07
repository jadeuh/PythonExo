# -*-coding:Utf-8 -*

print("Hello")
#RQ: on surligne et on fait Ctrl+/ pour mettre en commentaire et que ca ne Run pas depuis le début
#RQ: On utilise des boucles while lorsque le nombre d'itérations n'est pas connu et des boucles for lorsque le nombre d'itérations est connu :



# 1. Écrire un algorithme qui demande un entier positif, et le rejette tant que le nombre saisi n’est pas conforme.

# i= -1
# while (i < 0) :
#     i = int(input("Veuillez saisir un entier positif : "))
#     if i < 0 :
#         print( i, "est négatif donc non conforme")
# print(i, "est positif, tout est ok !")



# 2. Écrire un algorithme qui demande 10 entiers, compte le nombre d’entiers positifs saisis, et affiche ce résultat.

# compteur = 0
# for i in range(10):               # équivalent à for i in (0,1,2,3,4,5,6,7,8,9):
#     a = int(float(input("Veuillez saisir un entier positif ou négatif : ")))
#     if a >=0 :
#         compteur = compteur +1
# print("Le nb d'entier positif saisi est", compteur)



# 3. Écrire un algorithme qui demande des entiers positifs à l’utilisateur, les additionne, et qui s’arrête en affichant le
# résultat dès qu’un entier négatif est saisi.

# i = 1
# somme = 0
# while (i >= 0) :
#     i = int(float(input("Veuillez saisir un entier positif : ")))
#     if i >= 0 :
#         somme += i
#     if i < 0 :
#         break
# print("La somme des entiers positifs est", somme)


# 4. Modifier ce dernier algorithme pour afficher la moyenne de la série d’entiers positifs saisis.

i = 1                             # i est l'entrée de l'utilisateur
somme = 0
nb_iteration = 0
while (i >= 0) :
     i = int(float(input("Veuillez saisir un entier positif : ")))
     if i >= 0 :
         somme += i
         nb_iteration = nb_iteration + 1
     if i < 0 :
         break
moyenne = somme / nb_i
print("La moyenne des entiers positifs est ", moyenne)



