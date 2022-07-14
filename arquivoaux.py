# cabecalho pra n dar warnings
import numpy as np
import matplotlib.pyplot as plt

n = 54
x = np.zeros(n)
h = 3434
vetorAlfa = np.zeros(23)
# fim do cabecalho inutil

vetoruAproximado = 33
vetoruExato = 3

fig, ax = plt.subplots()
line1, = ax.plot(x, vetoruAproximado, label='Valor aproximado', marker = '.')
line2, = ax.plot(x, vetoruExato, label='Valor exato', marker = '.')
ax.set_title('Valores aproximados e exatos da primeira validacao')
ax.set_xlabel('Valor de x')
ax.set_ylabel('Valores obtidos')

fig, ax2 = plt.subplots()
line1, = ax2.plot(x, vetoruAproximado, label='Valor aproximado', marker = '.')
line2, = ax2.plot(x, vetoruExato, label='Valor exato', marker = '.')
    


ax.legend()
plt.show()

def calculaMEFpadrao(n, L, funcaoX, funcaoK, funcaoQ):
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
        diagB[i] = pow((1/h),2) * calculaIntegral(x[i], x[i+1], funcaoK) + pow((-1/h),2) * calculaIntegral(x[i+1], x[i+2], funcaoK) + pow((1/h),2) * calculaIntegral(x[i], x[i+1], "("+funcaoQ+")*pow((x-"+str(x[i])+"),2)") + pow((1/h),2) * calculaIntegral(x[i+1], x[i+2], "("+funcaoQ+")*pow(("+str(x[i+2])+"-x),2)")

    ##  Calculo da diagonal acima da diagonal principal.  ##
    for i in range (0, n-1):
        diagC[i] = -1 * pow((1/h),2) * calculaIntegral(x[i+1], x[i+2], funcaoK) + pow((1/h),2) * calculaIntegral(x[i+1],x[i+2], "("+funcaoQ+")*("+str(x[i+2])+"-x)*(x-"+str(x[i+1])+")")

    ##  Calculo da diagonal abaixo da diagonal principal.  ##
    for i in range (1, n):
        diagA[i] = -1 * pow((1/h),2) * calculaIntegral(x[i], x[i+1], funcaoK) + pow((1/h),2) * calculaIntegral(x[i],x[i+1], "("+funcaoQ+")*("+str(x[i+1])+"-x)*(x-"+str(x[i])+")")

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
