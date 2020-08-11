c = str(input("Digite o nome da sua cidade:")).capitalize()
a = c.find("Santo")
if a == 0:
    print("Sua cidade começa com santo")
else:
    print("Sua cidade não começa com santo")