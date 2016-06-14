import csv
from random import randint as rint
'''Parametros: gen= numero de geracoes
               f= constante real entre 0 e 2'''
def DE(gen,f):

    base = csv.reader(open('base.txt'), delimiter= ' ')
    entrada,pais, ngen = [], [], 0
    for i in base:
        aux = []
        for j in i:
            aux.append(float(j))
        entrada.append(aux)
    pais = entrada
    cent1, cent2 = distancia(pais)
    for i in range(len(pais)):
        fit = fitness(pais[i], pais[cent1], pais[cent2])
        pais[i].append(fit)
    while ngen<gen:  # condicao de parada
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
        print(filhos)
        ngen += 1


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


def fitness(matriz, cent1, cent2):# informar as instancias nao os indices
    j=((matriz[0]-cent1[0])**2 + (matriz[1]-cent1[1])**2) + ((matriz[0]-cent2[0])**2 + (matriz[1]-cent2[1])**2)
    fit = 2*(j +0.1)
    return fit

'''Work in progress'''
DE(1,2)