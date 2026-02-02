import matplotlib.pyplot as plt
import numpy as np

paises = ["Brasil", "China", "Russia","Africa"]
valores = [12,2,3,0]

def plotGraph(paises, valores):

    plt.figure(figsize=(10,6))
    plt.plot(paises,valores, 'r--')
    plt.show()

# plotGraph(paises, valores)
valores, paises = zip(*sorted(zip(valores, paises)))

print(valores)
print(paises)