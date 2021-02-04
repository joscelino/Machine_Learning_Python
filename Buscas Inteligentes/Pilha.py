# -*- coding: utf-8 -*-
"""
Pilha
"""

# Classe de analise da pilha
class Pilha:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.cidades = [None] * self.tamanho
        self.topo = -1
        
    def empilhar(self, cidade):
        if not Pilha.pilhaCheia(self):
            self.topo += 1
            self.cidades[self.topo] = cidade
        else:
            print("Impossivel empilhar - PILHA CHEIA!")
        
    def desempilhar(self):
        if not Pilha.pilhaVazia(self):
            temp = self.cidades[self.topo]
            self.topo -= 1
            return temp
        else:
            print("Impossivel desempilhar - PILHA VAZIA!")
            return None
    
    def getTopo(self):
        return self.cidades[self.topo]
    
    def pilhaVazia(self):
        return (self.topo == -1)
    
    def pilhaCheia(self):
        return (self.topo == self.tamanho - 1)
    
from Mapa import Mapa
mapa = Mapa()
pilha = Pilha(5)
pilha.empilhar(mapa.portoUniao)
pilha.empilhar(mapa.campoLargo)
pilha.empilhar(mapa.canoinhas)
pilha.getTopo().nome
pilha.desempilhar()
pilha.empilhar(mapa.curitiba)
pilha.empilhar(mapa.curitiba)
pilha.empilhar(mapa.tijucas)
pilha.empilhar(mapa.mafra)
pilha.desempilhar()     
