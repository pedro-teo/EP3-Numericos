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
    print("3. Secao 4.3 - Q(x) constante")
    print("4. Secao 4.3 - Q(x) com funcao em x")
    print("5. Secao 4.4 - Equilibrio com variacao de material")
    menuChoice = int(input("Digite o numero da opcao desejada para calculos: "))

    ##  Resolucao do item 4.2, da primeira validacao disponibilizada.  ##
    if(menuChoice==1):
        print("\nItem 4.2 - Primeira validacao")

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

        ##  Calculos para n = 31.  ##
        print("\nPara n = 31: ")
        vetoruAproximadoNTrinta = calculaMEF(31 , L , funcaoX , funcaoK , funcaoQ)
        vetoruExatoNTrinta = geraVetorValidacaoProblemaUm(31)
        vetorErroMaximoNTrinta = calculaErroMaximo(31, vetoruAproximadoNTrinta, vetoruExatoNTrinta)
        print("     Valores aproximados:\n", vetoruAproximadoNTrinta)
        print("     Valores exatos:\n", vetoruExatoNTrinta)
        print("     Erro maximo obtido: ", vetorErroMaximoNTrinta)

        ##  Calculos para n = 63.  ##
        print("\nPara n = 63: ")
        vetoruAproximadoNSessenta = calculaMEF(63 , L , funcaoX , funcaoK , funcaoQ)
        vetoruExatoNSessenta = geraVetorValidacaoProblemaUm(63)
        vetorErroMaximoNSessenta = calculaErroMaximo(63, vetoruAproximadoNSessenta, vetoruExatoNSessenta)
        print("     Valores aproximados:\n", vetoruAproximadoNSessenta)
        print("     Valores exatos:\n", vetoruExatoNSessenta)
        print("     Erro maximo obtido: ", vetorErroMaximoNSessenta)

        ##  Imprime os erros maximos obtidos de cada n, para fins de estudo com o h^2.  ##
        print("\n     Em suma, para o primeiro problema de validacao, foram obtidos\n     os seguintes erros maximos, reapresentados aqui juntos:\n")
        print("     Erro maximo  (n=7): ",vetorErroMaximoNSete)
        print("     Erro maximo (n=15): ",vetorErroMaximoNQuinze)
        print("     Erro maximo (n=31): ",vetorErroMaximoNTrinta)
        print("     Erro maximo (n=63): ",vetorErroMaximoNSessenta)
        print("\nO sistema agora abrira um grafico, contendo as curvas obtidas.")
        print("Caso deseje executar outra opcao, feche o grafico primeiro e,\ndepois, rode o codigo novamente.\n")
        ##  Plot do grafico das 4 series obtidas anteriormente neste exercicio.  ##
        x1 = np.linspace(0.0, 1.0, num=9)
        x2 = np.linspace(0.0, 1.0, num=17)
        x3 = np.linspace(0.0, 1.0, num=33)
        x4 = np.linspace(0.0, 1.0, num=65)

        fig, ax = plt.subplots(2,2)
        ax[0,0].plot(x1, vetoruAproximadoNSete, label='Valor aproximado', marker = '.')
        ax[0,0].plot(x1, vetoruExatoNSete, label='Valor exato', marker = '.', linestyle='--')
        ax[0,1].plot(x2, vetoruAproximadoNQuinze, label='Valor aproximado', marker = '.')
        ax[0,1].plot(x2, vetoruExatoNQuinze, label='Valor exato', marker = '.', linestyle='--')
        ax[1,0].plot(x3, vetoruAproximadoNTrinta, label='Valor aproximado', marker = '.')
        ax[1,0].plot(x3, vetoruExatoNTrinta, label='Valor exato', marker = '.', linestyle='--')
        ax[1,1].plot(x4, vetoruAproximadoNSessenta, label='Valor aproximado', marker = '.')
        ax[1,1].plot(x4, vetoruExatoNSessenta, label='Valor exato', marker = '.', linestyle='--')
        ax[0,0].set_title('n = 7')
        ax[0,1].set_title('n = 15')
        ax[1,0].set_title('n = 31')
        ax[1,1].set_title('n = 63')

        ax[1,1].legend()
        fig.tight_layout()
        plt.show()

    ##  Resolucao do item 4.2, da segunda validacao disponibilizada.  ##
    elif(menuChoice==2):
        print("\nItem 4.2 - Segunda validacao")

        ##  Dados do segundo problema de validacao.  ##
        L = 1
        funcaoX = "np.exp(x)+1"
        funcaoK = "np.exp(x)"
        funcaoQ = "0"
        
        ##  Calculos para n = 7.  ##
        print("\nPara n = 7: ")
        vetoruAproximadoNSete = calculaMEF(7 , L , funcaoX , funcaoK , funcaoQ)
        vetoruExatoNSete = geraVetorValidacaoProblemaDois(7)
        vetorErroMaximoNSete = calculaErroMaximo(7, vetoruAproximadoNSete, vetoruExatoNSete)
        print("     Valores aproximados:\n", vetoruAproximadoNSete)
        print("     Valores exatos:\n", vetoruExatoNSete)
        print("     Erro maximo obtido: ", vetorErroMaximoNSete)

        ##  Calculos para n = 15.  ##
        print("\nPara n = 15: ")
        vetoruAproximadoNQuinze = calculaMEF(15 , L , funcaoX , funcaoK , funcaoQ)
        vetoruExatoNQuinze = geraVetorValidacaoProblemaDois(15)
        vetorErroMaximoNQuinze = calculaErroMaximo(15, vetoruAproximadoNQuinze, vetoruExatoNQuinze)
        print("     Valores aproximados:\n", vetoruAproximadoNQuinze)
        print("     Valores exatos:\n", vetoruExatoNQuinze)
        print("     Erro maximo obtido: ", vetorErroMaximoNQuinze)

        ##  Calculos para n = 31.  ##
        print("\nPara n = 31: ")
        vetoruAproximadoNTrinta = calculaMEF(31 , L , funcaoX , funcaoK , funcaoQ)
        vetoruExatoNTrinta = geraVetorValidacaoProblemaDois(31)
        vetorErroMaximoNTrinta = calculaErroMaximo(31, vetoruAproximadoNTrinta, vetoruExatoNTrinta)
        print("     Valores aproximados:\n", vetoruAproximadoNTrinta)
        print("     Valores exatos:\n", vetoruExatoNTrinta)
        print("     Erro maximo obtido: ", vetorErroMaximoNTrinta)

        ##  Calculos para n = 63.  ##
        print("\nPara n = 63: ")
        vetoruAproximadoNSessenta = calculaMEF(63 , L , funcaoX , funcaoK , funcaoQ)
        vetoruExatoNSessenta = geraVetorValidacaoProblemaDois(63)
        vetorErroMaximoNSessenta = calculaErroMaximo(63, vetoruAproximadoNSessenta, vetoruExatoNSessenta)
        print("     Valores aproximados:\n", vetoruAproximadoNSessenta)
        print("     Valores exatos:\n", vetoruExatoNSessenta)
        print("     Erro maximo obtido: ", vetorErroMaximoNSessenta)

        ##  Imprime os erros maximos obtidos de cada n, para fins de estudo com o h^2.  ##
        print("\n     Em suma, para o segundo problema de validacao, foram obtidos\n     os seguintes erros maximos, reapresentados aqui juntos:\n")
        print("     Erro maximo  (n=7): ",vetorErroMaximoNSete)
        print("     Erro maximo (n=15): ",vetorErroMaximoNQuinze)
        print("     Erro maximo (n=31): ",vetorErroMaximoNTrinta)
        print("     Erro maximo (n=63): ",vetorErroMaximoNSessenta)
        print("\nO sistema agora abrira um grafico, contendo as curvas obtidas.")
        print("Caso deseje executar outra opcao, feche o grafico primeiro e,\ndepois, rode o codigo novamente.\n")

        ##  Plot do grafico das 4 series obtidas anteriormente neste exercicio.  ##
        x1 = np.linspace(0.0, 1.0, num=9)
        x2 = np.linspace(0.0, 1.0, num=17)
        x3 = np.linspace(0.0, 1.0, num=33)
        x4 = np.linspace(0.0, 1.0, num=65)

        fig, ax = plt.subplots(2,2)
        ax[0,0].plot(x1, vetoruAproximadoNSete, label='Valor aproximado', marker = '.')
        ax[0,0].plot(x1, vetoruExatoNSete, label='Valor exato', marker = '.', linestyle='--')
        ax[0,1].plot(x2, vetoruAproximadoNQuinze, label='Valor aproximado', marker = '.')
        ax[0,1].plot(x2, vetoruExatoNQuinze, label='Valor exato', marker = '.', linestyle='--')
        ax[1,0].plot(x3, vetoruAproximadoNTrinta, label='Valor aproximado', marker = '.')
        ax[1,0].plot(x3, vetoruExatoNTrinta, label='Valor exato', marker = '.', linestyle='--')
        ax[1,1].plot(x4, vetoruAproximadoNSessenta, label='Valor aproximado', marker = '.')
        ax[1,1].plot(x4, vetoruExatoNSessenta, label='Valor exato', marker = '.', linestyle='--')
        ax[0,0].set_title('n = 7')
        ax[0,1].set_title('n = 15')
        ax[1,0].set_title('n = 31')
        ax[1,1].set_title('n = 63')

        ax[1,1].legend()
        fig.tight_layout()
        plt.show()
    
    ##  Resolucao do item 4.3, de equilibrio com forcantes de calor.  ##
    elif(menuChoice==3):
        ##  Primeiro caso considerado:                             ##
        ##  * Utilizou-se a funcao de Q+0 descrita no PDF, com     ## 
        ##    Q+0 = 30W / (20*20*2 mm3).                           ##
        ##  * Para Q-0, considerou-se que a perda de calor ocorre  ##
        ##    de forma semelhante, com Q-0 = 20W / (20*20*2 mm3)   ##
        ##    (ou seja, um resfriamento menor que aquecimento).    ##
        n = 63
        L = 1
        funcaoQMais  = "30/(8*pow(10,-7))"
        funcaoQMenos = "20/(8*pow(10,-7))"
        funcaoK = "3.6"
        funcaoQ = funcaoQMais+"-("+funcaoQMenos+")"
        funcaoX = funcaoQ
        resultadoUm = calculaMEF(n, L, funcaoX, funcaoK, funcaoQ)

        h = L/(n+1)
        x = np.zeros(n+2)
        for i in range(0, n+2):
            x[i] = i*h
        
        vetorNovoUm = np.zeros(n+2)
        for i in range(0, n+2):
            vetorNovoUm[i] = resultadoUm[i] - eval(funcaoQ)*293.15

        ##  Segundo caso considerado:                              ##
        ##  * Utilizou-se a funcao de Q+(x) descrita no PDF, com   ## 
        ##    Q+0 = 30W / (20*20*2 mm3) e Sigma = 0.08.            ##
        ##  * Considerou-se Q- = 0, para analisar o efeito da      ##
        ##    variacao de Sigma na curva obtida.                   ##
        n = 63
        L = 1
        funcaoQMais  = "(30/(8*pow(10,3))) * np.exp(-pow((x-0.5),2)/pow(0.9,2))"
        funcaoQMenos = "0"
        funcaoK = "3.6"
        funcaoQ = funcaoQMais+"-("+funcaoQMenos+")"
        funcaoX = funcaoQ
        resultadoDois = calculaMEF(n, L, funcaoX, funcaoK, funcaoQ)

        ##  Terceiro caso considerado:                             ##
        ##  * Utilizou-se a funcao de Q+(x) descrita no PDF, com   ## 
        ##    Q+0 = 30W / (20*20*2 mm3) e Sigma = 0.015.            ##
        ##  * Considerou-se Q- = 0, para analisar o efeito da      ##
        ##    variacao de Sigma na curva obtida.                   ##
        n = 63
        L = 1
        funcaoQMais  = "(30/(8*pow(10,3))) * np.exp(-pow((x-0.5),2)/pow(1,2))"
        funcaoQMenos = "0"
        funcaoK = "3.6"
        funcaoQ = funcaoQMais+"-("+funcaoQMenos+")"
        funcaoX = funcaoQ
        resultadoTres = calculaMEF(n, L, funcaoX, funcaoK, funcaoQ)
        
        ##  Quarto caso considerado:                               ##
        ##  * Utilizou-se a funcao de Q+(x) descrita no PDF, com   ## 
        ##    Q+0 = 30W / (20*20*2 mm3) e Sigma = 0.08.            ##
        ##  * Utilizou-se a funcao de Q-(x), descrita no PDF, com  ##
        ##    Q-0 = 30W / (20*20*2 mm3)                ##
        ##    (ou seja, um resfriamento menor que aquecimento).    ##
        n = 63
        L = 1
        funcaoQMais  = "(30/(8*pow(10,3)))"
        funcaoQMenos = "(20/(8*pow(10,3))) * ( np.exp(-pow((x/0.003),2)) + np.exp(-pow((x-1)/0.003,2)) )"
        funcaoK = "3.6"
        funcaoQ = funcaoQMais+"-("+funcaoQMenos+")"
        funcaoX = funcaoQ
        resultadoQuatro = calculaMEF(n, L, funcaoX, funcaoK, funcaoQ)

        ## CURVA 5 Q PARECE ESTAR CERTA
        n = 63
        L = 1
        funcaoQMais  = "(30/(8*pow(10,-7))) * np.exp(-pow((x-0.5),2)/pow(0.2,2))"
        funcaoQMenos = "(30/(8*pow(10,-7))) * ( np.exp(-pow((x/0.4),2)) + np.exp(-pow((x-1)/0.4,2)) )"
        funcaoK = "3.6"
        funcaoQ = funcaoQMais+"-("+funcaoQMenos+")"
        funcaoX = funcaoQ
        resultadoCinco = calculaMEF(n, L, funcaoX, funcaoK, funcaoQ)

        h = L/(n+1)
        vetorX = np.zeros(n+2)
        for i in range(0, n+2):
            vetorX[i] = i*h
        
        vetorNovoCinco = np.zeros(n+2)
        for i in range(0, n+2):
            x = vetorX[i]
            vetorNovoCinco[i] = resultadoCinco[i] - eval(funcaoQ)*293.15

        
        ## CURVA do amigo do Teodoro
        n = 7
        L = 1
        #funcaoQMais  = "100"
        #funcaoQMenos = "0"
        funcaoK = "3.6"
        funcaoQ = "0"
        #funcaoX = funcaoQMais+"-("+funcaoQMenos+")"
        funcaoX = "100*np.exp(-pow(x-(1/2),2)/pow(10,2)) - 50*(np.exp(-(np.power(x,2)/np.power(5,2))) + np.exp(-(np.power(x-1,2)/np.power(5,2))) )"
        #funcaoY = - 50(np.exp(-(np.power(x,2)/np.power(5,2))) + np.exp(-(np.power(x-1,2)/np.power(5,2))))
        resultadoSeis = calculaMEF(n, L, funcaoX, funcaoK, funcaoQ)

        ## CURVA da Namie
        n = 60
        L = 1
        funcaoQMais  = "0"
        funcaoQMenos = "100"
        funcaoK = "3.6"
        funcaoQ = "0"
        funcaoX = funcaoQMais+"-("+funcaoQMenos+")"
        #funcaoY = - 50(np.exp(-(np.power(x,2)/np.power(5,2))) + np.exp(-(np.power(x-1,2)/np.power(5,2))))
        resultadoNamie = calculaMEF(n, L, funcaoX, funcaoK, funcaoQ)


        xNamie = np.linspace(0.0, 1.0, num=62)
        x4 = np.linspace(0.0, 1.0, num=65)
        x1 = np.linspace(0.0, 1.0, num=9)
        fig, ax = plt.subplots()
        #line1, = ax.plot(x4, resultadoUm, label='Caso 1', marker = '.')
        #line2, = ax.plot(x4, resultadoDois, label='Caso 2', marker = '.')
        #line3, = ax.plot(x4, resultadoTres, label='Caso 3', marker = '.')
        #line4, = ax.plot(x4, resultadoQuatro, label='Caso 4', marker='.')
        #line5, = ax.plot(x4, resultadoCinco, label='Caso 5', marker='.')
        
        #line6, = ax.plot(x4, resultadoSeis, label='Socorro Namie', marker = '.')
        #line6, = ax.plot(x1, resultadoSeis, label='Socorro Namie', marker = '.')
        line6, = ax.plot(xNamie, resultadoNamie, label='Socorro Namie', marker = '.')


        ax.set_title('Análise do efeito da variação de Q(x)')
        ax.set_xlabel('Posicao')
        ax.set_ylabel('Valor obtido')

        #fig, ax2 = plt.subplots()
        #line1, = ax2.plot(x, vetoruAproximado, label='Valor aproximado', marker = '.')
        #line2, = ax2.plot(x, vetoruExato, label='Valor exato', marker = '.')

        ax.legend()
        plt.show()

    ##  Resolucao do item 4.4, de equilibrio com variacao de material.  ##
    elif(menuChoice==4):
        ##  Note:                                                  ##
        ##  * Para comportar a variacao do material, refletida     ##
        ##    no uso de ks e ka, foi confeccionada uma segunda     ##
        ##    funcao de calculo de MEF, com entradas extras:       ##
        ##    ks, ka e d.                                          ##
        ##  * Utilizou-se a funcao de Q+(x) descrita no PDF, com   ## 
        ##    Q+0 = 30W / (20*20*2 mm3)                            ##
        ##  * Utilizou-se a funcao de Q-(x) descrita no PDF, com   ## 
        ##    Q+0 = 30W / (20*20*2 mm3)                            ##

        ##  Dados do problema.  ##
        n = 63
        L = 1
        d = 0.3
        funcaoQMais  = "(30/(8*pow(10,-7))) * np.exp(-pow((x-0.5),2)/pow(0.08,2))"
        funcaoQMenos = "(20/(8*pow(10,-7))) * ( np.exp(-pow((x/0.8),2)) + np.exp(-pow((x-1)/0.8,2)) )"
        funcaoKa = "60*pow(10,3)"
        funcaoKs = "3.6*pow(10,3)"
        funcaoQ = funcaoQMais+"-("+funcaoQMenos+")"
        print(funcaoQ)
        funcaoX = funcaoQ

        resultado = calculaMEFteste(n, L, d, funcaoX, funcaoKs, funcaoKa, funcaoQ)

        ##  Plot do grafico das 4 series obtidas anteriormente neste exercicio.  ##
        x4 = np.linspace(0.0, 1.0, num=65)

        fig, ax = plt.subplots()
        line1, = ax.plot(x4, resultado, label='Valor aproximado', marker = '.')
        ax.set_title('Valores ex3')
        ax.set_xlabel('Valor de x')
        ax.set_ylabel('Valores obtidos')

        ax.legend()
        plt.show()

    elif(menuChoice==5):
        ##  Dados do problema.  ##
        n = 63
        L = 1
        d = 0.3
        funcaoQ = "(30/(8*pow(10,-7))) * np.exp(-pow((x-0.5),2)/pow(0.08,2))"
        funcaoKa = "60"
        funcaoKs = "3.6"
        funcaoX = funcaoQ

        resultado = calculaMEFteste(n, L, d, funcaoX, funcaoKs, funcaoKa, funcaoQ)

        ##  Plot do grafico das 4 series obtidas anteriormente neste exercicio.  ##
        x4 = np.linspace(0.0, 1.0, num=65)

        fig, ax = plt.subplots()
        line1, = ax.plot(x4, resultado, label='Valor aproximado', marker = '.')
        ax.set_title('Valores ex3')
        ax.set_xlabel('Valor de x')
        ax.set_ylabel('Valores obtidos')

        ax.legend()
        plt.show()

    ##  Mensagem de erro, para opcao escolhida invalida.  ##
    else:
        print("\nNenhuma opcao valida foi selecionada. Rode novamente o codigo!\n")

