print(30*"-")
print("Banco Augusto".center(30))
print(30*"-")
v = int(input("Quando você gostaria de sacar:"))
s = 50
c= 0
while True:
    if v>=s:
        v -= s
        c +=1
    else:
        if c > 0:
            print(f"Total de Cédulas de {s} é {c}")
        if s == 50:
            s = 20
        elif s == 20:
            s = 10
        elif s == 10:
            s = 1
        c = 0
        if v == 0:
            break



