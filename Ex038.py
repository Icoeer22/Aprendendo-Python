a = int(input("Digite um valor:"))
b = int(input("Digite mais um valor:"))
if a > b:
    print(f"O primeiro número é maior {a}")
elif b > a:
    print(f"O segundo número é maior {b}")
elif a == b:
    print("Os dois valores são iguais.")