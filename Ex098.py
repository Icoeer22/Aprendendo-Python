from time import sleep
def cont(inicio,fim,passo):
    if passo == 0:
        passo = 1
    if passo <0:
        passo*=-1
    print(f"Contagem de {inicio} até {fim} de {passo} em {passo}!!!")

    if inicio < fim:
        conta = inicio
        while conta<= fim:
            print(f"{conta}",end=" ")
            sleep(0.5)
            conta+=passo
        print("Fim")
    else:
        conta=inicio
        while conta>= fim:
            print(f"{conta}",end=" ")
            conta -=passo
            sleep(0.5)
        print("Fim")


cont(1,10,1)
cont(10,0,2)
print(30*"-")
print("Agora é a sua vez!!!")
i = int(input("Informe o valor de início:"))
f = int(input("Informe o valor final:"))
p = int(input("Informe o falor de passo:"))
cont(i,f,p)