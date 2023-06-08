import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator
#masse du système 
M = 0.60 # En kg
#intensité de la pesanteur g
G = 9.81 # en N.kg⁻¹
# Lecture du fichier
# fichier = input("Quel est le nom du fichier de pointage (sans l'extension .csv)?")+".csv"
fichier = "csv\\mouvement_parabolique.csv"
data = pd.read_csv(fichier, sep=';', header=0) # suppose séparateur (;ou,) et nom des champs connus !
# typage (, ->.) et str-> float
t = list(pd.to_numeric(data['Temps'].str.replace(',', '.')))
x = list(pd.to_numeric(data['X'].str.replace(',', '.')))
y = list(pd.to_numeric(data['Y'].str.replace(',', '.')))
#Calcul des coordonnées Vx et Vy des vecteurs vitesse
vx=[]
for i in range(len(x)-1) :
    vx = vx + [(x[i+1]-x[i]) / (t[i+1]-t[i])]
vy=[]
for i in range(len(y)-1) :
    vy = vy + [(y[i+1]-y[i]) / (t[i+1]-t[i])]
# calcule de la vitesse
v = []
for i in range(len(vx)) :
    v = v + [(vx[i]**2 + vy[i]**2)**0.5] # racine carrée ou puissance 1/2
# calcul des énergies
energie_p = [] # Energie potentielle
for i in range(len(vx)) :
    energie_p = energie_p + [M*G*y[i]] # y est l'axe vertical orienté vers le haut
energie_c = []  # Energie cinétique
for i in range(len(vx)) :
    energie_c = energie_c + [0.5*M*v[i]**2]
energie_m = [] # Energie mécanique
for i in range(len(vx))  :
    energie_m = energie_m + [energie_c[i] + energie_p[i]]
# Préparation du graphique
# Ajuster la taille et la position de la fenêtre
plt.figure(figsize=(10, 7))
mngr = plt.get_current_fig_manager()
mngr.window.geometry("+50+50")
# # Ajustement du plot
plt.subplots_adjust(hspace=0.5)
# Sous figure supérieure
plt.subplot(211)
plt.ylim([0, 1.5*max(energie_m)])
plt.xlim([0, max(t)])
#Parametres de la grille
axes = plt.gca()
axes.minorticks_on()
axes.grid(which='major', linestyle='-', linewidth='0.7', color='black')
axes.grid(which='minor', linestyle='-', linewidth='0.5', color='grey')
# Attention le temps dispose d'une valeur de plus !
# Tracé des énergies
plt.plot(t[0:-1], energie_p,'ro', label='Énergie potentielle de pesanteur')
plt.plot(t[0:-1], energie_c,'go', label='Énergie cinétique')
plt.plot(t[0:-1], energie_m,'ko', label='Énergie mécanique')
#Légendes
plt.title("Évolution des énergies au cours du temps", fontsize=10)
plt.ylabel(r'$\mathcal{E}$ (J)', fontsize=10)
plt.xlabel('$t$ (s)', fontsize=10)
plt.tick_params(labelsize=8)
plt.legend(loc=2, fontsize="8")
# Sous figure infèrieure
plt.subplot(212)
plt.ylim([0, 1.1*max(x)])
plt.xlim([0, max(t)])
# #Parametres de la grille
axes2 = plt.gca()
axes2.minorticks_on()
axes2.grid(which='major', linestyle='-', linewidth='0.7', color='black')
axes2.grid(which='minor', linestyle='-', linewidth='0.5', color='grey')
axes2.yaxis.set_minor_locator(AutoMinorLocator(2))
#tracé de la position
plt.plot(t, x, 'bo')
#Légendes
plt.title("Évolution de la position X du système", fontsize=10)
plt.ylabel('X (m)', fontsize=10)
plt.xlabel('$t$ (s)', fontsize=10)
plt.tick_params(labelsize=10)
# tracé
plt.show()
