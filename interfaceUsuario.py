from constantes import Constantes
from algoritmoGenetico import AlgoritmoGenetico

class InterfaceUsuario:

    @staticmethod
    def inputsUsuario():
        qTipoCruzamento = ["Qual o tipo de cruzamento, ponto ou uniforme? (p / u) \n", Constantes.tipoCruzamento]
        qUtilizaElitsmo = ["Possui elitismo? (s / n) \n", Constantes.temElitismo]
        qSelecaoRoletaOuTorneio = ["Tipo de seleção: Roleta ou Torneio de 2 individuos? (r / t) \n", Constantes.tipoSelecao]
        qTipoMutacao = ["Qual o tipo de mutação, aleatória ou bit a bit? (a / b) \n", Constantes.tipoMutacao]
        qProbabilidaCruzamento = ["Qual a probabilidade de cruzamento? (0 a 100) \n", Constantes.taxaCruzamento]
        qProbabilidaMutacao = ["Qual a probabilidade de mutacao? (0 a 100) \n", Constantes.taxaMutacao]
        qNumeroDeIndividuos = ["Qual o numero de individuos? (somente número inteiro) \n", Constantes.numeroIndividuos]
        qNumeroGeracao = ["Qual o numero de gerações? (somente número inteiro) \n", Constantes.numeroGeracao]
        
        rTipoCruzamento = input(qTipoCruzamento[0])
        rUtilizaElitismo = input(qUtilizaElitsmo[0])
        rSelecaoRoletaOuTorneio = input(qSelecaoRoletaOuTorneio[0])
        rTipoMutacao = input(qTipoMutacao[0])
        rProbabilidadeMutacao = input(qProbabilidaMutacao[0])
        rProbabilidadeCruzamento = input(qProbabilidaCruzamento[0])
        rNumeroIndividuos = input(qNumeroDeIndividuos[0])
        rNumeroGeracao = input(qNumeroGeracao[0])

        HasMapEscolhasUsuario = { qTipoCruzamento[1]: rTipoCruzamento,
                                  qUtilizaElitsmo[1]: rUtilizaElitismo,
                                  qSelecaoRoletaOuTorneio[1]: rSelecaoRoletaOuTorneio,
                                  qTipoMutacao[1]: rTipoMutacao,
                                  qProbabilidaCruzamento[1]: rProbabilidadeCruzamento,
                                  qProbabilidaMutacao[1]: rProbabilidadeMutacao,
                                  qNumeroDeIndividuos[1]: rNumeroIndividuos,
                                  qNumeroGeracao[1]: rNumeroGeracao
        }
        InterfaceUsuario.inicializarOtimizacao(HasMapEscolhasUsuario)
    
    @staticmethod
    def inputsUsuarioComParametros(rTipoCruzamento, rUtilizaElitismo, rSelecaoRoletaOuTorneio, rTipoMutacao, rProbabilidadeMutacao, rProbabilidadeCruzamento, rNumeroIndividuos, rNumeroGeracao):
        HasMapEscolhasUsuario = { Constantes.tipoCruzamento: rTipoCruzamento,
                                  Constantes.temElitismo: rUtilizaElitismo,
                                  Constantes.tipoSelecao: rSelecaoRoletaOuTorneio,
                                  Constantes.tipoMutacao: rTipoMutacao,
                                  Constantes.taxaCruzamento: rProbabilidadeCruzamento,
                                  Constantes.taxaMutacao: rProbabilidadeMutacao,
                                  Constantes.numeroIndividuos: rNumeroIndividuos,
                                  Constantes.numeroGeracao: rNumeroGeracao
        }
        InterfaceUsuario.inicializarOtimizacao(HasMapEscolhasUsuario)

    @staticmethod
    def inicializarOtimizacao(hasMapEscolhasUsuario):
        ag = AlgoritmoGenetico()
        ag.iniciarOtimizacao(hasMapEscolhasUsuario)