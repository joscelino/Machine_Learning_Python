# -*- coding: utf-8 -*-
from rbm import RBM
import numpy as np
from typing import Dict, List

rbm: Dict = RBM(num_visible=6, num_hidden=2)

base = np.array([[1, 1, 1, 0, 0, 0],
                 [1, 0, 1, 0, 0, 0],
                 [1, 1, 1, 0, 0, 0],
                 [0, 0, 1, 1, 1, 1],
                 [0, 0, 1, 1, 0, 1],
                 [0, 0, 1, 1, 0, 1]])

produto: List = ["Combo 1", "Combo 2", "Combo 3", "Coxinha", "Acai no copo", "Acai na barca"]

rbm.train(base, max_epochs = 5000)
rbm.weights

cliente1 = np.array([[1, 0, 1, 1, 0, 0]])
cliente2 = np.array([[0, 0, 0, 1, 1, 0]])

rbm.run_visible(cliente1)
rbm.run_visible(cliente2)

camada_escondida = np.array([[0, 1]])
recomendacao = rbm.run_hidden(camada_escondida)

for i in range(len(cliente1[0])):
    #print(cliente1[0], i)
    if cliente1[0, i] == 0 and recomendacao[0, i] == 1:
        print(produto[i])

