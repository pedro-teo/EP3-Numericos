###     MAP3121 - Calculo Numerico - Escola Politecnica                  ###
###     Tarefa 3 - Modelagem de um Sistema de Resfriamento de Chips      ###

###     Alunos deste grupo:                                              ###       
###     Fabio Akira Yonamine   - NUSP 11805398                           ###
###     Pedro H. Teodoro Silva - NUSP 11805314                           ###

##  Importacao da biblioteca numpy, com abreviacao np.  ##
import numpy as np

##  Funcao principal.  ##
def main():
    ##  Escolha do n desejado para os calculos subsequentes.  ##
    #n = int(input("Digite o n para as analises: "))
    #L = int(input("Digite o L para as analises: ")) ## L = 1 para comecar
    n = 7
    L = 1
    funcao = "12*x*(1-x)-2"

    ##  Cálculo do intervalo entre pontos.  ##
    h = L/(n+1)
    print("\nIntervalo entre pontos: "+str(h))

    ##  Criacao do vetor com valores x_i.  ##
    x = np.zeros(n+2)
    for i in range(0, n+2):
        x[i] = i*h
    print("Valores do vetor x:")
    print(x)

    ## Criacao da matriz A da equacao (8)
    diagA = np.zeros(n)
    diagB = np.zeros(n)
    diagC = np.zeros(n)

    diagA[0] = 0
    diagB[0] = 2/h
    diagC[0] = -1/h

    diagA[n-1] = -1/h
    diagB[n-1] = 2/h
    diagC[n-1] = 0

    for i in range(1, n-1):
        diagA[i] = -1/h
        diagB[i] =  2/h
        diagC[i] = -1/h

    print(diagA)
    print(diagB)
    print(diagC)

    ## Calculo do vetor da funcao chapeu da equacao (8)
    b = np.zeros(n)
    for i in range(0, n): # COMECA EM ZERO E VAI ATE N-1
        b[i] = calculaIntegralNDois(x[i],x[i+1],"("+funcao+")*(x-"+str(x[i])+")/"+str(h)) + calculaIntegralNDois(x[i+1],x[i+2],"("+funcao+")*("+str(x[i+2])+"-x)/"+str(h))

    print("Vetor b: ")
    print(b)

    ##  Resolve sistema matricial para achar o vetor alfa.  ##
    vetorAlfa = resolveTridiagonal(n,diagA,diagB,diagC,b)
    print("vetor alfa resolvido: ")
    print(vetorAlfa)

    ##  Finalmente, calculo do valor aproximado.  ##

    ##### vDesejado eh um numero qualquer q eu desejo calcular, q eu escolhi 0.3 aqui
    vDesejado = 0.3
    rAproximado = 0
    for i in range(0, n):
        if (vDesejado <= x[i+1] and vDesejado >= x[i]):
            rAproximado = rAproximado + vetorAlfa[i] * (vDesejado - x[i]) / h
        elif (vDesejado <= x[i+2] and vDesejado >= x[i+1]):
            rAproximado = rAproximado + vetorAlfa[i] * (x[i+2] - vDesejado) / h

    print("Valor aproximado: ")
    print(rAproximado)
    print("Valor exato: ")
    print( pow(vDesejado,2) * pow((1 - vDesejado),2))

    #print("Para u = 1, valor esperado: "+str((0.5)^2+(0.5)^2))
    #print(funcaoTeste(5,0,1,x))
    print(geraVetorValidacao(n,x))

    print(vetorAlfa - geraVetorValidacao(n,x))
        

##  Funcao que gera o vetor de validacao do item 4.2.  ##
def geraVetorValidacao(n,x):
    valoresExatos = np.zeros(n)

    for i in range (1,n+1):
        valoresExatos[i-1] = pow(x[i],2) * pow(1 - x[i],2)
    return valoresExatos

def geraVetorValidacaoProblemaDois(n,x):
    valoresExatos = np.zeros(n)
    
    for i in range (0,n):
        valoresExatos[i] = pow(x[i],2) + pow(1 - x[i],2)
    return valoresExatos

