class FuncaoCusto:
    
    def funcaoPadrao(individuo):
        combinacao=individuo.getCombinacao()
        sinalDeSaida=9+combinacao[3]*combinacao[5]-combinacao[23]*combinacao[14]+combinacao[24]*combinacao[4]-combinacao[21]*combinacao[10]+combinacao[36]*combinacao[15]-combinacao[11]*combinacao[26]+combinacao[16]*combinacao[17]+combinacao[3]*combinacao[33]+combinacao[28]*combinacao[19]+combinacao[12]*combinacao[34]-combinacao[31]*combinacao[32]-combinacao[22]*combinacao[25]+combinacao[35]*combinacao[27]-combinacao[29]*combinacao[7]+combinacao[8]*combinacao[13]-combinacao[6]*combinacao[9]+combinacao[18]*combinacao[20]-combinacao[1]*combinacao[30]+combinacao[23]*combinacao[4]+combinacao[21]*combinacao[15]+combinacao[26]*combinacao[16]+combinacao[31]*combinacao[12]+combinacao[25]*combinacao[19]+combinacao[7]*combinacao[8]+combinacao[9]*combinacao[18]+combinacao[1]*combinacao[33]
        return sinalDeSaida
    
