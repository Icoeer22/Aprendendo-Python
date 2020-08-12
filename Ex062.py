a = int(input("Informe o primeiro termo da PA:"))
b = int(input("Informe a razão da Progressão Aritimética:"))
r = "S"
cont = 0
n = 0
print(20*"-=")
while cont < 10:

    if cont == 0:
        print(f"{a}¬",end="")
    else:
        if cont == 9:
            print(f"{a+b}")
        else:
            print(f"{a+b}¬", end="")
        a +=b
    cont +=1
while r == "S":
    print(20*"-=")
    r = str(input("Você deseja continuar:")).upper().strip()
    if r == "S":
        n = int(input("Quantos numeros novos você deseja:"))
        print(20*"-=")
        h = cont + n
        while cont < h:
            if cont == (h-1):
                print(f"{a+b}")
            else:
                print(f"{a+b}¬",end="")
            a +=b
            cont+=1
print("Fim")
