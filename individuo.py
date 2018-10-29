import numpy as np

class Individuo:
    combinacao = []
    rank = 0
    fitness = 0

    def __init__(self):
        self.gerarCombinacao()
        self.fitness = -100 #inicializa com valor baixo

    def gerarCombinacao(self):
        self.combinacao = np.random.choice([0, 1], 36)

    def getCombinacao(self):
        return self.combinacao