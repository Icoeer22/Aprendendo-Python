def leiaInt(msg):
    ok = False
    p = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print("Erro digite um número válido!")
        if ok:
            break
    return valor


# Principal
n = leiaInt  ("Digite um numero:")
print(f"Você digitou o número {n}")
