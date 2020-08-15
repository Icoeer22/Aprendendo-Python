ne = ("Zero","Um","Dois","Três","Quatro","Cinco","Seis","Sete","Oito","Nove","Dez","Onze","Doze","Treze","Catorze","Quinze","Dezesseis","Dezessete","Dezoito","Dezenove","Vinte")
while True:
    n = int(input("Digite um número entre 0 e 20 para sabe-lo por extenso: "))
    if 0 <= n <= 20:
        break
print(30*"-=")
print(f"O numero {n} por extenso é {ne[n]}")
print(30*"-=")