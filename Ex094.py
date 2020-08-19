tot = []
pessoa = {}
cont = 0
id = 0
while True:
    pessoa["nome"] = str(input("Digigte o nome:")).strip()
    while True:
        s = str(input("DIgite o sexo [M/F]")).upper().strip()[0]
        if s[0] == "M" or s[0] == "F":
            pessoa["sexo"] = s
            break
        else:
            print("Resposta invalida, por favor responda corretamente.")
    ida = int(input("Digite a idade da pessoa:"))
    id += ida
    pessoa["idade"] = ida
    tot.append(pessoa.copy())
    pessoa.clear()
    while True:
        r = str(input("Você deseja cadastrar mais uma pessoa [S/N]:")).upper().strip()
        if r[0] == "N" or r[0] == "S":
            break
        else:
            print("Resposta invalida, por favor responda corretamente.")
    if r[0]=="N":
        break
print(30*"•","Analise",30*"•")
print(f"-O tatal de pessoas cadastradas foi {len(tot)}.")
print(f"-A idade média das pessoas cadastradas foi {id/len(tot):.2f}")
print(f"-As mulheres cadastradas foram: ",end="")
for a in tot:
    if a["sexo"] == "F":
        print(a["nome"],end=" ")
        cont +=1
if cont == 0:
    print("Nenhuma mulher foi cadastrada.")
print()
cont = 0
print("-A lista de pessoa(s) que tem idade acima da media é:")
for a in tot:
    if a["idade"] >= (id/len(tot)):
        print("    ",end="")
        for k, v in a.items():
            print(f"{k} = {v};", end="")
        cont+=1
        print()
if cont == 0:
    print("Ninguém acima da média de idade.")