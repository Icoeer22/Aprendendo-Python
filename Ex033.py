a = int(input("Digite um valor:"))
b = int(input("Digite um valor:"))
c = int(input("Digite um valor:"))
lista = [a,b,c]
print(f"O maior valor é {max(lista)}")
print(f"O menor valor é {min(lista)}")
if a > b and a > c:
    print(f"O maior numero é {a}")
if a < b and a < c:
    print(f"O menor numero é {a}")
if b > a and b > c:
    print(f"O maior numero é {b}")
if b < a and b < c:
    print(f"O menor numero é {b}")
if c > a and c > b:
    print(f"O maior numero é {c}")
if c < a and c < b:
    print(f"O menor valor é {c}")