tabela = [[[],[],[]],[[],[],[]],[[],[],[]]]
for a in range(0,3):
    b = float(input(f"Informe um número para a matriz na posição (0,{a}):"))
    tabela[0][a].append(b)
for a in range(0,3):
    b = float(input(f"Informe um número para a matriz na posição (1,{a}):"))
    tabela[1][a].append(b)
for a in range(0,3):
    b = float(input(f"Informe um número para a matriz na posição (2,{a}):"))
    tabela[2][a].append(b)
print(30*"-=")
print(f"{tabela[0][0]}{tabela[0][1]}{tabela[0][2]}")
print(f"{tabela[1][0]}{tabela[1][1]}{tabela[1][2]}")
print(f"{tabela[2][0]}{tabela[2][1]}{tabela[2][2]}")
print(30*"-=")


matriz = [[0,0,0],[0,0,0],[0,0,0]]
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f"Informe um valor para a matriz na posição [{l},{c}]:"))
print(30*"-=")
for l in range(0,3):
    for c in range(0,3):
        print(f"[{matriz[l][c]:^5}]",end="")
    print()