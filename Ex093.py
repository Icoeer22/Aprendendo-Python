from operator import itemgetter
joga = {}
joga["jogador"]=str(input("Informe o nome do jogador:")).strip()
n = int(input("Quantos jogos ele jogou:"))
gols = []
t=0
for a in range(0,n):
    b =(int(input(f"Quantos gols o jogador fez no jogo {a+1}:")))
    gols.append(b)
    t+=b
joga["gols"] = gols[:]
joga["total"] = t
print(10*'-=',"Análise",10*"-=")
print(joga)
print(27*"-=")
for k, v in joga.items():
    print(f"{k} tem valor {v}")
print(27*"-=")
print(f"O jogador {joga['jogador']} que jogou {n} jogos")
print(f'O jogador {joga["jogador"]} jogou {len(joga["gols"]) }' )
for i,v in enumerate(joga["gols"]):
    print(f"O jogador na partida {i+1} fez {v} gols")
print(27*"-=")