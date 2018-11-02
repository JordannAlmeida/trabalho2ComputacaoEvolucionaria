import numpy as np

from funcaoCusto import FuncaoCusto

class Individuo:
    

    def __init__(self):
        self.gerarCombinacao()
        self.recalcularFitness()
        self.rank = 0

    def gerarCombinacao(self):
        self.combinacao = np.random.choice([0, 1], 36)

    def getCombinacao(self):
        return self.combinacao
    
    def setCombinacao(self, combinacao):
        self.combinacao = combinacao
        self.recalcularFitness()

    def getFitness(self):
        return self.fitness

    def recalcularFitness(self):
        self.fitness = FuncaoCusto.funcaoPadrao(self)
    
    def getRank(self):
        return self.rank

    def setRank(self, newRank):
        self.rank = newRank