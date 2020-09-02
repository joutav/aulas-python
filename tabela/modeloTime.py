from collections import defaultdict
from functools import total_ordering


@total_ordering
class Time:
    def __init__(self, nome):
        self._nome = nome
        self._partidas = 0
        self._vitorias = 0
        self._tempo_de_vitorais = 0
        self._derrotas = 0
        self._vitorias_confrontos_diretos = defaultdict(int)
        self._derrotas_confrontos_diretos = defaultdict(int)

    def venceu(self, adversario, tempo_game):
        self._vitorias += 1
        self._partidas += 1
        self._vitorias_confrontos_diretos[adversario.nome] += 1
        self._tempo_de_vitorais += tempo_game

    def perdeu(self, adversario):
        self._partidas += 1
        self._derrotas += 1
        self._derrotas_confrontos_diretos[adversario.nome] += 1

    def __str__(self):
        return '{}: {} vitorias'.format(self._nome, self._vitorias)

    def __repr__(self):
        return '{} : {}V'.format(self._nome, self._vitorias)

    def media_tempo_vitorias(self):
        if self._vitorias != 0:
            return self._tempo_de_vitorais / self._vitorias
        return 0

    @property
    def vitorias(self):
        return self._vitorias

    @property
    def nome(self):
        return self._nome

    def obter_confrontos_diretos(self, other):
        return self._vitorias_confrontos_diretos[other.nome]

    def __eq__(self, other):
        vitorias = self._vitorias == other.vitorias
        confrontos = self.obter_confrontos_diretos(other) == other.obter_confrontos_diretos(self)
        tempo_game = self.media_tempo_vitorias() == other.media_tempo_vitorias()

        return vitorias and confrontos and tempo_game

    def __lt__(self, other):

        vitorias = self._vitorias == other.vitorias
        confrontos = self.obter_confrontos_diretos(other) == other.obter_confrontos_diretos(self)

        if vitorias and confrontos:
            return self.media_tempo_vitorias() > other.media_tempo_vitorias()
        if vitorias:
            return self.obter_confrontos_diretos(other) < other.obter_confrontos_diretos(self)

        return self._vitorias < other.vitorias
