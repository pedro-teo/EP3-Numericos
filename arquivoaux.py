## to achando que esses for aqui tao errados K
    resposta = np.zeros(n+2)
    for i in range(0, n+1):
        print(x[i])
        for j in range(1, n+1):
            print("par:")
            print(x[j-1])
            print(x[j])
            print(x[j+1])
            print()
            if  (x[i] >= x[j-1] and x[i] <= x[j]):
                resposta[i] = resposta[i] + vetorAlfa[j] * (x[i]-x[j-1])/h
            elif(x[i] <= x[j+1] and x[i] >= x[j]):
                resposta[i] = resposta[i] + vetorAlfa[j] * (x[j+1]-x[i])/h
            else:
                #qalo
                resposta[i] = resposta[i] + 0
    print(resposta)

    # comentarios para teste de calculo de integral
    #olaaa = "+3"
    #print(calculaIntegral(-1,2,"("+"pow(x,2)"+")"+olaaa))
    #print(calculaIntegralNDois(-1,2,"("+"pow(x,2)"+")"+olaaa))
    #olaaa = "+1"
    #print(calculaIntegralNDois(0,2,"("+"3*pow(x,2)+6*x"+")"+olaaa))
    #print(calculaIntegral(0,2,"("+"3*pow(x,2)+6*x"+")"+olaaa))