import matplotlib.pyplot as plt
import numpy as np
p_ka = float(input('pKA du couple HA / A-  ? '))
ph = np.linspace(0, 14, 1000) # Axe linéaire de 1000 valeurs entre 0 et 14
ph_ad = [100 / (1 + 10**(i-p_ka)) for i in ph] # Jeu de valeur pH décroissant
ph_ac = [100 / (1 + 10**(p_ka-i)) for i in ph] # Jeu de valeur pH croissant
plt.title('Diagramme de distribution d\'un couple HA/A-')
plt.xlabel('pH')
plt.ylabel('%')
plt.axis(xmin=0, xmax=14, ymin=0, ymax=100)
plt.xticks(range(15))
plt.yticks(range(0, 110, 10))
plt.grid(linestyle="-.")
plt.plot(ph, ph_ac, color='r', label='% en HA' )
plt.plot(ph, ph_ad, color='b',label='% en A-' )
plt.show()
