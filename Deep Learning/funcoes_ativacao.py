# -*- coding: utf-8 -*-
import numpy as np

# transfer function
def stepFunction(soma):
    if (soma >= 1):
        return 1
    return 0

# funcao sigmoide
def sigmoidFunction(soma):
    return 1 / (1 + np.exp(-soma))

# funcao Tangente Hiperbolica
def tahnFunction(soma):
    return (np.exp(soma) - np.exp(-soma)) / (np.exp(soma) + np.exp(-soma))

# funcao ReLU (rectified linear units)
def reluFunction(soma):
    if soma >= 0:
        return soma
    return 0

# funcao linear
def linearFunction(soma):
    return soma

# funcao Softmax
def softmaxFunction(x):
    ex = np.exp(x)
    return ex / ex.sum()

valores = [5.0, 2.0, 1.3]
print(softmaxFunction(valores))

    
