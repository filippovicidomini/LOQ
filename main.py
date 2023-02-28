"""Disegna, usando uno script Python, la dimensione laterale di un fascio gaus- siano in funzione della direzione di propagazione della radiazione.
Assumi una larghezza minima w0 = 10 μm nel fuoco, e la lunghezza d’onda di un laser a elio-neon nel rosso.
Di quanto è aumentato il diametro del fascio ad una distanza dal fuoco z = 3 mm?
Con gli stessi parametri disegna ora l’ampiezza di campo del fascio nel piano in due posizioni: nel fuoco,
e alla distanza di Rayleigh. Come cam- biano relativamente l’ampiezza massima e la larghezza del fascio tra i due punti?
E la sua intensità massima, e quella totale?"""

import numpy as np
import matplotlib.pyplot as plt

# Definisco le costanti
w0 = 10e-6
z = 3e-3
lam = 632.8e-9
k = 2*np.pi/lam
zR = np.pi*w0**2/lam

# Definisco le funzioni
def w(z):
    return w0*np.sqrt(1+(z/zR)**2)

def R(z):
    return z*(1+(zR/z)**2)

def E(z,theta):
    return np.exp(-2*(w(z)*np.cos(theta))**2/w0**2)

# Definisco gli array
theta = np.linspace(-np.pi/2,np.pi/2,1000)
z = np.linspace(0,3e-3,1000)

# Disegno la dimensione laterale del fascio in funzione della direzione di propagazione
plt.figure(1)
plt.plot(theta*180/np.pi,w(z))
plt.xlabel('theta [°]')
plt.ylabel('w [m]')
plt.title('Dimensione laterale del fascio in funzione della direzione di propagazione')
plt.grid(0.5)
plt.show()
