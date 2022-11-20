import random
import math


class Individuo:

    def __init__(self, n, rainhas=[], binario=''):
        self.n = n
        self.bits = math.ceil(math.log(self.n, 2))
        if rainhas and not binario:
            self.rainhas = rainhas
            self.binario = self.convertDecimal2Binario()
        elif not rainhas and binario:
            self.binario = binario
            self.rainhas = self.convertBinario2Decimal()
        else:
            self.rainhas = self.gerarIndividuo()
            self.binario = self.convertDecimal2Binario()

        self.fitness = self.calcular_fitness()

    def gerarIndividuo(self):
        '''Função para gerar um tabuleiro com rainhas aleatórias.'''
        return [random.randint(1, self.n) for _ in range(self.n)]

    def convertBinario2Decimal(self):
        individuo = []
        for i in range(0, len(self.binario), self.bits):
            individuo.append(int(self.binario[i:i+self.bits], 2) + 1)
        return individuo

    def convertDecimal2Binario(self):
        binario = ''
        for e in self.rainhas:
            binario += format(e - 1, "b").zfill(self.bits)
        return binario

    def calcular_fitness(self):
        '''Calcula o fitness de um cromossomo'''
        ataques = 0
        max_ataques = self.n*(self.n-1)/2
        for i in range(self.n):
            for j in range(i + 1, self.n):
                if self.rainhas[i] == self.rainhas[j]:
                    ataques += 1
                elif self.rainhas[i] + (j - i) == self.rainhas[j]:
                    ataques += 1
                elif self.rainhas[i] - (j - i) == self.rainhas[j]:
                    ataques += 1
        self.adptacao = max_ataques - ataques
        return self.adptacao
