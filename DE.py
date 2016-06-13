import csv
from random import randint as rint
'''Parametros: gen= numero de geracoes
               f= constante real entre 0 e 2'''
def DE(gen,f):

    base = csv.reader(open('base.txt'), delimiter= ' ')
    entrada,pais, ngen =[], [], 1
    for i in base:
        aux = []
        for j in i:
            aux.append(float(j))
        entrada.append(aux)
    pais = entrada
    while ngen<gen:# condicao de parada
        for i in range(len(pais)):
            if (i==len(pais)-1): # para o penultimo elementos
                filho = crossover(pais[i], pais[i + 1])
            elif (i==len(pais)): # utiliza o primeiro elemento na multacao do ultimo
                filho = crossover(pais[i], pais[0])
            else:
                if rint(0,1)==0:# Escolhe aleatoriamente entre crossover ou mutacao
                    filho = mutacao(pais[i], pais[i+1], pais[i+2], f)
                else:
                    filho = crossover(pais[i], pais[i+1])

            ngen +=1




def crossover(pai1, pai2):
    filho = []
    for i in range(len(pai1)-1):
        if rint(0,1)==0:
            filho.append(pai1[i])
        else:
            filho.append(pai2[i])
    return (filho)

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

'''for j in range(len(entrada[0])-1):
                print(entrada[i][j])'''
