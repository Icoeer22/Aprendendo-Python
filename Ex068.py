import random
v = 0
ps =" "

while True:
    pc = random.randint(0,10)
    while ps not in "PI":
        ps = str(input("Você gostaria de Par ou Impar:")).upper().strip()
    psn = int(input("Escolha um número de 0 á 10:"))
    if ps[0] == "I":
        if (pc+psn) % 2 == 0:
            print(f"O pc escolheu {pc} e você {psn} ")
            print("Que pena você perdeu")
            print(15*"-=")
            break
        else:
            print(f"O pc escolheu {pc} e você {psn} ")
            print("Você ganhou essa!!!")
            v +=1
            print(15 * "-=")
    if ps[0] == "P":
         if (pc+psn) % 2 == 0:
            print(f"O pc escolheu {pc} e você {psn} ")
            print("Você ganhou essa!!!")
            v+=1
            print(15 * "-=")
         else:
            print(f"O pc escolheu {pc} e você {psn} ")
            print("Que pena você perdeu")
            print(15 * "-=")
            break
    ps =" "
print(f"Você ganhou {v} vezes seguidas!!!")