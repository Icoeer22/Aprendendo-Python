import random
pc = random.choice(["PEDRA", "PAPEL", "TESOURA"])
ps = str(input("Escola PEDRA / PAPEL / TESOURA e jogue com o PC:")).upper().strip()
print(f"Voçe escolheu {ps} e o PC escolheu {pc} logo:")
if ps == pc:
    print("EMPATOU")
elif pc == "PEDRA" and ps == "TESOURA":
    print("PC WIN")
elif pc == "PEDRA" and ps == "PAPEL":
    print("VOCÊ WIN")
elif pc == "TESOURA" and ps == "PAPEL":
    print("PC WIN")
elif pc == "TESOURA" and ps == "PEDRA":
    print("VOCE WIN")
elif pc == "PAPEL" and ps == "TESOURA":
    print("VOCE WIN")
elif pc == "PAPEL" and ps == "PEDRA":
    print("PC WIN")