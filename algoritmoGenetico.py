import random
class AlgoritmoGenetico:
    

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

    def selecaoDosPaisRoleta(listaDeAvaliacao)
        pai1=giraRoleta(listaDeAvaliacao)
        pai2=giraRoleta(listaDeAvaliacao)
        pais=[pai1,pai2]
        return pais

    def cruzamentoUmPonto(pais,txCruzamento)
        pai1=pais[1]
        pai2=pais[2]
        tam1=len(pai1)
        tam2=len(pai2)
        filhos=[]
        if tam1!=tam2:
            filhos="impossível, tamanho diferente"
        if tam1==tam2:
            cruz=random.randint(0,100)
        if cruz<txCruzamento:
            crossOver=random.randint(1,(tam1-2))
            filho1=pai1[0:crossOver]+pai2[crossOver:tam2]
            filho2=pai2[0:crossOver]+pai1[crossOver:tam1]
            filhos=[filho1,filho2]
         return filhos

    def cruzamentoUniforme(pais)
        pai1=pais[1]
        pai2=pais[2]
        tam1=len(pai1)
        tam2=len(pai2)
        filhos=[]
        if tam1!=tam2:
            filhos="impossível, tamanho diferente"
        if tam1==tam2:
            cruz=random.randint(0,100)
        if cruz<txCruzamento:
            crossOver=random.randint(1,(tam1-2))
            filho1=pai1[0:crossOver]+pai2[crossOver:tam2]
            filho2=pai2[0:crossOver]+pai1[crossOver:tam1]
            filhos=[filho1,filho2]
         return filhos