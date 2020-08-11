from datetime import datetime
a = int(input("Digite o ano de nacimento do seu atleta:"))
t = datetime.now()
c = t.year - a
if c < 9:
    print("MIRIM")
elif 9 <= c < 14:
    print('INFANTIL')
elif 14 <= c < 19:
    print("JUNIOR")
elif 19 <= c <= 20:
    print("SENIOR")
elif c > 20:
    print("MASTER")
