p = ("Pao", "Caixa", "Viga")
for a,b in enumerate(p):
    print(f"\nA palavra {p[a]} tem as vogais:",end=" ")
    for letra in b:
        if letra.lower() in "aeiou":
            print(letra, end=" ")