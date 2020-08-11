a = int(input("Digite um segmento de reta:"))
b = int(input("Digite um segmento de reta:"))
c = int(input("Digite um segmento de reta:"))

if a < b + c and b < a + c and c < a +b:
    if a == c == b:
        print("EQUILATERO")
    elif a == b or a == c or c ==b:
        print("ISÓCELES")
    elif a != b != c:
        print("ESCALENO")

else:
    print("Não forma triangulo")