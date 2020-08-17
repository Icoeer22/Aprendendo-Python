print(15 * "-=", "Aplicativo Escolar ", 15 * "-=")
lista = []
m = 0
temp = []
while True:
    n = str(input("Nome:"))
    n1 = float(input("Nota 1:"))
    n2 = float(input("Nota 2:"))
    m = (n1 + n2) / 2
    lista.append([n, [n1, n2], m])
    while True:
        r = str(input("Quer adicionar mais um aluno [S/N]:")).upper().strip()
        if r[0] == "N" or r[0] == "S":
            break
    if r[0] == "N":
        break
print(5 * "-=", "Lista dos Alunos", 5 * "-=")
print("No.".ljust(10), "Nome".center(10), "Média".rjust(10))
for c in range(0, len(lista)):
    print(f"{c}".ljust(10), f"{lista[c][0]}".center(10), f"{lista[c][2]}".rjust(10))
print(19 * "-=")
while True:
    aluno = int(input("Qual o número do aluno que você deseja ver as notas (999 interrompe):"))
    if aluno == 999:
        break
    else:
        print(46 * '•')
        print(f"A média do aluno {lista[aluno][0]} é {lista[aluno][1]}")
        print(46 * '•')
print("Obrigado por confiar no nosso sistema!!!")
