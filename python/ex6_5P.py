# Tracé des courbes expérimentale de la charge d'un condensateur
# avec un conducteur ohmique de 10Ω

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

R = 10 # en ohm

# valeurs expérimentales
# date en seconde
t_ex = np.array([0, 100, 200, 300, 400, 500, 600, 700, 800,
                 1000, 1500, 2000, 3000, 4000, 5000, 7000])
# tensions aux bornes du condensateur en volt
uc_ex = np.array([0, 0.22, 0.42, 0.6, 0.76, 0.9, 1.03, 1.16,
                  1.27, 1.45, 1.79, 1.99, 2.19, 2.26, 2.28, 2.3])

def modele(x, a, b):
    return a * (1 - np.exp(-x/b))

u_inf = max(uc_ex)
# p0 initialisation nécessaire des valeurs des parametres si le modèle n'est pas trouvé
(params, covariance) = curve_fit(modele, t_ex, uc_ex, p0 = [u_inf, R])  
# A compléter

# calcul de la capacité
c = int(params[1] / R ) # en farad
# Préparation du graphique
plt.title("Etude de la charge d'un condensateur")
plt.xlabel("Temps (s)")
plt.ylabel("Uc (V)")
plt.grid()
# affichage de l'équation dans le graphique
plt.text(3000, 1,
         f'Uc(t)={params[0]:.2f}*(1-exp(-t/{int(params[1])}))',
         fontsize = 10, color="blue", backgroundcolor = "#FFFFFF")
plt.text(3000, 0.7,
         f'C = {c} F',
         fontsize = 10, color="blue", backgroundcolor = "#FFFFFF")
# tracé
plt.plot(t_ex, uc_ex, "bo", label="Mesures")
plt.plot(t_ex, modele(t_ex, params[0], params[1]), 'g--',
         label=f'modele: U∞={params[0]:.2f}V, tau ={int(params[1])} s ⁻¹')
plt.legend()
plt.show()
