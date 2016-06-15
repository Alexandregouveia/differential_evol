import csv
from DE import distancia


def k_means():
    base = csv.reader(open('base.txt'), delimiter= ' ')
    entrada,pais, ngen = [], [], 0
    for i in base:
        aux = []
        for j in i:
            aux.append(float(j))
        entrada.append(aux)
    pais = entrada
    cent1, cent2 = distancia(pais)
    centroid1 = pais[cent1]
    centroid2 = pais[cent2]
    for i in range(10): # 10 iteracoes
        for i in range(len(pais)):
            if calc_dist(pais[i], centroid1) > calc_dist(pais[i], centroid2):# classe 1
                pais[2] = 1
                centroid1 = att_dist(pais[i], centroid1)
            else: # classe -1
                pais[2] = -1
                centroid1 = att_dist(pais[i], centroid2)


def calc_dist(pai, cent1):
    dist = ((pai[0]-cent1[0])**2 + (pai[1]-cent1[1])**2)**1/2
    return dist


def att_dist(pai, cent):
    novo = []
    novo.append((pai[0] + cent[0])/2)
    novo.append((pai[1] + cent[1]) / 2)
    return novo
