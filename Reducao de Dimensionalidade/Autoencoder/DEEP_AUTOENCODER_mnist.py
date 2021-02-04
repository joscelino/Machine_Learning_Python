# -*- coding: utf-8 -*-
# Importacao das bibliotecas
import numpy as np
import matplotlib.pyplot as plt
from keras.datasets import mnist
from keras.models import Model, Sequential
from keras.layers import Input, Dense

# Definicao das Variaveis
(previsores_treinamento, _), (previsores_teste, _) = mnist.load_data()

# Normalizacao dos dados
previsores_treinamento = previsores_treinamento.astype('float32') / 255
previsores_teste = previsores_teste.astype('float32') / 255

# Reshape para o padrao de dimensoes do Keras
previsores_treinamento = previsores_treinamento.reshape((len(previsores_treinamento), np.prod(previsores_treinamento.shape[1:])))
previsores_teste = previsores_teste.reshape((len(previsores_teste), np.prod(previsores_teste.shape[1:])))

# Criando o autoencoder
autoencoder = Sequential()

# Criando o Encode
autoencoder.add(Dense(units = 128, activation = 'relu', input_dim = 784))
autoencoder.add(Dense(units = 64, activation = 'relu'))
autoencoder.add(Dense(units = 32, activation = 'relu'))

# Criando o Decode
autoencoder.add(Dense(units = 64, activation = 'relu'))
autoencoder.add(Dense(units = 128, activation = 'relu'))
autoencoder.add(Dense(units = 784, activation = 'sigmoid'))

# Visualizando os detalhes
autoencoder.summary()

# Compilando a Rede Neural
autoencoder.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])

# Treinamento da Rede
autoencoder.fit(previsores_treinamento, previsores_treinamento, epochs = 50, batch_size = 256, 
                validation_data = (previsores_teste, previsores_teste))

# Capturando o codificador
dimensao_original = Input(shape=(784, ))
camada_encoder1 = autoencoder.layers[0]
camada_encoder2 = autoencoder.layers[1]
camada_encoder3 = autoencoder.layers[2]

# Criando o encoder
encoder = Model(dimensao_original, camada_encoder3(camada_encoder2(camada_encoder1(dimensao_original))))

# Visualizando os detalhes
encoder.summary()

# Criando variaveis codificadas e decodificadas
imagens_codificadas = encoder.predict(previsores_teste)
imagens_decodificadas = autoencoder.predict(previsores_teste)

# Visualizando as imagens
numero_imagens = 10
imagens_teste = np.random.randint(previsores_teste.shape[0], size = numero_imagens)
plt.figure(figsize=(18, 18))
for i, indice_imagem in enumerate(imagens_teste):
    #print(i)
    #print(indice_imagem)
    # Imagem Original
    eixo = plt.subplot(10, 10, i+1)
    plt.imshow(previsores_teste[indice_imagem].reshape(28,28)) # 28 e 28 sao as dimensoes originais
    plt.xticks()
    plt.yticks()
    plt.show()
    # Imagem Codificada
    eixo = plt.subplot(10, 10, i+1+numero_imagens)
    plt.imshow(imagens_codificadas[indice_imagem].reshape(8,4)) # 8 e 4 sao as dimensoes que resultam em 32
    plt.xticks()
    plt.yticks()
    plt.show()
    # Imagem reconstruida
    eixo = plt.subplot(10, 10, i+1+numero_imagens*2)
    plt.imshow(imagens_decodificadas[indice_imagem].reshape(28,28)) # 28 e 28 [ara retornar a dimensao original
    plt.xticks()
    plt.yticks()
    plt.show()
