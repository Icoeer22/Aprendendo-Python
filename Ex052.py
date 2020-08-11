a = int(input("Digite um número:"))
b = 0
for c in range(1, a+1):
    if a % c == 0:
        b += 1
if b == 1 or b == 2:
    print("Numero primo")
else:
    print("NAO PRIMIO")