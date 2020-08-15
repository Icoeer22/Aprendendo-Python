preco = ("Pão", 1, "Borracha", 3 , "Livro", 15, "Jogo", 200)
print(39*"-")
print("Listagem de Preçõs".center(39))
print(39*"-")
for a in range(0,len(preco)):
    if a%2==0:
        print(f"{preco[a]:.<30}",end="")
    else:
        print(f"R${preco[a]:>7.2f}")
