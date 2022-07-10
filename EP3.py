###     MAP3121 - Calculo Numerico - Escola Politecnica                  ###
###     Tarefa 3 - Modelagem de um Sistema de Resfriamento de Chips      ###

###     Alunos deste grupo:                                              ###       
###     Fabio Akira Yonamine   - NUSP 11805398                           ###
###     Pedro H. Teodoro Silva - NUSP 11805314                           ###

##  Importacao da biblioteca numpy, com abreviacao np.  ##
import numpy as np
##  Importacao da biblioteca 
import matplotlib.pyplot as plt

##  Funcao principal.  ##
def main():
    ##  Menu que fornece as opcoes disponiveis neste EP 3.  ##
    print("Veja as opcoes disponiveis... ")
    print("1. Secao 4.2 - Validacao")
    print("2. Secao 4.2 - Validacao complementar")
    print("3. ")
    print("4. ")
    menuChoice = int(input("Digite o numero da opcao desejada para calculos: "))

    ##  Uso do MEF para resolucao do primeiro problema de validacao disponibilizado.  ##
    if(menuChoice==1):
        print("\nItem 4.2 - Primeira validacao")

        ##  Vetor que guarda os quatro valores de erro maximo, para cada n.  ##
        vetorErroMaximo = np.zeros(4)

        ##  Dados do primeiro problema de validacao.  ##
        L = 1
        funcaoX = "12*x*(1-x)-2"
        funcaoK = "1"
        funcaoQ = "0"

        ##  Calculos para n = 7.  ##
        print("\nPara n = 7: ")
        vetoruAproximadoNSete = calculaMEF(7 , L , funcaoX , funcaoK , funcaoQ)
        vetoruExatoNSete = geraVetorValidacaoProblemaUm(7)
        vetorErroMaximoNSete = calculaErroMaximo(7, vetoruAproximadoNSete, vetoruExatoNSete)
        print("     Valores aproximados:\n", vetoruAproximadoNSete)
        print("     Valores exatos:\n", vetoruExatoNSete)
        print("     Erro maximo obtido: ", vetorErroMaximoNSete)

        ##  Calculos para n = 15.  ##
        print("\nPara n = 15: ")
        vetoruAproximadoNQuinze = calculaMEF(15 , L , funcaoX , funcaoK , funcaoQ)
        vetoruExatoNQuinze = geraVetorValidacaoProblemaUm(15)
        vetorErroMaximoNQuinze = calculaErroMaximo(15, vetoruAproximadoNQuinze, vetoruExatoNQuinze)
        print("     Valores aproximados:\n", vetoruAproximadoNQuinze)
        print("     Valores exatos:\n", vetoruExatoNQuinze)
        print("     Erro maximo obtido: ", vetorErroMaximoNQuinze)


    elif(menuChoice==2):
        print(1)

    #for i in range(0,4):
    ##  Chama as funcoes para calcular valores esperados e exatos, assim como o erro maximo.  ##
    #    print("\nPara n = ",n[i],"...")
    #    vetoruAproximado = calculaMEF(n[i] , L , funcaoX , k , q)
    #    vetoruExato = geraVetorValidacaoProblemaUm(n[i])
    #    vetorErroMaximo[i] = calculaErroMaximo(n[i], vetoruAproximado, vetoruExato)
    #    print("     Valores aproximados:\n", vetoruAproximado)
    #    print("     Valores exatos:\n", vetoruExato)
    #    print("     Erro maximo obtido: ", vetorErroMaximo[i])
    #
    #print("\n     Em suma, para o primeiro problema de validacao, foram obtidos\n     os seguintes erros maximos, reapresentados aqui juntos:\n")
    #for i in range(0,4):
    #    print("     Erro maximo ( n =",n[i],"): ",vetorErroMaximo[i])

    #h = L/(63+1)
    #x = np.zeros(63+2)
    #for i in range(0, 63+2):
    #    x[i] = i*h
    
    #fig, ax = plt.subplots(2,2)
    #ax[1,1].plot(x, vetoruAproximado, label='Valor aproximado', marker = '.')
    #ax[1,1].plot(x, vetoruExato, label='Valor exato', marker = '.')
    #ax.set_title('Valores aproximados e exatos da primeira validacao')
    #ax.set_xlabel('Valor de x')
    #ax.set_ylabel('Valores obtidos')

    #fig, ax2 = plt.subplots()
    #line1, = ax2.plot(x, vetoruAproximado, label='Valor aproximado', marker = '.')
    #line2, = ax2.plot(x, vetoruExato, label='Valor exato', marker = '.')
    


    #ax[1,1].legend()
    #plt.show()

    ########################################################################################

    ##  Uso do MEF para resolucao do segundo problema de validacao disponibilizado.  ##
    print("\nItem 4.2 - Segunda validacao")

    ##  Dados do segundo problema de validacao.  ##
    L = 1
    funcaoX = "np.exp(x)+1"
    k = "np.exp(x)"
    q = "0"

    #print(calculaMEF(n, L, funcao, "1", 0))

    #print("resultado do PDF adicional:\n", calculaMEF(n, L,"np.exp(x)+1", "np.exp(x)", 0))
    #print("resutado exato:\n", geraVetorValidacaoProblemaDois(n,x))

