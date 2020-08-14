c = 0
t = 0
a = 0
min = 0
np = " "
while True:
    n = str(input("Digite o nome do produto:"))
    p = float(input("Digite o valo do produto:"))
    if p >= 1000:
        c +=1
    if a == 0:
        min = p
        np = n
    elif p < min:
        min = p
        np = n
    t +=p
    a +=1
    r = str(input("Você deseja continuar:")).upper().strip()
    print(50*"-")
    if r[0] == "N":
        break
print(50*"-")
print(f"O valor a ser pago será {t}")
print(f"{c} produtos custão mais de 1000 reais.")
print(f"O menor produto é {np}")
print(50*"-")