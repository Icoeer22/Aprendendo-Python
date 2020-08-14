c= 0
while True:
    a = int(input("Você deseja saber a tabuáda de qual número:"))
    if a < 0:
        break
    else:
        print(15*"=")
        while True:
            if c == 10:
                print(15*"=")
                c = 0
                break
            c+=1
            print(f"{a} X {c} = {a*c}")
print("Obrigado por usar este programa!!!")