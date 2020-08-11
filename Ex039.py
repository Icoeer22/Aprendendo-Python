from datetime import datetime
a = datetime.now()
ano = int(input("Digite seu ano de nascimento:"))
b = a.year - ano
c = 18 - b
if b  == 18:
    print(f"Ta na hora de se alistar")
elif b < 18:
    print(f"Ainda não precisa se alistar falta {c} anos ainda")
elif b > 18:
    print(f"Ja passou da hora ne, passou {c*-1}")