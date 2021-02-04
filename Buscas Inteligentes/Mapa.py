from Cidade import Cidade
from Adjacente import Adjacente

class Mapa:

    portoUniao = Cidade("Porto União")
    pauloFrontin = Cidade("Paulo Frontin")
    canoinhas = Cidade("Canoinhas")
    irati = Cidade("Irati")
    palmeira = Cidade("Palmeira")
    campoLargo = Cidade("Campo Largo")
    curitiba = Cidade("Curitiba")
    balsaNova = Cidade("Balsa Nova")
    araucaria = Cidade("Araucária")
    saoJose = Cidade("São José dos Pinhais")
    contenda = Cidade("Contenda")
    mafra = Cidade("Mafra")
    tijucas = Cidade("Tijucas do Sul")
    lapa = Cidade("Lapa")
    saoMateus = Cidade("São Mateus do Sul")
    tresBarras = Cidade("Três Barras")
    
    portoUniao.addCidadeAdjacente(Adjacente(pauloFrontin))  
    portoUniao.addCidadeAdjacente(Adjacente(canoinhas))
    portoUniao.addCidadeAdjacente(Adjacente(saoMateus))
       
    pauloFrontin.addCidadeAdjacente(Adjacente(portoUniao))
    pauloFrontin.addCidadeAdjacente(Adjacente(irati))
    
    canoinhas.addCidadeAdjacente(Adjacente(portoUniao))
    canoinhas.addCidadeAdjacente(Adjacente(tresBarras))
    canoinhas.addCidadeAdjacente(Adjacente(mafra))
    
    irati.addCidadeAdjacente(Adjacente(pauloFrontin))
    irati.addCidadeAdjacente(Adjacente(palmeira))
    irati.addCidadeAdjacente(Adjacente(saoMateus))
    
    palmeira.addCidadeAdjacente(Adjacente(irati))
    palmeira.addCidadeAdjacente(Adjacente(saoMateus))
    palmeira.addCidadeAdjacente(Adjacente(campoLargo))
    
    campoLargo.addCidadeAdjacente(Adjacente(palmeira))
    campoLargo.addCidadeAdjacente(Adjacente(balsaNova))
    campoLargo.addCidadeAdjacente(Adjacente(curitiba))
    
    curitiba.addCidadeAdjacente(Adjacente(campoLargo))
    curitiba.addCidadeAdjacente(Adjacente(balsaNova))
    curitiba.addCidadeAdjacente(Adjacente(araucaria))
    curitiba.addCidadeAdjacente(Adjacente(saoJose))
    
    balsaNova.addCidadeAdjacente(Adjacente(curitiba))
    balsaNova.addCidadeAdjacente(Adjacente(campoLargo))
    balsaNova.addCidadeAdjacente(Adjacente(contenda))
    
    araucaria.addCidadeAdjacente(Adjacente(curitiba))
    araucaria.addCidadeAdjacente(Adjacente(contenda))
    
    saoJose.addCidadeAdjacente(Adjacente(curitiba))
    saoJose.addCidadeAdjacente(Adjacente(tijucas))
    
    contenda.addCidadeAdjacente(Adjacente(balsaNova))
    contenda.addCidadeAdjacente(Adjacente(araucaria))
    contenda.addCidadeAdjacente(Adjacente(lapa))

    mafra.addCidadeAdjacente(Adjacente(tijucas))
    mafra.addCidadeAdjacente(Adjacente(lapa))
    mafra.addCidadeAdjacente(Adjacente(canoinhas))
    
    tijucas.addCidadeAdjacente(Adjacente(mafra))
    tijucas.addCidadeAdjacente(Adjacente(saoJose))

    lapa.addCidadeAdjacente(Adjacente(contenda))
    lapa.addCidadeAdjacente(Adjacente(saoMateus))
    lapa.addCidadeAdjacente(Adjacente(mafra))
    
    saoMateus.addCidadeAdjacente(Adjacente(palmeira))
    saoMateus.addCidadeAdjacente(Adjacente(irati))
    saoMateus.addCidadeAdjacente(Adjacente(lapa))
    saoMateus.addCidadeAdjacente(Adjacente(tresBarras))
    saoMateus.addCidadeAdjacente(Adjacente(portoUniao))
    
    tresBarras.addCidadeAdjacente(Adjacente(saoMateus))
    tresBarras.addCidadeAdjacente(Adjacente(canoinhas))
    
'''mapa = Mapa()
mapa.portoUniao.nome
mapa.portoUniao.visitado
mapa.portoUniao.adjacentes
mapa.portoUniao.distanciaObjetivo
for i in range(len(mapa.portoUniao.adjacentes)):
    print(mapa.portoUniao.adjacentes[i].cidade.nome)'''
