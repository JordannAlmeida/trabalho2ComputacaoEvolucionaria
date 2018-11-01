import numpy as np

class MetricasPopulacao:
    
    @staticmethod
    def getListaFitness(populacao):
        return [individuo.getFitness() for individuo in populacao]

    @staticmethod
    def mediaFitnessPopulacao(populacao):
        listaFitness = MetricasPopulacao.getListaFitness(populacao)
        return np.mean(listaFitness)        

    @staticmethod
    def desvioPadraoFitnessPopulacao(populacao):
        listaFitness = MetricasPopulacao.getListaFitness(populacao)
        return np.std(listaFitness)
    
    @staticmethod
    def melhorIndividuoPopulacao(populacao):
        listaFitness = MetricasPopulacao.getListaFitness(populacao)
        index = listaFitness.index(max(listaFitness))
        return populacao[index]

    @staticmethod
    def piorIndividuoPopulacao(populacao):
        listaFitness = MetricasPopulacao.getListaFitness(populacao)
        index = listaFitness.index(min(listaFitness))
        return populacao[index]

    @staticmethod
    def rankearPopulacao(populacao):
        newPopulacao = sorted(populacao, key=lambda individuo: individuo.getFitness(), reverse=True)
        for j in range(0, len(newPopulacao)-1):
            newPopulacao[j].setRank(j+1)
        return newPopulacao