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
    return (valor_med, desvio)

def regiones(data):
    v1 = np.array(data)
    mean = np.mean(v1)    
    std = np.std(v1)
    x1 = []
    y1 = []
    x2 = []
    y2 = []
    x3 = []
    y3 = []
    for i in range(len(data)):
        if data[i] <= (mean-std):
            x1.append(i)
            y1.append(data[i])
        elif data[i] >= (mean+std):
            x2.append(i)
            y2.append(data[i])
        else:
            x3.append(i)
            y3.append(data[i])

    fig = plt.figure()
    fig.suptitle('Regiones', fontsize=16)
    ax1 = fig.add_subplot(1, 3, 1)  
    ax2 = fig.add_subplot(1, 3, 2)  
    ax3 = fig.add_subplot(1, 3, 3) 

    ax1.plot(x1, y1, c='darkgreen', label='aburrida')
    ax1.legend()
    ax1.grid()

    ax2.scatter(x2, y2, c='darkred', label=' entusiasmada')
    ax2.legend()
    ax2.grid()

    ax3.scatter(x3, y3, c='blue', label='tranquila')
    ax3.legend()
    ax3.grid()

    plt.show()
        


if __name__ == "__main__":
  # Leer la DB
  data = fetch()

  # Data analytics
  show(data)
  estadistica(data)
  regiones(data)


