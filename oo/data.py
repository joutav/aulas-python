class Data:

    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def formatada(self):
        print("{:2}/{:02}/{:4}".format(self.dia, self.mes, self.ano))

