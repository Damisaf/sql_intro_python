'''

## regiones(data)
Deben crear la función "regiones" para graficar en matplotlib las zonas donde
 la persona estuvo tranquila mirando el partido, donde estuvo aburrida y 
 donde estuvo muy enganchada y entusiasmada. Para ello se utilizará numpy para
  calcular el valor medio y el desvio estandar como se hizo en el punto anterior
   y deberá realizar el siguiente proceso:
- Calcular el valor medio (mean) y el desvio estandar (std) con numpy

Debe crear 3 pares de listas de datos a partir de data:
- En una lista x1 e y1 para almacenar todos los valores menores o iguales
 al valor medio menos el desvio (pulso <= mean-std) y su índice correspondiente
- En una lista x2 e y2 para almacenar todos los valores mayores o iguales
 al valor medio más el desvio (pulso >= mean+std) y su índice correspondiente
- En una lista x3 e y3 para almacenar todos aquelas valores que no haya guardado
 en niguna de las dos listas anteriores y su índice correspondiente

Una vez obtenidos las listas mencionadas, debe dibujar tres scatter plot 
en un solo gráfico. 
Cada uno de los tres scatter plot representa cada una de las listas
 mencionadas que debe dibujar con un color diferente.

NOTA: Les dejamos el ejemplo de como tendrían que armar una de las tres pares
 de listas,
  deben modificar el código siguiente para poder agregar las otras dos pares 
  listas mencionadas (x2 y2 e x3 y3).
IMPORTANTE: Recuerdo calcular "mean" y "std" antes con numpy.

```
x1 = []
y1 = []
for i in range(len(data)):
    if data[i] <= (mean-std):
        x1.append(i)
        y1.append(data[i])
```

# Esquema del ejercicio
Deben crear su archivo de python y crear las funciones mencionadas en este documento. Deben crear la sección "if _name_ == "_main_" y ahí crear el flujo de prueba de este programa:
'''


__author__ = "Damian Safdie"
__email__ = "damiansafdie@gmail.com"
__version__ = "1.1"

import sqlite3
import matplotlib.pyplot as plt
import numpy as np


def fetch():  
    conn = sqlite3.connect("heart.db")
    c = conn.cursor()
    c.execute("SELECT pulso FROM sensor")
    data = c.fetchall()
    pulsos =  [x[0] for x in data]
    conn.close()
    return pulsos


def show(data):
    x = [i for i in range(len(data))]
    y = data
    fig = plt.figure()
    fig.suptitle('Ritmo cardiaco', fontsize=16)
    ax = fig.add_subplot()
    ax.plot(x, y, c='blue', label='pulso')
    ax.legend()
    ax.grid()
    plt.show()
    

def estadistica(data):
    v1 = np.array(data)
    valor_med = np.mean(v1)
    valor_min = np.min(v1)
    valor_max = np.max (v1)
    desvio = np.std(v1)
    print("Valor Medio : ", valor_med)
    print("Valor Minimo: ", valor_min)
    print("Valor Maximo: ", valor_max)
    print("Desvio std  : ", desvio)

    


if __name__ == "__main__":
  # Leer la DB
  data = fetch()

  # Data analytics
  show(data)
  estadistica(data)
  #regiones(data)

