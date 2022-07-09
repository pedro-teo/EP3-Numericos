# cabecalho pra n dar warnings
import numpy as np
n = 54
x = np.zeros(n)
h = 3434
vetorAlfa = np.zeros(23)
# fim do cabecalho inutil

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

    # comentarios para teste de calculo de integral
    #olaaa = "+3"
    #print(calculaIntegral(-1,2,"("+"pow(x,2)"+")"+olaaa))
    #print(calculaIntegralNDois(-1,2,"("+"pow(x,2)"+")"+olaaa))
    #olaaa = "+1"
    #print(calculaIntegralNDois(0,2,"("+"3*pow(x,2)+6*x"+")"+olaaa))
    #print(calculaIntegral(0,2,"("+"3*pow(x,2)+6*x"+")"+olaaa))