import random
ps = int(input("Digite um valor que você acha estar certo entre 0 e 5:"))
pc = random.randint(0,5)
print(f"O pc pensou em {pc}")
if ps == pc:
    print("Paraben voce ganhou!!!")
else:
    print("Que pena voce perdeu")

