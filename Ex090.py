aluno = {}
aluno["nome"] = str(input("Informe o nome do aluno:"))
aluno["media"] = float(input("Digite a média do aluno:"))
if aluno["media"] >= 7:
    aluno["estado"] = "aprovado"
elif aluno["media"] < 7:
    aluno["estado"] = "reprovado"
for k , v in aluno.items():
    print(f"{k} é igual a {v} ")