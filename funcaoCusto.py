class FuncaoCusto:
    
    def funcaoPadrao(individuo):
        combinacao=individuo.getCombinacao()
        sinalDeSaida=9+combinacao[1]*combinacao[4]-combinacao[22]*combinacao[13]+combinacao[23]*combinacao[3]-combinacao[20]*combinacao[9]+combinacao[35]*combinacao[14]-combinacao[10]*combinacao[25]+combinacao[15]*combinacao[16]+combinacao[2]*combinacao[32]+combinacao[27]*combinacao[18]+combinacao[11]*combinacao[33]-combinacao[30]*combinacao[31]-combinacao[21]*combinacao[24]+combinacao[34]*combinacao[26]-combinacao[28]*combinacao[6]+combinacao[7]*combinacao[12]-combinacao[5]*combinacao[8]+combinacao[17]*combinacao[19]-combinacao[0]*combinacao[29]+combinacao[22]*combinacao[3]+combinacao[20]*combinacao[14]+combinacao[25]*combinacao[15]+combinacao[30]*combinacao[11]+combinacao[24]*combinacao[18]+combinacao[6]*combinacao[7]+combinacao[8]*combinacao[17]+combinacao[0]*combinacao[32]
        return sinalDeSaida
    
