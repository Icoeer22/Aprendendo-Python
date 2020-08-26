from time import sleep
cor = ('\33[m', '\33[30;44m', '\33[30;41m', '\33[30;42m')
def titulo(msg, c=0):
    t = len(msg) + 4
    print(cor[c], end="")
    print("~" * t)
    print(f"  {msg}  ")
    print("~" * t)
    print(cor[0],end="")
def ajuda(com):
    """
    :return: Você informa uma função ou biblioteca e a def respondera para você de forma colorida.
    """
    sleep(1)
    titulo(f"Acessando o manual do comando {a}", 1)
    sleep(1.5)
    print("\33[7m")
    help(com)
    print("\33[m")


a = ""
while True:
    titulo("Sistema de ajuda PyHelp", 3)
    a = str(input("Função ou Biblioteca [fim finaliza]>")).lower().strip()
    if a == "fim":
        sleep(1)
        break
    else:
        ajuda(a)
titulo("Fim do programa", 2)
