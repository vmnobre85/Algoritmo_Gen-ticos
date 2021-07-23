#%%

from random import choices
from random import randint
from numpy import exp
from numpy import log as ln


def calcula_peso_mochila(mochila, pesos):


    peso_mochila = 0
        
    for i in range(0, len(mochila)):
        peso_objeto = pesos[i]     
        zero_ou_um = mochila[i]     
        peso_mochila += zero_ou_um*peso_objeto

    return peso_mochila

def calcula_pesos_populacao(populacao, pesos):

    pesos_mochilas = []

    for mochila in populacao:
        peso_total = calcula_peso_mochila(mochila, pesos)
        pesos_mochilas.append(peso_total)

    return pesos_mochilas

def calcula_valor_mochila(mochila, valores):

    valor_mochila = 0
    
    for i in range(0, len(mochila)):
        valor_objeto = valores[i]     
        zero_ou_um = mochila[i]     
        valor_mochila += zero_ou_um*valor_objeto

    return valor_mochila

def calcula_valores_populacao(populacao, valores):

    valores_mochilas = []

    for mochila in populacao:
        valor_total = calcula_valor_mochila(mochila, valores)
        valores_mochilas.append(valor_total)

    return valores_mochilas

def cruzamento(populacao, pais):

    n_objetos = len(populacao[0])
    nova_populacao = []
    nova_populacao.append(populacao[0])    

    for i in range(0, len(pais)):
        mae_index = pais[i][0]
        pai_index = pais[i][1]
        mae = populacao[mae_index]
        pai = populacao[pai_index]
        local_corte = randint(1, n_objetos)
    
        filho = mae[0:local_corte] + pai[local_corte:]
        nova_populacao.append(filho)

    return nova_populacao

def decodifica_mochila(mochila, nomes, valores, pesos):
    
    mochila_decodificada = []
            
    for i in range(0, len(mochila)):
        if (mochila[i] == 1):
            mochila_decodificada.append(len(nomes)-23)
        else:
            mochila_decodificada.append(len(nomes)-24)

    valor_mochila = calcula_valor_mochila(mochila, valores)
    peso_mochila = calcula_peso_mochila(mochila, pesos)
    
    mochila_decodificada.append('                                                              ')
    mochila_decodificada.append('                                                              ')  
    mochila_decodificada.append('                                                              ')      
    mochila_decodificada.append('Peso total '  + str(valor_mochila))
    mochila_decodificada.append('Valor R$ ' + str(peso_mochila))
    
    return mochila_decodificada

def funcao_objetivo(valores_mochilas, pesos_mochilas, valor_max, peso_max):

    aptidoes = []
    
    for i in range(0, len(valores_mochilas)):
        if (pesos_mochilas[i] <= peso_max):
            auxiliar = pesos_mochilas[i]/peso_max
        else:
            auxiliar = - 2.0
        aptidao = valores_mochilas[i]/valor_max + auxiliar
        aptidoes.append(aptidao)
            
    return aptidoes

def gera_mochila_aleatoria(n_objetos):
        
    mochila_aleatoria = []
        
    for i in range(0, n_objetos):
        zero_ou_um = randint(0, 1)
        mochila_aleatoria.append(zero_ou_um)
        
    return mochila_aleatoria

def gera_populacao_inicial(tamanho_populacao, n_objetos):
    
    populacao_inicial = []
    
    for i in range(0, tamanho_populacao):
        mochila_aleatoria = gera_mochila_aleatoria(n_objetos)
        populacao_inicial.append(mochila_aleatoria)

    return populacao_inicial

def gera_ranking(aptidoes):

    ranking = []

    for i in range(0, len(aptidoes)):
        valor_max = max(aptidoes)
        indice = aptidoes.index(valor_max)
        ranking.append(indice)
        aptidoes[indice] = -1

    return ranking

def print_lista(lista):

    for i in lista:
        print(i)
      