##  Funcao que calcula integral simples em dx (n = 10).          ##
##  Observacao: funcao NOVA, mas derivada do EP2.                ##
def calculaIntegral(a,b,funcao):
    ## Cria matriz com valores de pesos e nos para n = 10
    n10 = np.zeros((10,2))
    n10 = [[-0.9739065285171717200779640,0.0666713443086881375935688],[-0.8650633666889845107320967,0.1494513491505805931457763],[-0.6794095682990244062343274,0.2190863625159820439955349],[-0.4333953941292471907992659,0.2692667193099963550912269],[-0.1488743389816312108848260,0.2955242247147528701738930],[0.1488743389816312108848260,0.2955242247147528701738930],[0.4333953941292471907992659,0.2692667193099963550912269],[0.6794095682990244062343274,0.2190863625159820439955349],[0.8650633666889845107320967,0.1494513491505805931457763],[0.9739065285171717200779640,0.0666713443086881375935688]]
    
    ##  Inicializa a variavel que guardara o valor final da integral dupla desejada em zero.  ##
    resultado = 0

    ##  Funcao generica que define X, dada a transformação para S, para   ##
    ##  que os limites de integracao da integral sejam -1 e 1, de modo a  ##
    ##  usar os nos e pesos pre-fornecidos no enunciado.                  ##                                                  ##                               
    funcaoX = "((b-a)*s + a + b)/2"

    for i in range (0,10):
        s = n10[i][0]
        x = eval(funcaoX)
        resultado = resultado + n10[i][1] * eval(funcao)
    resultado = resultado * (b-a) / 2

    ##  Retorna o resultado para a chamada de funcao.  ##
    return resultado

##  Funcao que calcula integral simples em dx, com n = 2.        ##
##  Observacao: funcao derivada das presentes no EP2,            ##
##  porem alterada para calcular integrais simples em            ##
##  dx, com n = 2 somente.                                       ##
def calculaIntegralNDois(a,b,funcao):
    ## Cria matriz com valores de pesos e nos para n = 2
    n2 = np.zeros((2,2))
    n2 = [[-1/np.sqrt(3),1],[1/np.sqrt(3),1]]

    ##  Inicializa a variavel que guardara o valor final da integral dupla desejada em zero.  ##
    resultado = 0

    ##  Funcao generica que define X, dada a transformação para S, para   ##
    ##  que os limites de integracao da integral sejam -1 e 1, de modo a  ##
    ##  usar os nos e pesos pre-fornecidos no enunciado.                  ##                                                  ##                               
    funcaoX = "((b-a)*s + a + b)/2"

    for i in range (0,2):
        s = n2[i][0]
        x = eval(funcaoX)
        resultado = resultado + n2[i][1] * eval(funcao)
    resultado = resultado * (b-a) / 2

    ##  Retorna o resultado para a chamada de funcao.  ##
    return resultado    

##  Funcao que resolve uma matriz tridiagonal usando vetores com otimizacao.  ##
##  Observacao: funcao reproduzida integralmente do EP1 entregue.             ##
##  Observacao: esta funcao necessita da funcao decomposicaoLU, abaixo.       ##
def resolveTridiagonal(n, diagA, diagB, diagC, d):
    ## Geracao dos vetores L e U do sistema ##
    vetU = np.zeros(n)
    vetL = np.zeros(n)
    decomposicaoLU(n, diagA, diagB, diagC, vetU, vetL)

    ## Criacao dos vetores x e y ##
    vetX = np.zeros(n)
    vetY = np.zeros(n)

    ## Obtencao dos valores de y ##
    vetY[0] = d[0]
    for i in range(1, n):
        vetY[i] = d[i] - vetL[i]*vetY[i-1]

    ## Obtencao dos valores de x ##
    vetX[n-1] = vetY[n-1]/vetU[n-1]
    for i in range(n-2, -1, -1):
        vetX[i] = (vetY[i] - (diagC[i]*vetX[i+1]))/vetU[i]
    
    ## Retorna o vetor x ##
    return vetX

##  Funcao que retorna os vetores L e U de matrizes tridiagonais.  ##
##  Observacao: funcao reproduzida integralmente do EP1 entregue.  ##
def decomposicaoLU(n, diagA, diagB, diagC,vetU,vetL):
    vetU[0] = diagB[0]
    for i in range (1,n):
        vetL[i] = (diagA[i])/vetU[i-1]
        vetU[i] = diagB[i] - vetL[i]*diagC[i-1]

##  Comanda o programa a voltar para a funcao main.  ##
if __name__ == '__main__':
    main()
