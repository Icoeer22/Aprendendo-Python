lista = []
mai = men = 0
m = 0
n = 0
for a in range(0,5):
    b = (int(input("Digite um número:")))
    lista.append(b)
    if a == 0:
        mai = men = b
        m = n = a
    else:
        if b > mai:
            mai = b
            m = a
        if b < men:
            men = b
            n = a
print(f"A lista de números é {lista}")
print(f"O maior número é {mai} e está na posição ", end="")
for i, v in enumerate(lista):
    if v == mai:
        print(f"{i}..." , end="")
print()
print(f"O menor número é {men} e está na posição ",end="")
for i , v in enumerate(lista):
    if v == men:
        print(f"{i}...",end="")