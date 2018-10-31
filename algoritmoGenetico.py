import random
from constantes import Constantes
from individuo import Individuo

class AlgoritmoGenetico:
    
    #desenvolvido em sala, recebe um vetor com o fitness
    #retorna o índice dos pais nessa lista
    def giraRoleta(listaDeAvaliacao):
        soma=sum(listaDeAvaliacao,0)
        s=random.randint(0,soma)
        i=1
        aux=listaDeAvaliacao[i]
        while aux < s:
            i=i+1
            aux=aux+listaDeAvaliacao[i]
        individuo=i
        return individuo

    def selecaoDosPaisRoleta(listaDeAvaliacao):
        pai1=giraRoleta(listaDeAvaliacao)
        pai2=giraRoleta(listaDeAvaliacao)
        pais=[pai1,pai2]
        return pais

    #Conferir esse método (não tenho certeza se é assim que ele funciona)
    #Dar uma olhada em: http://www.inf.ufpr.br/aurora/tutoriais/Ceapostila.pdf
    #página 10 fig. 4
    def selecaoDosPaisTorneio(listaDeAvaliacao,k):
        pos1=random.randint(0,len(listaDeAvaliacao))
        pos2=random.randint(0,len(listaDeAvaliacao))
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
    def cruzamentoUmPonto(pais,txCruzamento):
        pai1=pais[1]
        pai2=pais[2]
        combinacaoPai1=pai1.getCombinacao()
        combinacaoPai2=pai2.getCombinacao()
        tam1=len(pai1)
        tam2=len(pai2)
        filhos=[]
        if tam1!=tam2:
            filhos="impossível, tamanho diferente"
        if tam1==tam2:
            cruz=random.randint(0,100)
        if cruz<txCruzamento:
            filho1=Individuo()
            filho2=Individuo()
            crossOver=random.randint(1,(tam1-2))
            combinacaoFilho1=combinacaoPai1[0:crossOver]+combinacaoPai2[crossOver:tam2]
            combinacaoFilho2=combinacaoPai2[0:crossOver]+combinacaoPai1[crossOver:tam1]
            filho1.setCombinacao(combinacaoFilho1)
            filho2.setCombinacao(combinacaoFilho2)
            filhos=[filho1,filho2]
        return filhos

    #Recebe um vetor de Individuos (pais) e um int
    #retorna um vetor de Individuos (filhos)
    def cruzamentoUniforme(pais,txCruzamento):
        #declaração dos pais e filhos
        pai1=pais[1]
        pai2=pais[2]
        combinacaoPai1=pai1.getCombinacao()
        combinacaoPai2=pai2.getCombinacao()
        tam1=len(combinacaoPai1)
        tam2=len(combinacaoPai2)
        filhos=[]
        i=0
        aux=[]

        #sorteio dos genes
        while i<tam1:
            aux[i]=random.randint(0,1)
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
                    aux1[i]=combinacaoPai1[i]
                    aux2[i]=combinacaoPai2[i]
                if aux[i]==1:
                    aux1[i]=combinacaoPai2[i]
                    aux2[i]=combinacaoPai1[i]
                i=i+1
            filho1.setCombinacao(combinacaoFilho1)
            filho2.setCombinacao(combinacaoFilho2)
            filhos=[filho1,filho2]
        return filhos

    #Recebe um Individuo (filho)
    #retorna um Individuo (filho)
    def mutacaoBitABit(filho):
        bit=random.randint(0,len(filho)-1)
        combinacaoFilho=filho.getCombinacao()
        if combinacaoFilho[bit]==0:
            combinacaoFilho[bit]=1
        if combinacaoFilho[bit]==1:
            combinacaoFilho[bit]=0
        filho.setCombinacao(combinacaoFilho)
        return filho

    #Recebe um Individuo (filho)
    #retorna um Individuo (filho)
    def mutacaoBitAleatorio(filho):
        bit=random.randint(0,len(filho)-1)
        combinacaoFilho=filho.getCombinacao()
        combinacaoFilho[bit]=random.randint(0,1)
        filho.setCombinacao(combinacaoFilho)
        return filho
    
    #metodo de execução do algoritimo genetico
    def iniciarOtimizacao(self, hasMapEscolhasUsuario):
        numeroIndividuos = int(hasMapEscolhasUsuario[Constantes.numeroIndividuos])
        populacao = [Individuo() for i in range(0, numeroIndividuos)]
        #for i in range(0, int(hasMapEscolhasUsuario[Constantes.numeroGeracao])):
            #TODO: Executar algoritmo
        print("FIM!\n")