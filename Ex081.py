list=[]
while True:
    list.append(int(input("Informe um número:")))

    while True:
        r = str(input("Você deseja adicionar mais um número:")).strip().upper()
        if r[0] == "N" or r[0] == "S":
            break
    if r[0] == "N":
        break
print(30*"-=")
print(f"A lista tem {len(list)} itens")
list.sort(reverse=True)
print(f"A lista ao decrescente fica {list}")
if 5 in list:
    print("O cinco está na lista")
else:
    print("O número cinco não está na lista")
print(30*"-=1")