# -*- encoding=utf-8 -*-
import random
import numpy as np
import math

qt_individuos = 20
dim = 2

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


# def atualiza()

if __name__ == '__main__':
  x = [0, 0]
  pop = gera_populacao()
  #representa os individuos na forma [individuo, fitness]
  pop_fit = []
  for i in range(qt_individuos):
    fit = avalia(pop[i])
    pop_fit.append([pop[i], fit])

  selecionados = seleciona(pop_fit)

