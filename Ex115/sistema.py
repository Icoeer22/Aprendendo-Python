from Ex115.lib.interface import *
from Ex115.lib.arquivo import *
from time import sleep

arq = "almas.txt"

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(["Ver Pessoas Cadastradas", "Cadastrar Nova Pessoa", "Sair Do Programa"])
    if resposta == 1:
        mostra(arq)
    elif resposta == 2:
        cabeçalho("Cadastrar Nova Pessoa")
        colet()
    elif resposta == 3:
        colet()
        break
    else:
        print("\33[31mERRO!, Digite uma opção válida!\33[m")
    sleep(1)