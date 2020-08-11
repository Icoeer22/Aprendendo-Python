a = float(input("Digite a primeira nota:"))
b = float(input("Digite a segunda nota:"))
c = (a+b)/2
if c < 5:
    print("REPROVADO")
elif 5 <= c < 7:
    print("RECUPERAÇÃO")
elif c >= 7:
    print("APROVADO")