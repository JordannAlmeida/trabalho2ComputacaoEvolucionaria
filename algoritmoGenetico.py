import random
from constantes import Constantes
from individuo import Individuo
from metricasPopulacao import MetricasPopulacao

class AlgoritmoGenetico:

    def __init__(self):
       self.melhorIndividuo = None
       self.elite = None
       self.piorIndividuo = None
       self.listMelhoresFitness = []
       self.listPioresFitness = [] 

    def getMelhorIndividuo(self):
        return self.melhorIndividuo

    def getElite(self):
        return self.elite
    
    def setElite(self,melhorIndividuo):
        elite=melhorIndividuo

    
    
    def getListaPioresFitness(self):
        return self.listPioresFitness
    
    def getPiorIndividuo(self):
        return self.piorIndividuo

    def getMediaPopulacao(self):
        return self.mediaPopulacao
    
    def getDesvioPadrao(self):
        return self.desvioPadrao
    
    def getListaMelhoresFitness(self):
        return self.listMelhoresFitness


    #desenvolvido em sala, recebe um vetor com o fitness
    #A lista de avaliacoes deve estar em ordem crescente
    #retorna o índice dos pais nessa lista
    def giraRoleta(self, listaDeAvaliacao):
        soma=sum(listaDeAvaliacao,0)
        s=random.randint(0,soma)
        i=len(listaDeAvaliacao) -1
        aux=listaDeAvaliacao[i]
        while aux < s:
            i=i-1
            aux=aux+listaDeAvaliacao[i]
        individuo=i
        return individuo

    def selecaoDosPaisRoleta(self, listaDeAvaliacao):
        pai1=self.giraRoleta(listaDeAvaliacao)
        pai2=self.giraRoleta(listaDeAvaliacao)
        pais=[pai1,pai2]
        return pais

    #Conferir esse método (não tenho certeza se é assim que ele funciona)
    #Dar uma olhada em: http://www.inf.ufpr.br/aurora/tutoriais/Ceapostila.pdf
    #página 10 fig. 4
    def selecaoDosPaisTorneio(self, listaDeAvaliacao):
        pos1=random.randint(0,len(listaDeAvaliacao)-1)
        pos2=random.randint(0,len(listaDeAvaliacao)-1)
        pai1=listaDeAvaliacao[pos1]
        pai2=listaDeAvaliacao[pos2]     
        pais=[]
        if pai1>pai2:
            pais=pos1
        if pai1<=pai2:
            pais=pos2
        return pais

    #Recebe um vetor de Individuos (pais) e um int
    #retorna um vetor de Individuos (filhos)
    def cruzamentoUmPonto(self, pais,txCruzamento):
        pai1=pais[0]
        pai2=pais[1]
        combinacaoPai1=pai1.getCombinacao()
        combinacaoPai2=pai2.getCombinacao()
        tam1=len(combinacaoPai1)
        tam2=len(combinacaoPai2)
        filhos=pais
        cruz=random.randint(0,100)
        if cruz<txCruzamento:
            filho1=Individuo()
            filho2=Individuo()
            crossOver=random.randint(1,(tam1-2))
            combinacaoFilho1=[*combinacaoPai1[:crossOver],*combinacaoPai2[crossOver:tam2]]
            combinacaoFilho2=[*combinacaoPai2[:crossOver],*combinacaoPai1[crossOver:tam1]]
            filho1.setCombinacao(combinacaoFilho1)
            filho2.setCombinacao(combinacaoFilho2)
            filhos=[filho1,filho2]
        return filhos

    #Recebe um vetor de Individuos (pais) e um int
    #retorna um vetor de Individuos (filhos)
    def cruzamentoUniforme(self, pais,txCruzamento):
        #declaração dos pais e filhos
        pai1=pais[0]
        pai2=pais[1]
        combinacaoPai1=pai1.getCombinacao()
        combinacaoPai2=pai2.getCombinacao()
        tam1=len(combinacaoPai1)
        tam2=len(combinacaoPai2)
        filhos=pais
        i=0
        aux=[]
        #sorteio dos genes
        while i<tam1:
            aux.append(random.randint(0,1))
            i=i+1 
        cruz=random.randint(0,100)
        if cruz<txCruzamento:
            i=0
            filho1=Individuo()
            filho2=Individuo()
            combinacaoFilho1=[]
            combinacaoFilho2=[]
            
            while i<tam1:
                if aux[i]==0:
                    combinacaoFilho1.append(combinacaoPai1[i])
                    combinacaoFilho2.append(combinacaoPai2[i])
                elif aux[i]==1:
                    combinacaoFilho1.append(combinacaoPai2[i])
                    combinacaoFilho2.append(combinacaoPai1[i])
                i=i+1
            filho1.setCombinacao(combinacaoFilho1)
            filho2.setCombinacao(combinacaoFilho2)
            filhos=[filho1,filho2]
        return filhos

    #Recebe um Individuo (filho) e um double (taxaMutacao)
    #retorna um Individuo (filho)
    def mutacaoBitABit(self, filho,taxaMutacao):
        i=0
        combinacaoFilho=filho.getCombinacao()
        while (i<len(combinacaoFilho)-1):
            r=random.uniform(0,100)
            if r<taxaMutacao:        
                if combinacaoFilho[i]==0:
                    combinacaoFilho[i]=1
                elif combinacaoFilho[i]==1:
                    combinacaoFilho[i]=0
                i=i+1
        filho.setCombinacao(combinacaoFilho)
        return filho

    #Recebe um Individuo (filho) e um double (taxaMutacao)
    #retorna um Individuo (filho)
    def mutacaoBitAleatorio(self, filho, taxaMutacao):
        r=random.uniform(0,100)
        combinacaoFilho=filho.getCombinacao()
        if r<taxaMutacao:
            bit=random.randint(0,len(filho.getCombinacao())-1)
            if combinacaoFilho[bit]==0:
                combinacaoFilho[bit]=1
            elif combinacaoFilho[bit]==1:
                combinacaoFilho[bit]=0
            filho.setCombinacao(combinacaoFilho)
        return filho
    
    #metodo de execução do algoritimo genetico
    def iniciarOtimizacao(self, hasMapEscolhasUsuario):
        numeroIndividuos = int(hasMapEscolhasUsuario[Constantes.numeroIndividuos])
        populacao = [Individuo() for i in range(0, numeroIndividuos)]
        self.melhorIndividuo = MetricasPopulacao.melhorIndividuoPopulacao(populacao)
        self.piorIndividuo = MetricasPopulacao.piorIndividuoPopulacao(populacao)
        filhos = [1,2]
        positionPais = []
        for i in range(0, int(hasMapEscolhasUsuario[Constantes.numeroGeracao])):
            populacao = MetricasPopulacao.rankearPopulacao(populacao)
            
            listaFitness = MetricasPopulacao.getListaFitness(populacao)

            newPopulacao=[]
            if (hasMapEscolhasUsuario[Constantes.temElitismo] == "s"):
                j=2
            else:
                j=0

            while j < (numeroIndividuos/2):
                positionPais = []
                #Verificar metodo de selecao:
                if(hasMapEscolhasUsuario[Constantes.tipoSelecao] == "r"):
                    positionPais = self.selecaoDosPaisRoleta(listaFitness)
                else:
                    positionPais.append(self.selecaoDosPaisTorneio(listaFitness))
                    positionPais.append(self.selecaoDosPaisTorneio(listaFitness))
                
                pais = [populacao[positionPais[0]], populacao[positionPais[1]]] 
            

                #Verificar metodo de cruzamento:
                if(hasMapEscolhasUsuario[Constantes.tipoCruzamento] == "p"):
                    filhos = self.cruzamentoUmPonto(pais, hasMapEscolhasUsuario[Constantes.taxaCruzamento])
                else:
                    filhos = self.cruzamentoUniforme(pais, hasMapEscolhasUsuario[Constantes.taxaCruzamento])
            
                #verifica tipo mutacao:
                
                if(hasMapEscolhasUsuario[Constantes.tipoMutacao] == "a"):
                    filhos[0] = self.mutacaoBitAleatorio(filhos[0], hasMapEscolhasUsuario[Constantes.taxaMutacao])
                    filhos[1] = self.mutacaoBitAleatorio(filhos[1], hasMapEscolhasUsuario[Constantes.taxaMutacao])
                else:
                    filhos[0] = self.mutacaoBitABit(filhos[0], hasMapEscolhasUsuario[Constantes.taxaMutacao])
                    filhos[1] = self.mutacaoBitABit(filhos[1], hasMapEscolhasUsuario[Constantes.taxaMutacao])
            
                
                newPopulacao.append(filhos[0])
                newPopulacao.append(filhos[1])
                j=j+1
            
            populacao = newPopulacao if hasMapEscolhasUsuario[Constantes.temElitismo] == "n" else [*populacao[:1], *newPopulacao] 
                
    # def atualizarPopulacao(self, filhos):
    #     newPopulacao=filhos
    #     return newPopulacao
    
            #metricas
            self.melhorIndividuo = MetricasPopulacao.melhorIndividuoPopulacao(populacao)
            self.piorIndividuo = MetricasPopulacao.piorIndividuoPopulacao(populacao)
            self.listMelhoresFitness.append(self.melhorIndividuo.getFitness())
            self.listPioresFitness.append(self.piorIndividuo.getFitness())
