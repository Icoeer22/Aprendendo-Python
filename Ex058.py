import random
pc = random.randint(0,10)
ps = int(input("Digite um numero entre 0 e 10 :"))
cont = 1
while ps != pc:
    ps = int(input("Que pena você errou, digite um numero:"))
    cont+=1
    if ps == pc:
        print("Parabens, você tentou {}".format(cont))
