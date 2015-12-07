#
# Algoritmo Genético Binário
#
# Enrico Navarro \ navarrolima_enrico@hotmail.com
# Lucas Costa
#

import random

def gerarpop():
    lista = list(range(-10,11))
    pop = random.sample(lista,4)
    x = 0
    while(x < len(pop)):
        if(pop[x] < 0):
            b = bin(pop[x])[:3]
            a = bin(pop[x])[3:].zfill(4)
            pop[x] = b + a
            pass
        else:
            b = bin(pop[x])[:2]
            a = bin(pop[x])[2:].zfill(4)
            pop[x] = b + a
            pass
        x += 1
        pass
    return pop

def fx(x):
    result = x**2 - 3*x +4
    return result

def avaliacaoinicial(pop):
    apt = []
    for i in pop:
        x = int(i,2)
        apt.append([fx(x),i])
        pass
    apt.sort()
    return apt

def avaliacao(pop):
    apt = []
    for i in pop:
        x = int(i[1],2)
        apt.append([fx(x),i])
        pass
    apt.sort()
    return apt

def selecao(apt):
    sel = random.sample(apt,4)
    sel.sort()
    sel = sel[:2]
    return sel

def crossover(pop):
    taxa = 0.6
    novapop = []
    x = 0
    while(x < len(pop)):
        pais = [pop[x][1], pop[x+1][1]]
        novapop.append(pais[0])
        novapop.append(pais[1])
        r = random.uniform(0.0,1.0)
        if(r < taxa):
            filhos = crosstrue(pais)
            pass
        else:
            filhos = [pais[0], pais[1]]
            pass
        for i in filhos:
            novapop.append(i)
            pass
        x += 2
        pass
    return novapop

def crosstrue(pais):
    filho1 = pais[0][:-2] + pais[1][-2:]
    filho2 = pais[1][:-2] + pais[0][-2:]
    return [filho1,filho2]

def mutacao(pop):
    for i in pop:
        for x in i:
            if(random.randint(1,100) == 1):
                if(x == '1'):
                    x = '0'
                    pass
                else:
                    x = '1'
                    pass
                pass
            pass
        pass
    return pop

def main():
    geracao = 0
    pop = gerarpop()
    apt = avaliacaoinicial(pop)
    while(geracao < 50):
        pop = selecao(apt)
        pop = crossover(pop)
        pop = mutacao(pop)
        apt = avaliacaoinicial(pop)
        geracao += 1
        pass
    print("=================== Resultado ===================\n")
    for i in apt:
        print("Elemento: " + str(int(i[1],2)) + " Resultado na funcao: " + str(i[0]) +".\n")
        pass
    return
    
main()
