import pandas as pd
import matplotlib.pyplot as plt
dados = pd.read_excel('C:/Users/Pablo/Aprendendo-Python/MachineLearning/a1.xlsx')
print(dados.head(6))
print(40*"-")

alunos = {"Nome":["Paulo","Pablo","Aline","Laysa", "Carla", "Marisa", "Édina","Pedro"],
          "Nota":[4, 7,5.5,9,10,6.8,4,4],
          "Aprovado":["Não","Sim","Não","Sim","Sim","Sim","Sim","Não"]}
alunospd = pd.DataFrame(alunos)
print(alunospd)
print(40*"-")
objeto =  pd.Series(["Pablo","Carla","Laysa","Guilherme"])
print(objeto)
print(40*"-")
objeto1 = pd.Series([1,2,3,4,5,6,7,8,9,0])
print(objeto1)
dados.rename(columns={"Numeros":"Numbers"}, inplace=True)
print(dados)
print(40*"-")
alunospd.hist(column = "Nota",bins = 100)
plt.show()
