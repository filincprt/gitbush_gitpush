import matplotlib.pyplot as plt
import numpy as np

def lagrange_polynomial(x, nodes):
    result = 0
    for i in range(len(nodes)):
        term = nodes[i][1]
        for j in range(len(nodes)):
            if i != j:
                term *= (x - nodes[j][0]) / (nodes[i][0] - nodes[j][0])
        result += term
    return result
    # Комментарий, которого нет в локальной версии
    # Комментарий, которого нет в локальной версии

# Узловые точки
nodes = [(1, -3), (2, -2), (4, 2), (7, 8)]

x_values = np.linspace(0, 8, 400)
y_values = [lagrange_polynomial(x, nodes) for x in x_values]

plt.plot(x_values, y_values, label='Interpolation Polynomial')
plt.scatter(*zip(*nodes), color='red', label='Nodes')
plt.xlabel('x')
plt.ylabel('P(x)')
plt.legend()
plt.title('Interpolation Polynomial and Nodes')
plt.grid(True)
plt.show()
