import re
class TelefonesBr:
    def __init__(self, telefone):
        self.padrao = '([0-9]{2})([0-9]{4,5})([0-9]{4})'
        if self.valida_telefone(telefone):
            self.numero = telefone
        else:
            raise ValueError("Telfone inválido")

    def __str__(self):
        return self.format_numero()

    def valida_telefone(self, telefone):
        resposta = re.findall(self.padrao, telefone)
        if resposta:
            return True
        else:
            return False

    def format_numero(self):
        resposta = re.search(self.padrao, self.numero)
        numero_formatado = '({}){}-{}'.format(
            resposta.group(1),
            resposta.group(2),
            resposta.group(3)
        )
        return numero_formatado