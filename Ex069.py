si = 0
h = 0
f = 0
a = "Cadastro de Pessoas"

print(30*"-")
print(f"{a:^30}")
print(30*"-")
while True:
    i = int(input("Qual a idade:"))
    s = " "
    while s not in "MF":
        s = str(input("Qual o sexo [M/F]:")).upper().strip()

    if i > 18:
        si += i
    if s[0] == "M":
        h += 1
    if s[0] == "F" and i < 20:
        f += 1
    r = " "
    while r[0] not in "SN":
        r = str(input("Você deseja cadastrar outra pessoa:")).upper().strip()
        print(30*"-")
    if r == "N":

        break

print(30*"-")
print("Resultados do Cadastro".center(30))
print(f"Pessoas com mais de 18 anos: {si}")
print(f"Homens cadastrados: {h}")
print(f"Mulheres com menos de 20 anos cadastradas: {f}")
print(30*"-")