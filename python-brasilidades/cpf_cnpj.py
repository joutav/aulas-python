from validate_docbr import CPF
from validate_docbr import CNPJ


class Documento:

    @staticmethod
    def cria_documento(documento):
        documento = str(documento)
        if len(documento) == 11:
            return DocCpf(documento)
        elif len(documento) == 14:
            return DocCnpj(documento)
        else:
            raise ValueError("Quantidade de dígitos inválida!!")


class DocCpf:

    def __init__(self, documento):
        self.cpf_verify = CPF()
        if self.valida(documento):
            self.cpf = documento
        else:
            raise ValueError("Cpf inválido!!")

    def __str__(self):
        return self.__format()

    def valida(self, documento):
        cpf = CPF()
        return self.cpf_verify.validate(documento)

    def __format(self):
        cpf = CPF()
        return self.cpf_verify.mask(self.cpf)


class DocCnpj:

    def __init__(self, documento):
        self.cnpj_verify = CNPJ()
        if self.valida(documento):
            self.cnpj = documento
        else:
            raise ValueError("CNPJ inválido!!")

    def __str__(self):
        return self.__format()

    def valida(self, documento):
        return self.cnpj_verify.validate(documento)

    def __format(self):
        return self.cnpj_verify.mask(self.cnpj)




