m = ""
g = 0
me = 0
f = 0
for a in range (0,4):
    n = str(input("Digite o nome:"))
    s = str(input("Digite o sexo [F/M]")).upper()
    i = int(input("Digite a idade:"))
    me += i
    if s == "F" and i < 20:
        f += 1
    if g == 0 and s == "M":
        g = i
    elif i > g and s =="M":
        m = n
        g = i
print(f"A média de idade é {me/4}")
print(f"Tem {f} mulheres com menos de 20 anos")
print(f"O homem mais velho se chama {m}")