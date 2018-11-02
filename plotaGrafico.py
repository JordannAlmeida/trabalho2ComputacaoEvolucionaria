import matplotlib.pyplot as pl

class PlotaGrafico:
    
    @staticmethod
    def plotarGrafico2d(eixoX, eixoY, titulo, tituloFigura="./fig/fig", labelX = "Epocas", labelY = "Fitness"):
        pl.axis(PlotaGrafico.defineAxisRange(eixoX, eixoY))
        pl.xlabel(labelX)
        pl.ylabel(labelY)
        pl.title(titulo)
        pl.plot(eixoX, eixoY, 'r--')
        pl.savefig(tituloFigura + ".png")
        pl.show()

    @staticmethod
    def defineAxisRange(eixoX, eixoY):
        return [min(eixoX)-2, max(eixoX)+2, min(eixoY)-2, max(eixoY)+2]
