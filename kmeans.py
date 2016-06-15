import csv
from DE import distancia


def k_means(pais, centroid1, centroid2):

    cluster1 = []
    cluster2 = []
    for i in range(len(pais)):
        if calc_dist(pais[i], centroid1) > calc_dist(pais[i], centroid2):
            pais[2] = 1
            centroid1 = att_dist(pais[i], centroid1, cluster1)
        else:  # classe -1
            pais[2] = -1
            centroid1 = att_dist(pais[i], centroid2)

    for i in range(10): # 10 iteracoes
        for i in range(len(pais)):
            if calc_dist(pais[i], centroid1) > calc_dist(pais[i], centroid2):# classe 1
                if pais[2] == 1:
                    att_dist(pais[i], centroid1, cluster1)
                else:
                    att_dist(pais[i], centroid1, cluster1)
                    att_dist2(pais[i], centroid2, cluster2)
            else: # classe -1
                if pais[2] == -1:
                    att_dist(pais[i], centroid2, cluster2)
                else:
                    att_dist(pais[i], centroid2, cluster2)
                    att_dist2(pais[i], centroid1, cluster1)
    return pais


def calc_dist(pai, cent1): #calcula a distancia entre a instancia e o centroid
    dist = ((pai[0]-cent1[0])**2 + (pai[1]-cent1[1])**2)**1/2
    return dist


def att_dist(pai, cent, cluster): # adiciona o elemento ao cluster
    novo = []
    cluster.append(pai)# adiciona o elemento ao cluster para atualizar o valor
    for i in range(len(cluster)):
        cent[0] = cluster[i][0] + cent[0]
        cent[1] = cluster[i][1] + cent[1]
    novo.append(cent[0]/len(cluster))
    novo.append(cent[1] / len(cluster))
    return novo


def att_dist2(pai, cent, cluster): # remove o elemento do cluster caso ele tenha sido classificado errado
    novo = []
    cluster.remove(pai)  # adiciona o elemento ao cluster para atualizar o valor
    for i in range(len(cluster)):
        cent[0] = cluster[i][0] + cent[0]
        cent[1] = cluster[i][1] + cent[1]
    novo.append(cent[0] / len(cluster))
    novo.append(cent[1] / len(cluster))
