r= "S"
m = 0
d = 0
mai = 0
men = 0
while r == "S":
    a = int(input("Digite um número:"))
    if d == 0:
        mai = men = a
    else:
        if a > mai:

            mai = a
        if a < men:
            men = a
    m +=a
    d +=1
    r = str(input("Quer continua [S/N]:")).upper().strip()
print(f"A media é {m/d}")
print(f"O maior numero é {mai}")
print(f"O menor numero é {men}")