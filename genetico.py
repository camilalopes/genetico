# -*- encoding=utf-8 -*-
import random
import numpy as np
import math

qt_individuos = 20
dim = 2
taxa_mutacao = 0.3
taxa_perturbacao = 0.05

#população inicial de 20 com individuos entre [-5.12, 5.12]
def rastrigin(X):
    n = len(X)
    A = 10
    f = (A * n) + sum([(xi**2 - A*np.cos(2*math.pi*xi)) for xi in X])
    return f

def gera_populacao():
  pop = []
  for _ in range(qt_individuos):
    x = []
    for _ in range(dim):
      xi = random.uniform(-5.12, 5.12)
      x.append(xi)
    pop.append(x)
  return pop

def avalia(X):
  fitness = -(rastrigin(X))
  return fitness

def seleciona(pop_fit):
  selecionados = []
  for _ in range(qt_individuos):
    #sorteia dois individuos
    pos1 = random.randint(0, qt_individuos-1)
    pos2 = random.randint(0, qt_individuos-1)
    #avalia o fitness
    if pop_fit[pos1][dim] > pop_fit[pos2][dim]:
      selecionados.append(pop_fit[pos1])
    else:
      selecionados.append(pop_fit[pos2])
  return selecionados

def muta(selecionados):
  mutados = []
  for _ in range(math.floor(taxa_mutacao*qt_individuos)):
    pos = random.randint(0, qt_individuos-1)
    dimensao = random.randint(0, dim-1)
    operacao = random.randint(0, 1)

    ind = selecionados[pos][0:dim]
    #realiza mutacao
    if operacao == 0:
      ind[dimensao] -= (taxa_mutacao*ind[dimensao])
    else:
      ind[dimensao] += (taxa_mutacao*ind[dimensao])
    #calcula novo fitness
    fit = avalia(ind)

    ind.append(fit)
    mutados.append(ind)
  return mutados

# def atualiza()

if __name__ == '__main__':
  x = [0, 0]
  pop = gera_populacao()
  #representa os individuos na forma [individuo, fitness]
  pop_fit = pop
  for i in range(qt_individuos):
    fit = avalia(pop[i])
    pop_fit[i].append(fit)
    
  selecionados = seleciona(pop_fit)
  mutados = muta(selecionados)