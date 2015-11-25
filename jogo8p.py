# Jogo 8Puzzle
#
# Enrico Navarro / navarrolima_enrico@hotmail.com / @enriconavarro
# Lucas Costa / @lucashcosta
#

import numpy
import random

def matriz(m):
    #Função generica para criação de matrizes 3x3
    matriz = numpy.zeros((3,3))
    x = 0
    j = 0
    count = 0
    while(count < len(m)):
        matriz[x][j] = m[count]
        if(j < 2):
            j += 1
            pass
        else:
            j = 0
            x += 1
            pass
        count += 1
        pass
    #print(matriz)
    return matriz

#Criação da Arvore de Resolucao
class tree(object):
    def __init__(self):
        self.data = None
        self.filhos = None

'''
#Criação da matriz randomica de estado inicial
def matrizrandomica():
    matriz = numpy.zeros((3,3))
    x = 1
    while(x <= 8):
        linha = random.randint(0,2)
        coluna = random.randint(0,2)
        if (matriz[linha][coluna] == 0.0):
            matriz[linha][coluna] = x
            x += 1
            pass
        pass
    print(matriz)
    return matriz
'''

def buscaprof(nodo,solucao):
    for i in nodo.filhos:
        nodofilho = buscaprof(i,solucao)
        if(nodofilho.data == solucao):
            return nodofilho
        pass
    if(nodo.data == solucao):
        return nodo
    else:
        return False

def main():
    #Criação da matriz solução
    solucao = matriz([1,2,3,8,0,4,7,6,5])

    #Criação da matriz de estado inicial
    e1 = matriz([8,6,0,5,2,1,3,4,7])

    #Criação da Arvore de Estados
    #raiz = arvoreinit()

    #Busca em profundidade
    #buscaprof(raiz,solucao)

main()
