from datetime import date


def voto(num):
    d = date.today()
    i = d.year-num
    if i >= 18:
        return f"Com {i} anos: Voto obrigatório."
    elif 16 <=i < 18 or i > 65:
        return f"Com {i} anos: Voto opcional."
    elif i < 16:
        return f"Com {i} anos: Inválido a votar."

p1 = voto(int(input("Digite seu ano de nascimento, para ser informado sobre sua condição de votação:")))
print(p1)
