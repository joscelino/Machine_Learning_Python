# -*- coding: utf-8 -*-
# Importacao das bibliotecas
import numpy as np
import matplotlib.pyplot as plt
from keras.datasets import mnist
from keras.models import Model, Sequential
from keras.layers import Input, Dense, Conv2D, MaxPooling2D, UpSampling2D, Flatten, Reshape

# Definicao das Variaveis
(previsores_treinamento, _), (previsores_teste, _) = mnist.load_data()

# Reshape para o padrao de dimensoes do Keras
previsores_treinamento = previsores_treinamento.reshape((len(previsores_treinamento), 28, 28, 1))
previsores_teste = previsores_teste.reshape((len(previsores_teste), 28, 28, 1))

# Normalizacao dos dados
previsores_treinamento = previsores_treinamento.astype('float32') / 255
previsores_teste = previsores_teste.astype('float32') / 255

# Criar o autoencoder
autoencoder = Sequential()

# Encoder
autoencoder.add(Conv2D(filters = 16, kernel_size = (3, 3), activation = 'relu', 
                       input_shape = (28, 28, 1)))

# Camada de MaxPooling
autoencoder.add(MaxPooling2D(pool_size = (2, 2)))

# Camadas da Rede de Convolucao
autoencoder.add(Conv2D(filters = 8, kernel_size = (3, 3), activation = 'relu', padding='same'))
autoencoder.add(MaxPooling2D(pool_size = (2, 2), padding='same')) #Parametro 'padding' indica como a imagem sera passada
autoencoder.add(Conv2D(filters = 8, kernel_size = (3, 3), activation = 'relu', padding='same', strides = (2, 2)))

# Transformando a saida em um vetor
autoencoder.add(Flatten())

# Reshape do Flatten
autoencoder.add(Reshape((4, 4, 8)))

# Processo de Decoder
autoencoder.add(Conv2D(filters = 8, kernel_size = (3, 3), activation = 'relu', padding='same'))
# Aumentando a Dimensionalidade
autoencoder.add(UpSampling2D(size = (2, 2)))
# Inserindo camadas da Rede
autoencoder.add(Conv2D(filters = 8, kernel_size = (3, 3), activation = 'relu', padding='same'))
autoencoder.add(UpSampling2D(size = (2, 2)))
autoencoder.add(Conv2D(filters = 16, kernel_size = (3, 3), activation = 'relu'))
autoencoder.add(UpSampling2D(size = (2, 2)))
autoencoder.add(Conv2D(filters = 1, kernel_size = (3, 3), activation = 'sigmoid', padding='same'))

# Visualizando estrutura
autoencoder.summary()

# Compilacao da Rede
autoencoder.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])

# Treinamento da Rede
autoencoder.fit(previsores_treinamento, previsores_treinamento, epochs = 50, batch_size = 256, 
                validation_data = (previsores_teste, previsores_teste))

# Encoder
encoder = Model(inputs = autoencoder.input, outputs = autoencoder.get_layer('flatten_1').output)
encoder.summary()

# Imagens codificadas
imagens_codificadas = encoder.predict(previsores_teste)

# Decodificando as imagens
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
    plt.imshow(imagens_codificadas[indice_imagem].reshape(16,8)) # 16 e 8 sao as dimensoes que resultam em 32
    plt.xticks()
    plt.yticks()
    plt.show()
    # Imagem reconstruida
    eixo = plt.subplot(10, 10, i+1+numero_imagens*2)
    plt.imshow(imagens_decodificadas[indice_imagem].reshape(28,28)) # 28 e 28 [ara retornar a dimensao original
    plt.xticks()
    plt.yticks()
    plt.show()