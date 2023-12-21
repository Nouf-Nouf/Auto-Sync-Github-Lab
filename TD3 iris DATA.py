# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 08:16:35 2023

@author: nbouc
"""

import math
import csv 

L = open("iris.data")
Datas = list(csv.reader(L))

def knn(Fleur_inconnue, Dataset, k):
    Distances = []
    for i in range(len(Dataset)):
        d = math.sqrt((float(Fleur_inconnue[0]) - float(Dataset[i][0]))2 + (float(Fleur_inconnue[1]) - float(Dataset[i][1]))2 + (float(Fleur_inconnue[2]) - float(Dataset[i][2]))2 + (float(Fleur_inconnue[3]) - float(Dataset[i][3]))2)
        Distances.append((i, d))
    Distances.sort(key = lambda x: x[1])
    classes = dict()
    for i in range(k):
        if Dataset[Distances[i][0]][4] in classes:
            classes[Dataset[Distances[i][0]][4]] += 1
        else:
            classes[Dataset[Distances[i][0]][4]] = 1
    max = 0
    for i in classes:
        if classes[i] > max:
            max = classes[i]
            classe = i
    return classe

Ks = []
for k in range(1,150):
    erreurs = 0
    for i in Datas:
        D = Datas[:]
        D.remove(i)
        if knn(i, D, k) != i[4]:
            erreurs += 1
    Ks.append((k, erreurs))
Ks.sort(key = lambda x:x[1])
print(Ks)