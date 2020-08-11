c = float(input("Qual o valor da casa:"))
t = int(input("Em quantos anos você pretende pagar:"))
s = float(input("Quanto você ganha:"))
t = t*12
v = c / t
sa = (s*30)/ 100
if v >  sa:
    print("NEGADO")
else:
    print("APROVADO")
    print(f"Você vai pagar {v:.2f} reais por mes")