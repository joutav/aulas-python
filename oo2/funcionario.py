class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self._salario



    def registra_horas(self, horas):
        print('Horas registradas...')

    def mostrar_tarefas(self):
        print('Fez muita coisa...')


class Caelum(Funcionario):
    def mostrar_tarefas(self):
        print('Fez muita coisa, Caelumer')

    def busca_cursos_do_mes(self, mes=None):
        print(f'Mostrando cursos - {mes}' if mes else 'Mostrando cursos desse mês')

    def bonificacao(self):
        return super._salario() * 1.1


class Alura(Funcionario):
    def mostrar_tarefas(self):
        print('Fez muita coisa, Alurete!')

    def busca_perguntas_sem_resposta(self):
        print('Mostrando perguntas não respondidas do fórum')


class Hipster:
    def __str__(self):
        return f'Hipster, {self.nome}'


class Junior(Alura):
    pass


class Plenos(Alura, Caelum):
    pass


class Senior(Alura, Caelum, Hipster):
    pass


luan = Senior('Luan')
print(luan)

# MIXIN pequenas classes que nao se instancia um objeto, apenas adiciona um comportamento em classes ja existentes.


