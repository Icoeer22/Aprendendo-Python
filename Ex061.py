a = int(input("Digite o fator de uma progessão aritimética:"))
c = int(input("Informe o primeiro barulho:"))
cont = 0
b = 1
while cont  < 10:
    if cont == 0:
        print(f"{c}¬",end= "")
    else:
        print(f"{c+a}¬", end="")
        c+=a
    cont+=1

print("Fim")