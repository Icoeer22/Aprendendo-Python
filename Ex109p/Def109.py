def formato(num):
    c = f"R${num:>8.2f}".replace(".",",")
    return c
def metade(num, m = False):
    d = num / 2
    if m == True:
        return formato(d)
    else:
        return d

def dobro(num, m = False):
    d = num*2
    if m == True:
        return formato(d)
    else:
        return d

def aumento(num, m = False):
    d = (110*num)/100
    if m == True:
        return formato(d)
    else:
        return d

def reducao(num, m = False):
    d = (87*num)/100
    if m == True:
        return formato(d)
    else:
        return d