def realiza_mutacao(populacao, mutantes, taxa_mutacao):
    
    quant_mutacoes = (len(populacao[0])*taxa_mutacao)//100
    
    for i in range(0, len(mutantes)):
        
        gene_index = []
        for j in range(0, len(populacao[0])):
            gene_index.append(j)
        
        cobaia = populacao[mutantes[i][0]]
        
        for k in range(0, quant_mutacoes):
            index_escolhido = choices(gene_index, k=1)
            
            if (cobaia[index_escolhido[0]] == 0):
                cobaia[index_escolhido[0]] = 1
            else:
                cobaia[index_escolhido[0]] = 0
                
            gene_index.remove(index_escolhido[0])
            
    return populacao 

def seleciona_mutantes(populacao, prob_mutacao):
        
    pop_index = []
    
    for i in range(0, len(populacao)):
        pop_index.append(i)
    
    mutantes = []
    quant_mutantes = (len(populacao)*prob_mutacao)//100
    
    for i in range(0, quant_mutantes):
        index_escolhido = choices(pop_index, k=1)
        mutantes.append(index_escolhido)
        pop_index.remove(mutantes[i][0])
        
    return mutantes

def seleciona_pais(ranking):

    p_max = 0.999    
    p_min = 0.001     
        
    pais_selecionados = []
    prob_selecao = []
    n_mochilas = len(ranking)
    
    for i in range(0, n_mochilas):
        prob = p_max / exp(ln(p_max/p_min) * i/(n_mochilas-1))
        prob_selecao.append(prob)
        
    for i in range(0, n_mochilas):        
        pais = choices(ranking, prob_selecao, k=2)        
        pais_selecionados.append(pais)

    return pais_selecionados

if __name__ == '__main__':

    objetos = [['1',382745, 825594], 
           ['2', 799601,1677009], 
           ['3', 909247,1676628], 
           ['4', 729069,1523970], 
           ['5', 467902,943972], 
           ['6', 44328,97426], 
           ['7', 34610,69666], 
           ['8', 698150,1296457], 
           ['9', 823460,1679693], 
           ['10', 903959,1902996], 
           ['11', 853665,1844992],
           ['12', 551830,1049289],
           ['13', 610856,1252836], 
           ['14', 670702,1319836], 
           ['15', 488960,953277], 
           ['16', 951111,2067538], 
           ['17', 323046,675367], 
           ['18', 446298,853655], 
           ['19', 931161,1826027], 
           ['20', 31385,65731], 
           ['21', 496951,901489], 
           ['22', 264724,577243], 
           ['23', 224916,466257],
           ['24', 169684,369261]]
    n_objetos = len(objetos)
    nomes, valores, pesos  = [], [], []

    for i in range(0, n_objetos):
        nomes.append(objetos[i][0])   
        valores.append(objetos[i][1]) 
        pesos.append(objetos[i][2])  

    valor_max = sum(valores)    
    peso_max = sum(pesos)    
    tamanho_populacao = 300
    peso_limite = 6404180    
    populacao = gera_populacao_inicial(tamanho_populacao, n_objetos)
    n_geracoes = 50    
    prob_mutacao = 15    
    taxa_mutacao = 5    

    for geracao in range(1, n_geracoes+1):
        t = 'Espaço de Busca - Geração ' + str(geracao)
        valores_mochilas = calcula_valores_populacao(populacao, valores)
        pesos_mochilas = calcula_pesos_populacao(populacao, pesos)
    

    for i in range(0, len(pesos_mochilas)):
        t = 'Função Objetivo - Geração ' + str(geracao)
        aptidoes = funcao_objetivo(valores_mochilas, pesos_mochilas, valor_max, peso_limite)
    
    for i in range(0, len(pesos_mochilas)):
        ranking = gera_ranking(aptidoes[:])
        pais = seleciona_pais(ranking)
        populacao = cruzamento(populacao, pais)
        mutantes = seleciona_mutantes(populacao, prob_mutacao)    
        populacao = realiza_mutacao(populacao, mutantes, taxa_mutacao)

        melhor_mochila = populacao[ranking[0]]
        mochila_decodificada = decodifica_mochila(melhor_mochila, nomes, valores, pesos)

    
    print_lista([mochila_decodificada])




    


# %%
