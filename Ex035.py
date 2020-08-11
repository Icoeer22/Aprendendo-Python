r = float(input("Digite o valor de uma reta:"))
a = float(input("Digite o valor de uma reta:"))
b = float(input("Digite o valor de uma reta:"))
if r < a + b and a < r + b and b < r + a:
    print("Forma um triangulo")
else:
    print("Nao forma um triangulo")