import pandas as pd
import matplotlib.pyplot as plt
dados = pd.read_csv("C:/Users/Pablo/Aprendendo-Python/MachineLearning/athlete_events.csv")

dados.boxplot(column="Age")
plt.show()


dados.hist(column = "Age", bins= 100)
plt.show()


masculino = dados.loc[dados["Sex"]== "M"]
a = masculino["Height"]
p = masculino["Weight"]
plt.scatter(a,p)
plt.show()


feminino = dados.loc[dados["Sex"] == "F"]
tam = feminino["Height"]
peso = feminino["Weight"]
ida = feminino["Age"]
plt.scatter(tam,peso,ida)
plt.show()