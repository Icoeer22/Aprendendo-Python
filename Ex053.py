a = str(input("Digite uma frase:")).upper().strip()
b =   a.split()
c = "".join(b)
d = ""
for e in range(len(a)-1, -1, -1):
    d += c[e]
if d == c:
    print("Palindromo")
else:
    print("no palindromo")