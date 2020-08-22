def area(a,b):
    print(f"A área do terreno de {a:.2f}m X {b:.2f}m é {a*b:.2f}m.")
#inicio
print(7*"-","Controle de Terreno",7*"-")
c = float(input("Largura (m):"))
d = float(input("Comprimento (m):"))
area(a=c,b=d)