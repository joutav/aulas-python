import re

email1 = 'Pao de batata, 5910-1234'
email2 = 'Suino de batata, 1234-4567'
email3 = 'Pao de mandioca, 5568-1234'
email4 = '4567-9875 Pao de nata, 99875-1234'

padrao = '[0-9]{4,5}[-]*[0-9]{4}'
mensagens = [email1, email2, email3, email4]

for email in mensagens:
    retorno = re.findall(padrao, email)
    print(retorno)

