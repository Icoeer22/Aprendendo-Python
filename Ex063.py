n = int(input("Digite um nomero para ver uma sequencia de fibonacci:"))
t1 = 0
t2 = 1
print(15*"-=")
print(f"{t1}¬{t2}¬",end="")
cont = 3
while cont <= n:
    t3 = t1+t2
    if cont == n:
        print(f"{t3}")
    else:
        print(f"{t3}¬",end="")
    t1=t2
    t2=t3
    cont +=1
print(15*"-=")