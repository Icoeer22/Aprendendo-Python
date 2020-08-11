p = float(input("Informe o preço do produto:"))
print("[1] Dinheiro ou Cheque")
print("[2] Cartão")
print("[3] Em 2x no cartão")
print("[4] Em 3x ou mais no cartão")
c = int(input("Qual o modo de pagamento:"))
if c == 1:
    print(f"O valor do produto com 10% de desconto fica {(p*90)/100}")
elif c == 2:
    print(f"O valor do produto com 5% fica {(p*95)/100}")
elif c == 3:
    print(f"O valor do produto fica o mesmo {p}")
elif c ==4:
    print(f"O valor do produto com 20% de juros fica {(p*120)/100}")