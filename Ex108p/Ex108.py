from Ex108p import Def108

p = float(input("Digite um preço: R$"))
print(f"A metade de {Def108.formato(p)} é {Def108.formato(Def108.metade(p))}")
print(f"O dobro de {Def108.formato(p)} é {Def108.formato(Def108.dobro(p))}")
print(f"Um aumento de 10%, temos {Def108.formato(Def108.aumento(p))}")
print(f"Uma redução de 13%, temos {Def108.formato(Def108.reducao(p))}")
