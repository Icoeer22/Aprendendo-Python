import random
from time import sleep
from operator import itemgetter
jogadores = {'jogador 1': random.randint(1,6),'jogador 2': random.randint(1,6),'jogador 3': random.randint(1,6),'jogador 4': random.randint(1,6)}
print(3*"=","Valores Sorteados",3*"=")
ranking ={}
for k, v in jogadores.items():
    print(f"O {k} tirou {v}")
    sleep(1)
ranking = sorted(jogadores.items(),key=itemgetter(1), reverse=True)
print(20*"-=")
for i, v in enumerate(ranking):
    print(f"{i+1}º lugar é o {v[0]} com {v[1]}")