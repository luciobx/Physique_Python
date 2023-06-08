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

