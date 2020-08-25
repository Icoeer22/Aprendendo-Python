def notas(*num, sit= False):
    r = dict()
    r["Total"] = len(num)
    r["Maior"] = max(num)
    r["Menor"] = min(num)
    r["Média"] = sum(num)/len(num)
    if sit:
        if r["Média"] >= 7:
            r["Situação"] = "Boa"
        elif r["Média"] >= 5:
            r["Situação"] = "Rasoavel"
        else:
            r["Situação"] = "Ruim"
    return r



#Principal
resp = notas (2, 3 , 10 , 5 , 7 , sit=True)
print(resp)