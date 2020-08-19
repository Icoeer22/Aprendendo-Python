from datetime import datetime
pessoa = {}
now = datetime.now()
pessoa["nome"] = str(input("Digite seu nome:")).strip()
ano = int(input("Informe o ano do seu nascimento:"))
a = now.year-ano
pessoa['idade'] = a
cart = int(input("Número da carteira de trabalho [ caso não tenha aperte 0 ] :"))
if cart != 0:
    pessoa['carteira'] = cart
    anos = int(input("Qual o ano da sua contratação:"))
    pessoa['contratação'] = anos
    sal = int(input("Qual o valor do seu salário:"))
    pessoa["salario"]  = sal
    pessoa["aposentadoria"] = (35-(now.year-anos))+a

else:
    pessoa['carteira'] = "não possui carteira"
print(10*"-","Dados da Pessoa", 10*"-")
for k, v in pessoa.items():
    print(f"{k} tem o valor {v}")
