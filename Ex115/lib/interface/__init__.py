def linha (tam = 42):
    return "-"*tam


def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except(ValueError, TypeError):
            print("\33[31mERRO: Por favor digite um valor válido!\33[m")
            continue
        except(KeyboardInterrupt):
            print("\33[31mERRO: Usuário preferiu não digitar!\33[m")
            return 0
        else:
            return n


def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabeçalho("MENU PRINCIPAL")
    c = 1
    for item in lista:
        print(f"\33[33m{c}\33[m - \33[34m{item}\33[m")
        c += 1
    print(linha())
    opc = leiaInt("\33[32mSua Opção:\33[m")
    return opc



