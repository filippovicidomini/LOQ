"""Disegna, usando uno script Python, la dimensione laterale di un fascio gaussiano in funzione della direzione di propagazione della radiazione.
Assumi una larghezza minima w0 = 10 μm nel fuoco, e la lunghezza d’onda di un laser a elio-neon nel rosso.
Di quanto è aumentato il diametro del fascio ad una distanza dal fuoco z = 3 mm?
Con gli stessi parametri disegna ora l’ampiezza di campo del fascio nel piano in due posizioni: nel fuoco,
e alla distanza di Rayleigh. Come cam- biano relativamente l’ampiezza massima e la larghezza del fascio tra i due punti?
E la sua intensità massima, e quella totale?"""

# la funzione del fascio gaussiano è : y = w0/w(z) * exp(-i*phi(z)) * exp(-i*k*r**2/2*r(z)) * exp(-r**2/w(z)**2)
# dove w(z) è la dimensione laterale del fascio in funzione della distanza z dal fuoco
# e r(z) è la distanza dal centro del fascio in funzione della distanza z dal fuoco


import matplotlib.pyplot as plt
import numpy as np

# Definisco le costanti
w0 = 10e-6
z = 3e-3
lam = 632.8e-9
k = 2 * np.pi / lam
zR = np.pi * w0 ** 2 / lam
E0 = 10

x = np.linspace(-10, 10, 1000)
y = np.linspace(-10, 10, 1000)
x, y = np.meshgrid(x, y)



# Definisco le funzioni
def w(z):
    return w0 * np.sqrt(1 + (z / zR) ** 2)


def R(z):
    return z * (1 + (zR / z) ** 2)


def phi(z):  # Gouy phase shift
    return np.arctan(z / zR)

def r(x, y):
    return np.sqrt(x ** 2 + y ** 2)

z = np.linspace(0, 3e-3, 1000)

def fascio_gaussiano(z, x, y):
    return w0 / w(z) * np.exp(-1j * phi(z)) * np.exp(-1j * k * r(x, y) ** 2 / (2 * R(z))) * np.exp(
        -r(x, y) ** 2 / w(z) ** 2) * np.exp(-1j * k * z) * E0
