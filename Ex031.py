ds = float(input("Digite a distancia da viagem:"))
if ds > 200:
    print(f"O preço daviagem vai ficar {ds*0.45} reais")
else:
    print(f"O preço da viagem vai ficar {ds*0.50} reais")