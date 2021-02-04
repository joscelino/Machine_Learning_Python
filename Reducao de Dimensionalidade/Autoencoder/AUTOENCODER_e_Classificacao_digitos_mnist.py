# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
# Importacao das bibliotecas
import numpy as np
import matplotlib.pyplot as plt
from keras.datasets import mnist
from keras.models import Model, Sequential
from keras.layers import Input, Dense
from keras.utils import np_utils

# Definicao das Variaveis
(previsores_treinamento, classe_treinamento), (previsores_teste, classe_teste) = mnist.load_data()

# Normalizacao dos dados
previsores_treinamento = previsores_treinamento.astype('float32') / 255
previsores_teste = previsores_teste.astype('float32') / 255
classe_dummy_treinamento = np_utils.to_categorical(classe_treinamento)
classe_dummy_teste = np_utils.to_categorical(classe_teste)

# Reshape para o padrao de dimensoes do Keras
previsores_treinamento = previsores_treinamento.reshape((len(previsores_treinamento), np.prod(previsores_treinamento.shape[1:])))
previsores_teste = previsores_teste.reshape((len(previsores_teste), np.prod(previsores_teste.shape[1:])))

# Criando o autoencoder
autoencoder = Sequential()

# Criando a Rede Neural
autoencoder.add(Dense(units = 32, activation = 'relu', input_dim = 784))
autoencoder.add(Dense(units = 784, activation = 'sigmoid'))

# Visualizando a estrutura da Rede Neural
autoencoder.summary()

# Compilando a Rede Neural
autoencoder.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])

# Treinamento da Rede
autoencoder.fit(previsores_treinamento, previsores_treinamento, epochs = 50, batch_size = 256, 
                validation_data = (previsores_teste, previsores_teste))

# Capturando o codificador
dimensao_original = Input(shape=(784, ))
camada_encoder = autoencoder.layers[0]

# Criando o novo modelo
encoder = Model(dimensao_original, camada_encoder(dimensao_original))

# Previsores codificados
previsores_treinamento_codificados = encoder.predict(previsores_treinamento)
previsores_teste_codificados = encoder.predict(previsores_teste)

# A seguir serao criadas 2 Redes Neurais para comparativo
# Primeira Rede Neural (sem reducao de dimensionalidade)
c1 = Sequential()
c1.add(Dense(units = 397, activation = 'relu', input_dim = 784))
c1.add(Dense(units = 397, activation = 'relu'))
c1.add(Dense(units = 10, activation = 'softmax'))

# Compilando a Rede Neural
c1.compile(optimizer = 'adam', loss = 'categorical_crossentropy', metrics = ['accuracy'])

# Treinamento da Rede Neural
c1.fit(previsores_treinamento, classe_dummy_treinamento, epochs = 100, batch_size = 256, 
                validation_data = (previsores_teste, classe_dummy_teste))

# Previsores codificados
previsores_treinamento_codificados = encoder.predict(previsores_treinamento)
previsores_teste_codificados = encoder.predict(previsores_teste)

# A seguir serao criadas 2 Redes Neurais para comparativo
# Segunda Rede Neural (com reducao de dimensionalidade)
c2 = Sequential()
c2.add(Dense(units = 21, activation = 'relu', input_dim = 32))
c2.add(Dense(units = 21, activation = 'relu'))
c2.add(Dense(units = 10, activation = 'softmax'))

# Compilando a Rede Neural
c2.compile(optimizer = 'adam', loss = 'categorical_crossentropy', metrics = ['accuracy'])

# Treinamento da Rede Neural
c2.fit(previsores_treinamento_codificados, classe_dummy_treinamento, epochs = 100, batch_size = 256, 
                validation_data = (previsores_teste_codificados, classe_dummy_teste))