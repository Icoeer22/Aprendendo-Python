from time import sleep



def maior(*nmr):
    cont = maior = 0
    print(50*"-=")
    for valor in nmr:
        print(f"{valor}  ", end="", flush=True)
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont +=1

    print(f"Foram informados {cont} valores.")
    print(f"O maior numero foi {maior}")


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(6)
maior()