def calculaErroMaximo(n, vetoruAproximado, vetoruExato):
    erroMaximo = 0
    for i in range (0,n):
        diferencaModulo = abs(vetoruAproximado[i] - vetoruExato[i])
        if(diferencaModulo > erroMaximo):
            erroMaximo = diferencaModulo
    return erroMaximo

def calculaMEF(n, L, funcaoX, funcaoK, funcaoQ):
    ##  Cálculo do intervalo entre pontos.  ##
    h = L/(n+1)
    print("     Intervalo entre pontos: "+str(h))

    ##  Criacao do vetor com valores x_i.  ##
    x = np.zeros(n+2)
    for i in range(0, n+2):
        x[i] = i*h
    print("     Valores do vetor x:")
    print(x)

    ##  Criacao da matriz A (tridiagonal) da equacao (8), representada em três vetores.  ##
    diagA = np.zeros(n)
    diagB = np.zeros(n)
    diagC = np.zeros(n)

    ##  Calculo da diagonal principal.  ##
    for i in range (0, n):
        diagB[i] = pow((1/h),2) * calculaIntegral(x[i], x[i+1], funcaoK) + pow((-1/h),2) * calculaIntegral(x[i+1], x[i+2], funcaoK)

    ##  Calculo da diagonal acima da diagonal principal.  ##
    for i in range (0, n-1):
        diagC[i] = -1 * pow((1/h),2) * calculaIntegral(x[i+1], x[i+2], funcaoK)

    ##  Calculo da diagonal abaixo da diagonal principal.  ##
    for i in range (1, n):
        diagA[i] = -1 * pow((1/h),2) * calculaIntegral(x[i], x[i+1], funcaoK)

    ##  Imprime as três diagonais criadas acima.  ##
    print("     Vetor a da matriz A:")
    print(diagA)
    print("     Vetor b da matriz A:")
    print(diagB)
    print("     Vetor c da matriz A:")
    print(diagC)

    ##  Calculo do vetor b, da funcao chapeu da equacao (8).  ##
    b = np.zeros(n)
    for i in range(0, n):
        b[i] = calculaIntegral(x[i],x[i+1],"("+funcaoX+")*(x-"+str(x[i])+")/"+str(h)) + calculaIntegral(x[i+1],x[i+2],"("+funcaoX+")*("+str(x[i+2])+"-x)/"+str(h))

    ##  Imprime o vetor b, calculado acima.  ##
    print("     Vetor b do sistema: ")
    print(b)

    ##  Resolve sistema matricial para achar o vetor alfa.  ##
    vetorAlfa = resolveTridiagonal(n,diagA,diagB,diagC,b)

    ##  Imprime o vetor alfa calculado acima.  ##
    print("     Vetor alfa, resolvido:")
    print(vetorAlfa)

    ##  Finalmente, calculo do valor aproximado.  ##
    #vetoruExato      = np.zeros(n+2)
    vetoruAproximado = np.zeros(n+2)

    for j in range(0,n+2):
        rAproximado = 0
        for i in range(0, n):
            if (x[j] <= x[i+1] and x[j] >= x[i]):
                rAproximado = rAproximado + vetorAlfa[i] * (x[j] - x[i]) / h
            elif (x[j] <= x[i+2] and x[j] >= x[i+1]):
                rAproximado = rAproximado + vetorAlfa[i] * (x[i+2] - x[j]) / h
        vetoruAproximado[j] = rAproximado
        #vetoruExato[j] =  pow(x[j],2) * pow((1 - x[j]),2)

    ##  Retorna vetor com os valores aproximados, nos pontos x_i.  ##
    return vetoruAproximado

##  Funcao que gera o vetor de validacao do item 4.2.  ##
def geraVetorValidacaoProblemaUm(n):
    ##  Criacao do vetor com valores x_i.  ##
    x = np.zeros(n+2)

    ##  Cálculo do intervalo entre pontos.  ##
    h = 1/(n+1)

    for i in range(0, n+2):
        x[i] = i*h

    valoresExatos = np.zeros(n+2)

    for i in range (1,n+2):
        valoresExatos[i] = pow(x[i],2) * pow(1 - x[i],2)
    return valoresExatos

##  Funcao que gera o vetor de validacao do complemento do item 4.2.  ##
def geraVetorValidacaoProblemaDois(n):
    valoresExatos = np.zeros(n+2)
    
    for i in range (0,n+2):
        valoresExatos[i] = (x[i] - 1) * (np.exp(-1 * x[i]) - 1)
    return valoresExatos

##  Funcao que calcula integral simples em dx, com n = 2.        ##
##  Observacao: funcao derivada das presentes no EP2,            ##
##  porem alterada para calcular integrais simples em            ##
##  dx, com n = 2 somente.                                       ##
def calculaIntegral(a,b,funcao):
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
