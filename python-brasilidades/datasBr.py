from datetime import datetime, timedelta


class DatasBr:

    def __init__(self):
        self.momento_cadastro = datetime.today()

    def mes_cadastro(self):
        meses_do_ano = [
            'Janeiro', 'Fevereiro', 'Março', 'Abril',
            'Maio', 'Junho', 'Julho', 'Agosto',
            'Setembro', 'Outubro', 'Novembro', 'Dezembro'
        ]
        return meses_do_ano[self.momento_cadastro.month - 1]

    def __str__(self):
        return self.format_data()

    def momento_cadastro(self):
        return self.__str__()

    def dia_semana(self):
        dias_da_semana = ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sabado', 'Domingo']
        return dias_da_semana[self.momento_cadastro.weekday()]

    def format_data(self):
        return self.momento_cadastro.strftime('%d/%m/%Y %H:%M')

    def tempo_cadastro(self):
        return datetime.today() - (self.momento_cadastro - timedelta(days=30))