import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import ExtraTreesClassifier
#Abrindo o arquivo que contem dados
arquivo = pd.read_csv("C:/Users/Pablo/Aprendendo-Python/MachineLearning/wines.csv")
arquivo.head()
#Trocando os dados escolhidos para analise de string para numero
arquivo["style"] = arquivo["style"].replace("red", 0)
arquivo["style"] = arquivo["style"].replace("white", 1)
#Separando arquivos em preditoras e variavel alvo
y = arquivo["style"]
x = arquivo.drop("style", axis =1)
#Criando dados para treino e dados para teste real
x_treino , x_teste , y_treino , y_teste = train_test_split(x,y , test_size=0.3)
#Criando modelo
modelo = ExtraTreesClassifier()
modelo.fit(x_treino, y_treino)
#Imprimindo resultado real
resultado = modelo.score(x_teste,y_teste)
print(f"O robo acertou {resultado*100:.1f}%")
#Prevendo alguns
prever = modelo.predict(x_teste[400:403])
print(prever)
#Mandei printar o y na mesma possição para saber se o bot acertou
print(y_teste[400:403])