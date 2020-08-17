listot = []
pessoa = []
mai = 0
lev = 0
while True:
    pessoa.append(str(input("Digite o nome da pessoa:").strip()))
    pessoa.append(float(input("Digite o peso dessa pessoa:").strip()))
    if len(listot) == 0:
        mai = lev = pessoa[1]
    else:
        if pessoa[1] >mai:
            mai = pessoa[1]

        if pessoa[1] < lev:
            lev = pessoa[1]
    listot.append(pessoa[:])
    pessoa.clear()
    while True:
        r = str(input("Você deseja adicionar mais alguém [S/N]: ").upper().strip())
        if r[0] == "N" or r[0]== "S":
            break
    if r[0] == "N":
        break
print(50*"-=")
print(f"A lista tem {len(listot)} pessoa(s)")
print(f"O maior peso foi {mai} kilos e foi da(s) pessoa(s) ",end="")
for p in listot:
    if p[1] == mai:
        print(f"{p[0]}",end=" ")
print(f"\nO menor peso foi {lev} e foi da(s) pessoa(s)",end="")
for p in listot:
    if p[1] == lev:
        print(f"{p[0]}",end=" ")
print(50*"\n-=")