def calculaErroMaximo(n, vetoruAproximado, vetoruExato):
    erroMaximo = 0
    for i in range (0,n):
        diferencaModulo = abs(vetoruAproximado[i] - vetoruExato[i])
        if(diferencaModulo > erroMaximo):
            erroMaximo = diferencaModulo
    return erroMaximo

def calculaMEFteste(n, L, d, funcaoX, funcaoKs, funcaoKa, funcaoQ): #antes era so funcaoK, e n tinha d
    ##  Calculo do limite entre materiais.  ##
    limInferior = (L/2) - d
    limSuperior = (L/2) + d 
    
    ##  Calculo do intervalo entre pontos.  ##
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
        if(x[i+1] > limInferior and x[i+1] < limSuperior):
            funcaoK = funcaoKs
        else:
            funcaoK = funcaoKa
        diagB[i] = pow((1/h),2) * calculaIntegral(x[i], x[i+1], funcaoK) + pow((-1/h),2) * calculaIntegral(x[i+1], x[i+2], funcaoK) + pow((1/h),2) * calculaIntegral(x[i], x[i+1], "("+funcaoQ+")*pow((x-"+str(x[i])+"),2)") + pow((1/h),2) * calculaIntegral(x[i+1], x[i+2], "("+funcaoQ+")*pow(("+str(x[i+2])+"-x),2)")

    ##  Calculo da diagonal acima da diagonal principal.  ##
    for i in range (0, n-1):
        if(x[i+1] > limInferior and x[i+1] < limSuperior):
            funcaoK = funcaoKs
        else:
            funcaoK = funcaoKa
        diagC[i] = -1 * pow((1/h),2) * calculaIntegral(x[i+1], x[i+2], funcaoK) + pow((1/h),2) * calculaIntegral(x[i+1],x[i+2], "("+funcaoQ+")*("+str(x[i+2])+"-x)*(x-"+str(x[i+1])+")")

    ##  Calculo da diagonal abaixo da diagonal principal.  ##
    for i in range (1, n):
        if(x[i+1] > limInferior and x[i+1] < limSuperior):
            funcaoK = funcaoKs
        else:
            funcaoK = funcaoKa
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

    ##  Retorna vetor com os valores aproximados, nos pontos x_i.  ##
    return vetoruAproximado


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
    ##  Criacao do vetor com valores x_i.  ##
    x = np.zeros(n+2)

    ##  Cálculo do intervalo entre pontos.  ##
    h = 1/(n+1)

    for i in range(0, n+2):
        x[i] = i*h
    
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
