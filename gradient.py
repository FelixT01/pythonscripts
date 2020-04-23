#!/usr/bin/python3
import numpy as np
import matplotlib.pyplot as plt

# funcion para optimizar
# V[x,y]


def f(V): return np.sin(0.5*V[0]*V[0] - 0.25*V[1]
                        * V[1] + 3)*np.cos(2*V[0] + 1 - np.e ** V[1])

# data
res = 100
X = np.linspace(-3, 3, res)
Y = np.linspace(-3, 3, res)
Z = np.zeros((res, res))  # Z is filled with zeros

# fill Z with the funcion f
for ix, x in enumerate(X):
    for iy, y in enumerate(Y):
        Z[iy, ix] = f([x, y])


# draw the surface
plt.contourf(X, Y, Z, res)
plt.colorbar()

# random point
P = np.random.rand(2)*6 - 3
plt.plot(P[0], P[1], "o", c="red")

# vector gradiente (con coordenadas las derivadas parciales dP/dP[0] y dP/dP[1])
# df/dx = lim h->0 (f(x+h)-f(x))/h
h = 0.001
lr = 0.01  # Learning Rate
grad = np.zeros(2)  # Vector gradiente de dos pocisiones

for _ in range(1000):
    for i, x in enumerate(P):
        _P = np.copy(P)  # Para no derivar sobre la derivada
        _P[i] = _P[i] + h
        deriv = (f(_P) - f(P))/h  # Derivando parcialmente cada parametro
        grad[i] = deriv
    P = P - lr*grad  # Invirtiendo el gradiente para ir decendiendo.
    if(_ % 1 == 0):
        plt.plot(P[0], P[1], ".", c="green")

print("Red point is Start")
plt.show()

#print("this is x: ", X)
#print("this is y: ", Y)
