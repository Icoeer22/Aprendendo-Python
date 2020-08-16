list = []
imp = []
par = []
while True:
    list.append(int(input("Digite um número:")))
    while True:
        r = str(input("Você quer continuar:")).upper().strip()
        if r[0] == "N" or r[0] == "S":
            break
    if r[0] == "N":
        break
for a in list:
    if list[a] % 2 == 0 or list[a] == 0:
        par.append(list[a])
    else:
        imp.append(list[a])
print(30*"-=")
print(f"A lista é {list}")
print(f"A lista par é {par}")
print(f"A lista ímpar é {imp}")
print(30*"-=")