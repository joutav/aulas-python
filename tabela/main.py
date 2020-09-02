from modeloTime import Time
from listaTimes import Campeonato

time_1 = Time('Pain Gaming')
time_2 = Time('Intz')
time_3 = Time('Kabum')
time_4 = Time('Keyd')

times = [time_1, time_2, time_3, time_4]

cblol = Campeonato(times)

cblol.embate(time_1, time_2, 35, 40)
cblol.embate(time_2, time_1, 30, 40)
cblol.embate(time_3, time_4, 27, 40)
cblol.embate(time_4, time_1, 25, 40)
cblol.embate(time_3, time_4, 27, 40)
cblol.embate(time_1, time_2, 47, 50)

print(cblol.tabela())

