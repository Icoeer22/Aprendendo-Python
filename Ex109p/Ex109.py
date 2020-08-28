from Ex109p import Def109

p = float(input("Digite um preço: R$"))
print(f"A metade de {Def109.formato(p)} é {Def109.metade(p, False)}")
print(f"O dobro de {Def109.formato(p)} é {Def109.dobro(p, True)}")
print(f"Um aumento de 10%, temos {Def109.aumento(p,False)}")
print(f"Uma redução de 13%, temos {Def109.reducao(p,True)}")
