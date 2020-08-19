listaj = []
gol = []
jogador = {}
while True:
    jogador["nome"] = str(input("Informe o nome do jogador:"))
    n = int(input(f"Quantas partidas o jogador {jogador['nome']} jogou:"))
    for j in range(0,n):
        gol.append(int(input(f"Quantos gol ele fez na partida {j+1}:")))
    jogador['gols'] = gol[:]
    jogador["total"] = sum(gol)
    listaj.append(jogador.copy())
    gol.clear()
    jogador.clear()
    while True:
        r = str(input("Deseja cadastrar mais um jogador [S/N]: ")).upper().strip()
        if r[0]=="S" or r[0] == "N":
            break
        else:
            print("Resposta inválida")
    if r[0] == "N":
        break
print(16*'-',"TABELA",16*"-")
print(" Cod ", end="")
for i in listaj[0].keys():
    print(f"{i:<15}", end="")
print()
print(40*"-")
for a, v in enumerate(listaj):
    print(F"{a:>2}  ",end="")
    for d in v.values():
        print(f"{str(d):<15}", end="")
    print()
print(40*"-")
while True:
    l = int(input("Você quer ver o levantamento de qual jogador [999 para o programa]:"))
    if l == 999:
        break
    if l >= len(listaj):
        print("Error , valor invalido!")
    else:
        print(40*"-")
        print(f"O levantamento do jogador {listaj[l]['nome']}:")
        print(40*"-")
        for n , g in enumerate(listaj[l]['gols']):
            print(f"No jogo {n+1} o jogador fez {listaj[l]['gols'][n]} gol(s).")
    print(40*"-")
