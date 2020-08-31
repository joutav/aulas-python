from ExtratorArgumentosUrl import ExtratorArgumentosUrl

url = 'moedaorigem=real&moedadestino=dolar'
argumento = ExtratorArgumentosUrl(url)

moeda_origem, moeda_destino = argumento.extrai_argumentos()

print(moeda_origem + ", " + moeda_destino)