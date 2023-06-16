# Tracé de la caractéristique d'une pile
import numpy as np
import matplotlib.pyplot as plt

# Points expérimentaux
intensite = [0, 0.025, 0.036, 0.048, 0.069] # en A
tension = [1.1, 1.08, 1.07, 1.06, 1.04] # en V

# A compléter

# Préparation du graphique
plt.title("Caractéristique de la pile Daniell")
plt.xlabel("Intensité du courant (A)")
plt.ylabel("Tension aux bornes de la pile (V)")
plt.gca().set_xlim(0, max(intensite)*1.1)
plt.gca().set_ylim(0, max(tension)*1.1)
plt.grid()

# modélisation
coefficients = np.polyfit(intensite, tension, 1)
# calcul du modèle
i_model = np.linspace(0, max(intensite), 10) # calcul pour 10 points
u_model = [coefficients[1] + coefficients[0] * val for val in i_model]

# tracé
plt.plot(intensite, tension, "b+")
plt.plot(i_model, u_model, 'r')
plt.show()