import csv
from random import randint as rint
from sklearn.preprocessing import normalize
'''Parametros: gen= numero de geracoes
               f= constante real entre 0 e 2
               Os resultados exibidos estão normalizados
'''


def DE(gen,f):
    output = open('saida.txt', 'w')
    result = open('result.txt', 'w')
    base = csv.reader(open('base.txt'), delimiter= ' ')
    entrada,pais, ngen = [], [], 0
    for i in base:
        aux = []
        for j in i:
            aux.append(float(j))
        entrada.append(aux)
    pais = entrada
    cent1, cent2 = distancia(pais)
    for i in range(len(pais)): # calcula o fitness dos pais
        fit = fitness(pais[i], pais[cent1], pais[cent2])
        pais[i].append(fit)
    while ngen < gen:  # condicao de parada(nº de gerações)
        filhos = []
        for i in range(len(pais)):
            if i == len(pais)-1:  # para o ultimo elementos
                filho = crossover(pais[i], pais[0])
            elif i == len(pais)-2:  #para o penultimo
                filho = crossover(pais[i], pais[i+1])
            else:
                if rint(0, 1) == 0:  # Escolhe aleatoriamente entre crossover ou mutacao
                    filho = mutacao(pais[i], pais[i+1], pais[i+2], f)
                else:
                    filho = crossover(pais[i], pais[i+1])
            filho.append(fitness(filho, pais[cent1], pais[cent2]))
            filhos.append(filho)
        pais = selecao(pais,filhos)
        cent1, cent2 = distancia(pais)# atualiza os centroides apos cada geracao
        ngen += 1
    pais = normalize(pais)
    pais = k_means(pais,pais[cent1], pais[cent2])
    for i in pais:
        output.write(str(i[-1]) + '\n')
        result.write(str(i) + '\n')


def crossover(pai1, pai2):
    filho = []
    for i in range(len(pai1)-1):
        if rint(0,1)==0:
            filho.append(pai1[i])
        else:
            filho.append(pai2[i])
    return filho


def mutacao(pai, vizinho1, vizinho2, f):
    filho = []
    for i in range(len(pai)-1):
        filho.append(pai[i]+f*(vizinho1[i]-vizinho2[i]))

    return filho


def selecao(pais, filhos):
    saida = []
    for i in range (len(pais)):
        if pais[i][-1]>filhos[i][-1]:
            saida.append(pais[i])
        else:
            saida.append(filhos[i])
    return saida


def distancia(matriz):# escolhe aleatoriamente os centroides
    while True:
        nun=rint(0,len(matriz)-1)
        if matriz[nun][2]==1:
            break
    while True:
        nun2 = rint(0, len(matriz) - 1)
        if matriz[nun2][2] == -1:
            break
    return nun, nun2


def fitness(matriz, cent1, cent2):# j0 = 0.1 k=2
    j = ((matriz[0]-cent1[0])**2 + (matriz[1]-cent1[1])**2) + ((matriz[0]-cent2[0])**2 + (matriz[1]-cent2[1])**2)
    fit = 100//(j + 0.1)
    return fit


def k_means(pais, centroid1, centroid2):
    print(centroid1, centroid2)
    cluster1 = []
    cluster2 = []
    for i in range(len(pais)):
        if calc_dist(pais[i], centroid1) > calc_dist(pais[i], centroid2):
            pais[i][2] = 1
            centroid1 = att_dist(pais[i], centroid1, cluster1)
        else:  # classe -1
            print(len(pais))
            pais[i][2] = -1
            centroid1 = att_dist(pais[i], centroid2, cluster2)

    for i in range(10): # 10 iteracoes
        for i in range(len(pais)):
            if calc_dist(pais[i], centroid1) > calc_dist(pais[i], centroid2):# classe 1
                if pais[i][2] == 1:
                    att_dist(pais[i], centroid1, cluster1)
                else:
                    att_dist(pais[i], centroid1, cluster1)
                    att_dist2(pais[i], centroid2, cluster2)
            else: # classe -1
                if pais[i][2] == -1:
                    att_dist(pais[i], centroid2, cluster2)
                else:
                    att_dist(pais[i], centroid2, cluster2)
                    att_dist2(pais[i], centroid1, cluster1)
    return pais


def calc_dist(pai, cent1): #calcula a distancia entre a instancia e o centroid
    dist = ((pai[0]-cent1[0])**2 + (pai[1]-cent1[1])**2)
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
    try:
        cluster.remove(pai)  # remove o elemento ao cluster para atualizar o valor
    except:
        pass
    for i in range(len(cluster)):
        cent[0] = cluster[i][0] + cent[0]
        cent[1] = cluster[i][1] + cent[1]
    novo.append(cent[0] / len(cluster))
    novo.append(cent[1] / len(cluster))
    return novo

'''Work in progress'''
DE(5, 2)
