# -*- coding: utf-8 -*-
# Importacao das bibliotecas
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets, metrics
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.neural_network import BernoulliRBM
from sklearn.naive_bayes import GaussianNB
from sklearn.pipeline import Pipeline

# Importacao da base de dados
base = datasets.load_digits()

# Criacao das variaveis
previsores = np.asarray(base.data, 'float32')
classe = base.target

# Normalizacao dos dados
normalizador = MinMaxScaler(feature_range = (0, 1))
previsores = normalizador.fit_transform(previsores)

# Dividindo entre treinamento e teste
previsores_treinamento, previsores_teste, classe_treinamento, classe_teste = train_test_split(previsores, classe,
                                                                                              test_size = 0.2, random_state = 0)

# Criando a RBM
rbm = BernoulliRBM(random_state = 0)
rbm.n_iter = 25
rbm.n_components = 50
naive_rbm = GaussianNB()

# Definindo o classificador com Pipeline (para executar mais de um processo de uma vez)
classificador_rbm = Pipeline(steps = [('rbm', rbm), ('naive', naive_rbm)])
classificador_rbm.fit(previsores_treinamento, classe_treinamento)

# Visualizando as imagens geradas
plt.figure(figsize = (20,20))
for i, comp in enumerate(rbm.components_):
    plt.subplot(10, 10, i + 1)
    plt.imshow(comp.reshape(8,8), cmap=plt.cm.gray_r)
    plt.xticks(())
    plt.yticks(())
plt.show()

# Analise das previsoes utilizando a reducao de dimensionalidade
previsoes_rbm = classificador_rbm.predict(previsores_teste)
precisao_rbm = metrics.accuracy_score(previsoes_rbm, classe_teste)

# Analise de previsoes sem a utilizacao da reducao de dimensionalidade
naive_simples = GaussianNB()
naive_simples.fit(previsores_treinamento, classe_treinamento)
previsoes_naive = naive_simples.predict(previsores_teste)
precisao_naive = metrics.accuracy_score(previsoes_naive, classe_teste)

