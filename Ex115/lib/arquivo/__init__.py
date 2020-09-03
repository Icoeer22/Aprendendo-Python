from Ex115.lib.interface import *


def arquivoExiste(nome):
    try:
        a = open(nome, "rt")
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        a = open(nome, "wt+")
        a.close()
    except:
        print("Erro ao criar arquivo!")
    else:
        print(f"Arquivo {nome} criado com sulcesso!")


def mostra(nome):
    try:
        a = open(nome, "rt")
    except:
        print("Erro ao ler arquivo!")
    else:
        cabeçalho("Ver Pessoas Cadastradas")
        for linha in a:
            valores = linha.split("\n")
            print(valores[0])



def colet():
    while True:
        nome = str(input("Nome:")).title()
        if nome.isnumeric():
            print("\33[31mERRO! Tipo de dado inválido!\33[m")
        else:
            break
    idade = leiaInt("Idade:")
    print(f"Novo registro de {nome} adcionado.")
    arquivo = open("almas.txt", "a")
    nom = []
    ida = []
    nom.append(f"{nome}".ljust(33))
    ida.append(str(f"{idade:>3} anos\n"))
    arquivo.writelines(nom)
    arquivo.writelines(ida)
    arquivo.close()
    nom.clear()
    ida.clear()

