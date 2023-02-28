"""Disegna, usando uno script Python, la dimensione laterale di un fascio gaussiano in funzione della direzione di propagazione della radiazione.
Assumi una larghezza minima w0 = 10 μm nel fuoco, e la lunghezza d’onda di un laser a elio-neon nel rosso.
Di quanto è aumentato il diametro del fascio ad una distanza dal fuoco z = 3 mm?
Con gli stessi parametri disegna ora l’ampiezza di campo del fascio nel piano in due posizioni: nel fuoco,
e alla distanza di Rayleigh. Come cam- biano relativamente l’ampiezza massima e la larghezza del fascio tra i due punti?
E la sua intensità massima, e quella totale?"""

# la funzione del fascio gaussiano è : y = w0/w(z) * exp(-i*phi(z)) * exp(-i*k*r**2/2*r(z)) * exp(-r**2/w(z)**2)
# dove w(z) è la dimensione laterale del fascio in funzione della distanza z dal fuoco
# e r(z) è la distanza dal centro del fascio in funzione della distanza z dal fuoco


import numpy as np
import matplotlib.pyplot as plt


# Definisco le costanti
w0 = 10e-6
z = 3e-3
lam = 632.8e-9
k = 2 * np.pi / lam
zR = np.pi * w0 ** 2 / lam
r = np.sqrt(x**2 + y**2)


# Definisco le funzioni
def w(z):
    return w0 * np.sqrt(1 + (z / zR) ** 2)


def R(z):
    return z * (1 + (zR / z) ** 2)

def phi(z): # Gouy phase shift
    return np.arctan(z / zR)


def fascio_gaussiano(z, theta):
    return w0 / w(z) * np.exp(-1j * phi(z)) * np.exp(-1j * k * r**2 / (2 * R(z)**2) * np.exp(
        -r ** 2 / w(z) ** 2))

# voglio vedere con dei colori il fascio gaussiano in funzione della direzione di propagazione theta
# quindi theta è una variabile che va da -pi/2 a pi/2
# e z è una variabile che va da 0 a 3 mm

theta = np.linspace(-np.pi / 2, np.pi / 2, 1000)
z = np.linspace(0, z, 1000)

# creo una matrice di z e theta
z, theta = np.meshgrid(z, theta)

# calcolo il fascio gaussiano
fascio = fascio_gaussiano(z, theta)

# disegno il fascio gaussiano
plt.figure()
plt.pcolormesh(z, theta, np.abs(fascio), shading='auto', cmap='magma')
plt.xlabel('z [m]', fontsize=12, fontweight='bold', color='red', labelpad=10, rotation=0)
plt.ylabel('theta [rad]', fontsize=12, fontweight='bold', color='red', labelpad=10, rotation=90)
plt.colorbar(label='fascio gaussiano', orientation='vertical', pad=0.1, fraction=0.05)
plt.tight_layout()
plt.show()

