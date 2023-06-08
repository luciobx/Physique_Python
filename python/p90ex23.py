import matplotlib.pyplot as plt
# ecart entre deux dates de mesure
DELTA_T =  0.01
# Nombre de point de mesure
N = 600
# intialiser un tableau de N dates
t = [i*DELTA_T for i in range(N)]
# Intialiser une tableau de concentration nulles
c = [0] * N
# Définir la première concentration
c[0] = 1.000 # en mol.L⁻¹
K = 0.464 # Coef en h⁻¹
# Pour indice date de e la première à l'avant dernière
for i in range(N-1):
    c[i+1] = c[i] - (t[i+1] - t[i]) * K * c[i]
# On prepare le tracé
plt.plot(t, c)
# On prépare les mesure réelles
t_mes = [0, 0.5, 1, 2, 4, 6]
c_mes = [1.000, 0.793, 0.630, 0.396, 0.155, 0.063]
# On prépare la nouvelle courbe
plt.plot(t_mes, c_mes, '+', markersize=12) # pour agrandir le + 
# On trace
plt.show()
    

