from acessaCep import BuscaEndereco

cep = '01001000'
objeto_cep = BuscaEndereco(cep)
print(objeto_cep.format_cep())

# r = requests.get('https://viacep.com.br/ws/01001000/json/')
objeto_cep.acessa_via_cep()

bairro, cidade, uf = objeto_cep.acessa_via_cep()

print(bairro, cidade, uf)