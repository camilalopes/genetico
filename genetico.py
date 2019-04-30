# -*- encoding=utf-8 -*-
import random
import numpy as np
import math

qt_execucoes = 30
qt_individuos = 20
dim = 2
taxa_cruzamento = 0.9
taxa_mutacao = 0.3
taxa_perturbacao = 0.05
qt_interacoes = 100

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
  # fitness = 1/(1+(rastrigin(X)))
  fitness = 1/rastrigin(X)+0.0001
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

def cruza(selecionados):
  alpha = 0.9
  filhos = []
  while len(filhos) < qt_individuos:
    pai = random.randint(0, qt_individuos-1)
    mae = random.randint(0, qt_individuos-1)
    terao_filhos = random.uniform(0, 1)
    if terao_filhos < taxa_cruzamento:
      filho1 = []
      filho2 = []
      for d in range(dim):
        filho1.append(alpha*selecionados[pai][d] + (1-alpha)*selecionados[mae][d])
        filho2.append((1-alpha)*selecionados[pai][d] + (alpha)*selecionados[mae][d])
      
      #calcula novo fitness
      fit = avalia(filho1)
      filho1.append(fit)
      fit = avalia(filho2)
      filho2.append(fit)
      #adiciona na lista de filhos
      filhos.append(filho1)
      filhos.append(filho2)
  return filhos

def cruza2(selecionados):
  filhos = []
  while len(filhos) < qt_individuos:
    pai = random.randint(0, qt_individuos-1)
    mae = random.randint(0, qt_individuos-1)
    terao_filhos = random.uniform(0, 1)
    if terao_filhos < taxa_cruzamento:
      filho1 = []
      filho2 = []
      ponto_corte = random.randint(0, dim-1)
      for i in range(ponto_corte+1):
        filho1.append(selecionados[pai][i])
        filho2.append(selecionados[mae][i])
      for i in range(ponto_corte+1, dim):
        filho1.append(selecionados[mae][i])
        filho2.append(selecionados[pai][i])
      #calcula novo fitness
      fit = avalia(filho1)
      filho1.append(fit)
      fit = avalia(filho2)
      filho2.append(fit)
      #adiciona na lista de filhos
      filhos.append(filho1)
      filhos.append(filho2)
  return filhos

def cruza3(selecionados):
  alpha = 0.9
  filhos = []
  while len(filhos) < qt_individuos:
    pai = random.randint(0, qt_individuos-1)
    mae = random.randint(0, qt_individuos-1)
    terao_filhos = random.uniform(0, 1)
    if terao_filhos < taxa_cruzamento:
      filho1 = []
      for d in range(dim):
        #avalia quem tem o melhor fitness
        if selecionados[mae][dim] > selecionados[pai][dim]:
          filho1.append(alpha*selecionados[mae][d] + (1-alpha)*selecionados[pai][d])
        else:
          filho1.append((1-alpha)*selecionados[mae][d] + (alpha)*selecionados[pai][d])
      #calcula novo fitness
      fit = avalia(filho1)
      filho1.append(fit)
      #adiciona na lista de filhos
      filhos.append(filho1)
  return filhos

def muta(filhos):
  mutados = []
  for _ in range(math.floor(taxa_mutacao*qt_individuos)):
    pos = random.randint(0, qt_individuos-1)
    dimensao = random.randint(0, dim-1)
    operacao = random.randint(0, 1)

    ind = filhos[pos][0:dim]
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

def sort_fit(val):
  return val[dim]

def atualiza(selecionados, mutados, melhor):
  nova_pop = []
  nova_pop += selecionados
  nova_pop += mutados
  nova_pop.append(melhor)
  #ordena os individuos pelo fitness
  nova_pop.sort(key = sort_fit, reverse = True)
  return nova_pop[0:qt_individuos]

if __name__ == '__main__':

  for _ in range(qt_execucoes):
    pop = gera_populacao()
    #representa os individuos na forma [individuo, fitness]
    pop_fit = pop
    for i in range(qt_individuos):
      fit = avalia(pop[i])
      pop_fit[i].append(fit)

    soma = 0.0
    for i in range(qt_interacoes):
      pop_fit.sort(key = sort_fit, reverse = True)
      # print("pop: ", pop_fit)
      melhor = pop_fit[0]
      selecionados = seleciona(pop_fit)
      # print("selecionados: ", selecionados)
      filhos = cruza3(selecionados)
      # print("filhos: ", filhos)
      mutados = muta(filhos)
      # print("mutados: ", mutados)
      nova_pop = atualiza(filhos, mutados, melhor)
      # print("nova pop: ", nova_pop)
      pop_fit = nova_pop
    print(nova_pop[0], " valor: ", rastrigin(nova_pop[0][0:dim]))
    soma += rastrigin(nova_pop[0][0:dim])
  print("media: ", soma/qt_execucoes)