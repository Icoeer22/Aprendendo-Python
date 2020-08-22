def fatorial(val=1, show=False):
    """

    :param val: Valor a ser cauculado o fatoria
    :param show: Se você quer ver aconta
    :return: O fatorial de val ou a conta toda com resultado
    """
    f=1
    for c in range(val, 0, -1):
        if show:
            print(c,end="")
            if c>1:
                print(f" X ",end="")
            else:
                print(" = ",end="")
        f*=c
    return f


print(fatorial(10,False))