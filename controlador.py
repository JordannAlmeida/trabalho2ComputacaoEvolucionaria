from constantes import Constantes
from algoritmoGenetico import AlgoritmoGenetico
from plotaGrafico import PlotaGrafico
import numpy

class Controlador:

    @staticmethod
    def inicializarOtimizacao(hasMapEscolhasUsuario):
        sucesso=0
        melhor=[]
        pior=[]
        resultados=[]
        media=None
        desvio=None

        melhores=[]
        for i in range (hasMapEscolhasUsuario[Constantes.numeroExecucao]):
            ag = AlgoritmoGenetico()
            ag.iniciarOtimizacao(hasMapEscolhasUsuario)
            melhor.append(max(ag.getListaMelhoresFitness())) 
            pior.append(max(ag.getListaPioresFitness()))
            resultados.append(ag.getMelhorIndividuo().getFitness())
            if max(ag.getListaMelhoresFitness())==27:
                sucesso=sucesso+1
            print("execucao: " + str(i) + "\n")
            if (hasMapEscolhasUsuario[Constantes.numeroExecucao] <=1 ):
                PlotaGrafico.plotarGrafico2d(numpy.arange(0, 50, 1), ag.getListaMelhoresFitness(), "teste")
        if (hasMapEscolhasUsuario[Constantes.numeroExecucao] >1 ):
            media = numpy.mean(resultados)
            desvio = numpy.std(resultados)
            PlotaGrafico.plotarGrafico2d(numpy.arange(0, 100, 1), melhor, Controlador.getTituloGrafico(hasMapEscolhasUsuario, media, desvio), "./fig/ensaio_" + hasMapEscolhasUsuario[Constantes.ensaio], "Execuções")

    @staticmethod
    def getTituloGrafico (hasMapEscolhasUsuario, media, desvio):
        return "Ensaio: " + hasMapEscolhasUsuario[Constantes.ensaio] + "\n" + "TC: " + hasMapEscolhasUsuario[Constantes.tipoCruzamento] + " E: " + hasMapEscolhasUsuario[Constantes.temElitismo] + "SL: " + hasMapEscolhasUsuario[Constantes.tipoSelecao] + " TM: " + hasMapEscolhasUsuario[Constantes.tipoMutacao] + " TxM: " + str(hasMapEscolhasUsuario[Constantes.taxaMutacao]) + " txC: " + str(hasMapEscolhasUsuario[Constantes.taxaCruzamento]) + " NI: " + str(hasMapEscolhasUsuario[Constantes.numeroIndividuos]) + " NG: " + str(hasMapEscolhasUsuario[Constantes.numeroGeracao]) + " nExec: " + str(hasMapEscolhasUsuario[Constantes.numeroExecucao]) + "\n" + "media: " + str(media) + " desvio: " + str(desvio)
