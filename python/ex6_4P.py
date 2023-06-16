# Représenter l'évolution au cours du temps des énergie cinétique, potentielle de pesanteur et mécanique
# d'un grélon en chute libre

import matplotlib.pyplot as plt

M = 15E-3  # masse du grelon en kg
G = 9.81 # Intensité de la pesanteur en N.kg ⁻ ¹
# Mesures expérimentales
z = [3.13, 2.92, 2.72, 2.51, 2.24, 1.90, 1.63, 1.36, 1.22] # altitude en m
t = [0.04, 0.08, 0.12, 0.16, 0.20, 0.24, 0.28, 0.32, 0.36] # date e s
v = [4.16, 4.32, 4.47, 4.76, 5.16, 5.54, 5.89, 6.11, 6.22] # vitesse en m.s⁻ ¹
# A compléter
# Calcul des valeurs
e_c = [0.5 * M * vi**2 for vi in v]
e_pp = [M * G * alt for alt in z]
e_m = [e_c[i] + e_pp[i] for i in range(len(e_c))]
# Préparation du tracé
plt.title("Etude energétique")
plt.xlabel("Temps (s)")
plt.ylabel("Energie (J)")
plt.grid(".-")
# tracé
plt.plot(t, e_c, 'r+-', label="Ec")
plt.plot(t, e_pp, 'b*:', label="Epp")
plt.plot(t, e_m, 'go-.', label="Em")
plt.legend()
plt.show()

