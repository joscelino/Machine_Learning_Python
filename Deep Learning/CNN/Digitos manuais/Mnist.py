# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Flatten, Dropout
from keras.utils import np_utils
from keras.layers import Conv2D, MaxPooling2D
from keras.layers.normalization import BatchNormalization

# Carregamento da base de dados
(X_treinamento, y_treinamento), (X_teste, y_teste) = mnist.load_data()

# Visualizar imagens
plt.imshow(X_treinamento[5])
plt.imshow(X_treinamento[5], cmap = 'gray')
plt.title('Classe' + str(y_treinamento[5]))

previsores_treinamento = X_treinamento.reshape(X_treinamento.shape[0],
                                               28, 28, 1)
previsores_teste = X_teste.reshape(X_teste.shape[0], 28, 28, 1)
previsores_treinamento = previsores_treinamento.astype('float32')
previsores_teste = previsores_teste.astype('float32')

# Alterando a escala dos previsores
previsores_treinamento /= 255
previsores_treinamento /= 255

# Criando variaveis dummy para substituir as variaveis categoricas
classe_treinamento = np_utils.to_categorical(y_treinamento, 10)
classe_teste = np_utils.to_categorical(y_teste, 10)

# Criando a Rede Neural
classificador = Sequential()
# Primeira Camada de Convolucao
classificador.add(Conv2D(32, (3,3), input_shape=(28, 28, 1), 
                         activation = 'relu'))
# Normalizacao da camada de convolucao
classificador.add(BatchNormalization())
# Camada de Pooling
classificador.add(MaxPooling2D(pool_size = (2, 2)))
# Segunda Camada de Convolucao
classificador.add(Conv2D(32, (3,3), activation = 'relu'))
# Normalizacao da camada de convolucao
classificador.add(BatchNormalization())
# Camada de Pooling
classificador.add(MaxPooling2D(pool_size = (2, 2)))
# Camada de flattening
classificador.add(Flatten())
# Gerando a Rede Neural Densa
classificador.add(Dense(units = 128, activation = 'relu'))
# Camada de Dropout
classificador.add(Dropout(0.2))
# Camada Oculta
classificador.add(Dense(units = 128, activation = 'relu'))
# Camada de Dropout
classificador.add(Dropout(0.2))
# Camada de Saida
classificador.add(Dense(units = 10, activation = 'softmax'))
# Compilacao da Rede Neural
classificador.compile(loss= 'categorical_crossentropy',
                      optimizer = 'adam', metrics = ['accuracy'])
classificador.fit(previsores_treinamento, classe_treinamento,
                   batch_size = 128, epochs = 5, 
                   validation_data = (previsores_teste, classe_teste))

resultado = classificador.evaluate(previsores_teste, classe_teste)

