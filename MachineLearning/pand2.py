import pandas as pd

def linha():
    print(40*"-")


alunos = {"Nome":["Paulo","Pablo","Aline","Laysa"],
          "Nota":[4,7,5.5,9],
          "Aprovado":["Não","Sim","Não","Sim"]}
alunosDF = pd.DataFrame(alunos)
dados = alunosDF
print(alunosDF)
linha()
print(alunosDF.shape)
linha()
print(alunosDF.describe())
linha()
print(alunosDF["Nome"])
linha()
print(alunosDF.loc[[2]])
linha()
print(alunosDF.loc[alunosDF["Aprovado"]=="Sim"])
linha()
print(dados["Nome"].value_counts())
linha()
alunosDF.drop("Nome", axis = 1 , inplace = True)
print(alunosDF)
linha()
