s = 0
q = 0
while True:
    n = int(input("Digite um número:"))
    
    if n == 999:
         break
    s += n
    q += 1
print(f"Soma = {s} e Quantidade de números = {q}")
print("Fim")