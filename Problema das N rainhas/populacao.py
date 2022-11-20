import numpy as np
import random
import copy
from individuo import Individuo


class Populacao:

    def __init__(self, n, n_individuo, p_crossover, p_mutacao, elitismo=False, individuos=[]):
        self.n = n
        self.n_individuo = n_individuo
        self.p_crossover = p_crossover
        self.p_mutacao = p_mutacao
        self.elitismo = elitismo
        self.individuos = individuos or self.gerarPopulacao()
        self.probabilidades = self.RoletaViciada()
        self.popIntermediaria = self.Selecao()
        self.popIntermediaria = self.Crossover_Mutacao()

    def gerarPopulacao(self):
        individuos = []
        for _ in range(self.n):
            individuos.append(Individuo(self.n_individuo))
        return individuos

    def RoletaViciada(self):
        if hasattr(self, 'probabilidades'):
            return self.probabilidades
        probabilidades, media = [], []
        total = 0
        self.melhorIndividuo = copy.deepcopy(self.individuos[0])

        for individuo in self.individuos:
            total += individuo.fitness
            probabilidades.append(total)
            media.append(individuo.fitness)

            if individuo.fitness > self.melhorIndividuo.fitness:
                self.melhorIndividuo = copy.deepcopy(individuo)

        self.media = np.mean(media)
        probabilidades = list(
            map(lambda x: x/total, probabilidades))
        self.probabilidades = probabilidades
        return probabilidades

    def Selecao(self):
        individuos = []
        for _ in range(self.n):

            random = np.random.random()
            for i in range(len(self.probabilidades)):
                if self.probabilidades[i] > random:
                    individuos.append(self.individuos[i])
                    break

        if self.elitismo:
            individuos[0] = copy.deepcopy(self.melhorIndividuo)

        return individuos

    def Crossover_Mutacao(self):
        individuos = []
        for i in range(0, self.n, 2):
            if np.random.random() < self.p_crossover:
                # Crossover
                corte1 = random.randint(0, self.n_individuo-1)
                corte2 = random.randint(corte1+1, self.n_individuo)
                pai1 = self.popIntermediaria[i].rainhas
                pai2 = self.popIntermediaria[i+1].rainhas
                filho1 = pai1[:corte1] + pai2[corte1:corte2]+pai1[corte2:]
                filho2 = pai2[:corte1]+pai1[corte1:corte2]+pai2[corte2:]
                novoIndividuo1 = Individuo(self.n_individuo, filho1)
                novoIndividuo2 = Individuo(self.n_individuo, filho2)
                # Mutação
                individuos.append(self.Mutacao(novoIndividuo1))
                individuos.append(self.Mutacao(novoIndividuo2))
            else:
                individuos.append(self.Mutacao(self.popIntermediaria[i]))
                individuos.append(self.Mutacao(self.popIntermediaria[i + 1]))

        if self.elitismo:
            individuos[0] = copy.deepcopy(self.melhorIndividuo)

        return individuos

    def Mutacao(self, individuo):
        if np.random.random() < self.p_mutacao:
            select = np.random.randint(self.n_individuo)
            individuo.rainhas[select] = np.random.randint(
                1, self.n_individuo + 1)
            return Individuo(
                self.n_individuo, individuo.rainhas)
        return individuo
