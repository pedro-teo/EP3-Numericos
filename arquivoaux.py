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