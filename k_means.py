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
    cluster1 = []
    cluster2 = []
    for i in range(len(pais)):
        if calc_dist(pais[i], centroid1) > calc_dist(pais[i], centroid2):  # classe 1
            pais[2] = 1
            centroid1 = att_dist(pais[i], centroid1, cluster1)
        else:  # classe -1
            pais[2] = -1
            centroid1 = att_dist(pais[i], centroid2)

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


def att_dist(pai, cent, cluster):
    novo = []
    for i in range(len(cluster)):
        cent[0] = pai[0] + cent[0]
        cent[1] = pai[1] + cent[1]
    novo.append(cent[0]/len(cluster))
    novo.append(cent[1] / len(cluster))

    return novo

def att_dist2(pai, cent):
    cent[0] = pai[0]