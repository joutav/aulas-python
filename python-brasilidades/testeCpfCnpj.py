from cpf_cnpj import Documento
import re
from validate_docbr import CNPJ

#cpf_um = Cpf(15316264754)

#print(cpf_um.format_cpf())

exemplo_cnpj = '26497490000177'
exemplo_cpf = 87607606050

texto_inputado = input('Insira seu cpf ou cnpj para validaçao: ')
texto_tratado = ''
texto_tratado = ''.join(str(i) for i in re.findall(r'\d', texto_inputado))


try:
    print('Cpf Valido: {}'.format(Documento.cria_documento(texto_tratado)))
except ValueError as e:
    print(e.__str__())



