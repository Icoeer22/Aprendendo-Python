def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except(ValueError, TypeError):
            print("ERRO: Por favor digite um valor válido!")
            continue
        except(KeyboardInterrupt):
            print("ERRO: Usuário preferiu não digitar!")
            return 0
        else:
            return n
def leiaFlt(msg):
    while True:
        try:
            n1 = float(input(msg))
        except(ValueError, TypeError):
            print("\33[31mERRO: Por favor digite um valor válido!\33[m")
        except(KeyboardInterrupt):
            print("\33[31mERRO: Usuário preferiu não digitar!\33[m")
            return 0
        else:
            return n1


# Principal
n = leiaInt  ("Digite um número inteiro:")
n1 = leiaFlt ("Digite um número real:")
print(f"\33[32mVocê digitou o número inteiro {n} e o número real {n1}\33[m")