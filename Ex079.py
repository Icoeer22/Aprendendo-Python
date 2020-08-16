list = []
while True:
    a = int(input("Digite um número:"))
    if a in list:
        print("Este número já esta na lista.")
    else:
        list.append(a)
        print("Número adicionado")
    c = str(input("Você quer continuar:")).upper().strip()
    print(30*"-")
    if c[0] == "N":
        break
print(f"A lista em ordem crescente é {sorted(list)}")