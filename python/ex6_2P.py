# Tracé des courbes théoriques et expérimentales
# de la décharge d'un condensateur de 100 μF
# dans un conducteur ohmique de 20kΩ

import matplotlib.pyplot as plt
import numpy as np

C = 100E-6 # en farad
R = 20E3 # en ohm
UINIT = 5 #en volt

# valeurs expérimentales
# date en seconde
t_ex = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
                 10, 11, 12])
# tensions aux bornes du condensateur en volt
uc_ex = np.array([4.99, 3.08, 1.93, 1.2, 0.75,
                  0.47, 0.3, 0.19, 0.12, 0.07, 0.05,
                  0.03, 0.02])
# A compléter
# Calcul de la courbe théorique
tau = R * C
t_theo = np.linspace(0, 12, 50) # rmq bornes inclues
u_theo = UINIT * np.exp(-t_theo/tau)

# Préparation du graphique
plt.title("Etude de la décharge d'un condensateur dans une resistance")
plt.xlabel("Temps (s)")
plt.ylabel("Uc (V)")
plt.grid()
# tracé
plt.plot(t_ex, uc_ex, "bo", label="Mesures")
plt.plot(t_theo, u_theo, "r", label="Modèle théorique")
plt.legend()
plt.show()
