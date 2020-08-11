a = float(input("Digite um numero:"))
b = float(input("Digite um numero:"))
s = 0
while s != 5:
    print(15*"-=")
    s = int(input(("[1] Somar \n[2] Mutiplicar \n[3] Maior numero \n[4] Numeros novos \n[5] Sair\nQual você deseja senhor:")))
    print(15*"-=")

    if s == 1:
        print(f"{a+b}")
    if s == 2:
        print(f"{a*b}")
    if s == 3:
        if a > b:
            print(f"{a}")
        if b > a:
            print(f"{b}")
        if a == b:
            print("Iguais")
    if s == 4:
        a = float(input("Digite um numero:"))
        b = float(input("Digite um numero:"))
print("Obrigado pela preferencia.")