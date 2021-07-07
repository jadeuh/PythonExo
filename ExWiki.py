# -*-coding:Utf-8 -*
#
# # Listes fournies au départ :
# t1 = [31,28,31,30,31,30,31,31,30,31,30,31]
# t2 = ['Janvier','Février','Mars','Avril','Mai','Juin',
#       'Juillet','Août','Septembre','Octobre','Novembre','Décembre']
#
# # Nouvelle liste à construire (vide au départ) :
# t3 = []
#
# # Boucle de traitement :
# i = 0
# while i < len(t1):
#     t3.append(t2[i])
#     t3.append(t1[i])
#     i = i + 1
#
# print(t3)

##########################################################################################################

# d = {"pommes" : 1, "oranges" : 3, "poires" : 2}
# e = {"poires" : 4, "raisins" : 5, "citrons" : 6}
# d.update(e)
#
#
# d["cerises"] = 5
# print(d)

#######################################################################################################

texte ="les saucisses et saucissons secs sont dans le saloir"
lettres ={}
for c in texte :
    lettres[c] = lettres.get(c,0) +1

# print(lettres)

lettres_triees = lettres.items()
lettres_triees.sort()
print(lettres_triees)


# nb = [17, 1, 45, 98, 16]
# nb.sort()
# print(nb)