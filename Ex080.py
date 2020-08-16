list = []
for a in range(0,5):
    b = int(input("Digite um número:"))
    if a == 0 or b > list[-1]:
        list.append(b)
    else:
        pos = 0
        while pos < len(list):
            if b <= list[pos]:
                list.insert(pos,b)
                break
            pos+=1
print(list)
