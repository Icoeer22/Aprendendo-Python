n = int(input("Digite um numero:"))
print("Escolha uma base de converção:")
while True:
    print("[1] Binário ")
    print("[2] Octal")
    print("[3] Hexadecimal")
    a = int(input("Qual base você quer:"))
    if a == 1 or a == 2 or a == 3:
        break
if a == 1:
    print(f"Em Binário fica {bin(n) [2:]}")
elif a == 2:
    print(f"Em Octal fica {oct(n)}")
else:
    print(f"Em Hexadecimal fica {hex(n)}")
