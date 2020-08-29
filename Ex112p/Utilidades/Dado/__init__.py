def leiaValor(msg):
   valido = False
   while not valido:
       entrada = str(input(msg)).replace(",",".").strip()
       if entrada.isalpha() or entrada.strip() == "" :
           print( " \33[0;31mErro, Valor inválido! \33[m")
       else:
           valido = True
           return float(entrada)

