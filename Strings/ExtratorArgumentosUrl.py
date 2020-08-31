class ExtratorArgumentosUrl:
    def __init__(self, url):
        if self.url_eh_valida(url):
            self.url = url
        else:
            raise LookupError("Url Inválida!!!")

    @staticmethod
    def url_eh_valida(url):
        if url:
            return True
        else:
            return False

    def extrai_argumentos(self):
        busca_moeda_origem = 'moedaorigem'
        busca_moeda_destino = 'moedadestino'

        indice_inicial_moeda_destino = self.encontra_indice_inicial(busca_moeda_destino)

        indice_inicial_moeda_origem = self.encontra_indice_inicial(busca_moeda_origem)
        indice_final_moeda_origem = self.url.find('&')

        moeda_origem = self.url[indice_inicial_moeda_origem:indice_final_moeda_origem]
        moeda_destino = self.url[indice_inicial_moeda_destino:]

        return moeda_origem, moeda_destino

    def encontra_indice_inicial(self, moeda_buscada):
        return self.url.find(moeda_buscada) + len(moeda_buscada) + 1

    def __str__(self):
        return self.url

    def __len__(self):
        return len(self.url)