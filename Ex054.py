from datetime import datetime
g = 0
d = datetime.now()
f = 0
for a in range(0, 7):
    b = int(input("Digite o ano de nascimento da pessoa:"))
    c = d.year - b
    if c < 18:
        g += 1
    else:
        f+=1
print(f"Esse numero de pessoas não atingiu a maioridade {g}")
print(f"Tantas pessoas ja sao de maior {f}")