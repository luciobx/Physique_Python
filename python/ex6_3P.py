# Vérification de la deuxième loi de Kepler
import matplotlib.pyplot as plt
import math as m

# valeurs expérimentales
# date en année
t_ex = [2020, 2021, 2022, 2023, 2024]
# Coordonnées en unité astronomique ua
x = [29.4328410560730, 29.6118356847488,
     29.74576820311831, 29.8342404541355,
     29.8774316380940] # abcisse
y = [-5.3906071859853, -4.2505317595919,
     -3.10349008723970,-1.9519995345194,
     -0.7985426911486] # ordonnées

def calcul_aire(an):
    '''
    renvoyer l'aire parcourue
    '''
    i = t_ex.index(an)
    # calcul des aires 2020-2021
    long1 = m.sqrt(x[i]**2 + y[i]**2)
    long2 = m.sqrt(x[i+1]**2 + y[i+1]**2)
    long3 = m.sqrt((x[i+1]-x[i])**2 + (y[i+1]-y[i])**2)
    demip = (long1 + long2 + long3) / 2 # demi perimetre
    aire = m.sqrt(demip * (demip - long1) * (demip - long2) * (demip - long3))
    return aire
# A compléter

# Préparation du graphique
plt.title("Portion de l'orbite de Neptune dans le référentiel héliocontrique")
plt.xlabel("Abcisse de Neptune (ua)")
plt.ylabel("Ordonnée de Neptune (ua)")
# tracé
plt.plot(x, y, 'b+:')
plt.show()

# calcul des aires
aire_a = calcul_aire(2020)
aire_b = calcul_aire(2022)
print(f"l'aire parcourue par le rayon vecteur entre 2020 et 2021 vaut {round(aire_a, 2)} ua²")
print(f"l'aire parcourue par le rayon vecteur entre 2022 et 2023 vaut {round(aire_b, 2)} ua²")
if abs(aire_b - aire_a) < 1E-2:
    print("Neptune vérifie la deuxième loi de Kepler")
else:
    print("Neptune ne vérifie pas la deuxième loi de Kepler")


