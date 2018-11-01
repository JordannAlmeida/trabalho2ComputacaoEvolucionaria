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
    #retorna o índice dos pais nessa lista
    def giraRoleta(self, listaDeAvaliacao):
        soma=sum(listaDeAvaliacao,0)
        s=random.randint(0,soma)
        i=0
        aux=listaDeAvaliacao[i]
        while aux < s:
            i=i+1
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
    def selecaoDosPaisTorneio(self, listaDeAvaliacao,k):
        pos1=random.randint(0,len(listaDeAvaliacao)-1)
        pos2=random.randint(0,len(listaDeAvaliacao)-1)
        pai1=listaDeAvaliacao[pos1]
        pai2=listaDeAvaliacao[pos2]     
        r=random.uniform(0,1)
        pais=[]
        if r<k:
            if pai1>pai2:
                pais=pos1
            if pai1<=pai2:
                pais=pos2
        if r>=k:
            if pai1<pai2:
                pais=pos1
            if pai1>=pai2:
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
        if tam1!=tam2:
            filhos="impossível, tamanho diferente"
        if tam1==tam2:
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

        #geração dos filhos, com base nos genes sorteados
        if tam1!=tam2:
            filhos="impossível, tamanho diferente"
        if tam1==tam2:
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
                if aux[i]==1:
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
                if combinacaoFilho[i]==1:
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
            if combinacaoFilho[bit]==1:
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
            #Verificar metodo de selecao:
            if(hasMapEscolhasUsuario[Constantes.tipoSelecao] == "r"):
                positionPais = self.selecaoDosPaisRoleta(listaFitness)
            else:
                positionPais.append(self.selecaoDosPaisTorneio(listaFitness, 0.75))
                positionPais.append(self.selecaoDosPaisTorneio(listaFitness, 0.75))
            
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
            
            #Verifica se tem Elitismo:
            if hasMapEscolhasUsuario[Constantes.temElitismo] == "s":
                elite = MetricasPopulacao.melhorIndividuoPopulacao(populacao)
                #TODO: AJUSTARRR
                if elite.getRank() != 1:
                    populacao[elite.getRank()-1], populacao[0] = populacao[0], populacao[elite.getRank()-1]
                    elite = populacao[0]
                    print("EPAAAAAAAAAAAA!!!!!!!!!!!!!!!!!!!!!!!!!!\n")
                    print(elite.getRank())
                    print("\n")
                position = random.randint(1, numeroIndividuos-1)
                if filhos[0].getFitness() > elite.getFitness():
                    populacao[position] = filhos[0]
                if filhos[1].getFitness() > elite.getFitness():
                    populacao[position] = filhos[1]
            else:
                position1 = random.randint(0, numeroIndividuos-1)
                position2 = random.randint(0, numeroIndividuos-1)
                populacao[position1] = filhos[0]
                populacao[position2] = filhos[1]

            #metricas
            self.melhorIndividuo = MetricasPopulacao.melhorIndividuoPopulacao(populacao)
            self.piorIndividuo = MetricasPopulacao.piorIndividuoPopulacao(populacao)
            self.listMelhoresFitness.append(self.melhorIndividuo.getFitness())
            self.listPioresFitness.append(self.piorIndividuo.getFitness())
