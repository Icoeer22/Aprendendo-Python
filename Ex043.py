p = float(input("Digite seu peso:"))
a = float(input("Digite sua altura:"))
c = p / (a**2)
if c < 18.5:
    print("ABAIXO DO PESO")
elif 18.5 <= c < 25:
    print("PESO IDEAL")
elif 25 <= c < 30:
    print("SOBREPESO")
elif 30 <= c < 40:
    print("OBESIDADE")
elif c > 40:
    print("OBESIDADE MÓRBIDA")