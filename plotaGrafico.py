import matplotlib.pyplot as pl

class PlotaGrafico:
    
    @staticmethod
    def plotarGrafico2d(eixoX, eixoY, labelX = "epocas", labelY = "Valor na Função Custo"):
        pl.axis(PlotaGrafico.defineAxisRange(eixoX, eixoY))
        pl.xlabel(labelX)
        pl.ylabel(labelY)
        pl.plot(eixoX, eixoY, 'r--')
        pl.show()

    @staticmethod
    def defineAxisRange(eixoX, eixoY):
        return [min(eixoX)-2, max(eixoX)+2, min(eixoY)-2, max(eixoY)+2]
