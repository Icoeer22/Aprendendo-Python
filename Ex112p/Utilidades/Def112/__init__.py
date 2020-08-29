def formato(num):
    c = f"R${num:>8.2f}".replace(".",",")
    return c
def metade(num):
    m = num / 2
    return m

def dobro(num):
    d = num*2
    return d

def aumento(num, por):
    d = ((100+por)*num)/100
    return d

def reducao(num, po):
    d = ((100-po)*num)/100
    return d

def resumo (num , aum , dim):
    print(30*"-")
    print(f'{"RESUMO DO VALOR":^30}')
    print(30*"-")
    print(f"{'Preço analisado:':<16} ", f"{formato(num):>}")
    print(f"{'Dobro do preço:':<16} ", f"{formato(dobro(num)):>}")
    print(f"{'Metade do preço:':<16} ", f"{formato(metade(num)):>}")
    print(f"{f'{aum}% de Aumento:':<16} ", f"{formato(aumento(num,aum)):>}")
    print(f"{f'{dim}% de Redução:':<16} ", f"{formato(reducao(num,dim)):>}")
    print(30*"-")