n = str(input("Digite seu nome:")).upper().strip()
a = n.find("SILVA")
if a >= 0:
    print("TEM SILVA")
elif a == -1:
    print("Não tem silva")