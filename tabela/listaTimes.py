from modeloTime import Time


class Campeonato:
    def __init__(self, times: list):
        self._times = times
        self._embates = 0

    @property
    def embates(self):
        return self._embates

    def __getitem__(self, item):
        return self._times[item]

    def embate(self, vencedor: Time, perdedor: Time, minuto_partida, segundo_partida):
        self._embates += 1
        tempo_partida = minuto_partida + segundo_partida / 60
        vencedor.venceu(perdedor, tempo_partida)
        perdedor.perdeu(vencedor)

    def tabela(self):
        self._times.sort(reverse=True)
        tabela = {}
        for time in self._times:
            tabela[time.nome] = time.vitorias
        return tabela
