c = 0
g = 0
for a in range(0,5):
    b = float(input("Digite um peso:"))
    if a == 0:
        c = b
        g = b
    elif b > c :
        c = b
    elif b < g:
        g = b

print("O mais pesado é {}".format(c))
print("O mais leve é {}".format(g))
