import pandas as pd

dados = pd.read_excel('C:/Users/Pablo/Aprendendo-Python/MachineLearning/a1.xlsx')
print(dados.head(6))
print(40*"-")

alunos = {"Nome":["Paulo","Pablo","Aline","Laysa"],
          "Nota":[4,7,5.5,9],
          "Aprovado":["Não","Sim","Não","Sim"]}
alunospd = pd.DataFrame(alunos)
print(alunospd)
print(40*"-")
objeto =  pd.Series(["Pablo","Carla","Laysa","Guilherme"])
print(objeto)
print(40*"-")
objeto1 = pd.Series([1,2,3,4,5,6,7,8,9,0])
print(objeto1)