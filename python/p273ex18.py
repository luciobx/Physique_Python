import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from matplotlib.widgets import Slider

def update(val):
    '''
    Actualiser la droite de modélisation et son équation,
    val float la valeur du curseur
    modifie en place
    periode_ma (numpy.ndarray)
    init_a[0] float 
    '''
    periode_aj = val * rayon_ma # Nouvelle equation y = ax
    modele[0].set_ydata(periode_aj)
    # le tracé est mis à jour en arrière plan
    # il faut mettre à jour l'objet equation
    equation.set_text(f'T² = {val:.2e} r³')

# Obtention des données type csv
fichier = 'csv\\Satellites_artificiels.csv'
data = pd.read_csv(fichier, sep=';', header=0) # encoding = utf-8
# Mise en forme des données, periode et rayon sont des objets pandas !
periode = data['T(s)']**2 # On conserve T²
rayon = (data['a(km)']*1E3)**3 # On conserve r³
# Calcul de la régression linéaire f sur T² = f(r³)
regression = np.polyfit(rayon, periode, 1) # renvoie les coefficients a, b d'un modèle ax+b
pente_moyenne = regression[0]
# initalisation d'un modèle ajustable y = ax 
init_a = 6.00e-14 #pente initiale du modèle
rayon_ma = np.linspace(0, rayon[2]*2, 5) # rayon du modele ajustable
periode_ma = init_a * rayon_ma # periode du modele ajustable

# Tracé des points expérimentaux et de la régression linéaire
# taille et position de la fenêtre
plt.figure(figsize=(10,6))
plt.get_current_fig_manager().window.geometry("+5+5")
# Ajustement du plot
plt.subplots_adjust(bottom=0.25) # espace en % pour le curseur 
# définition des axes
plt.axis([0, max(rayon)*1.15, 0, max(periode)*1.15])
plt.grid() # Paramètre de la grille
# légendes des axes
plt.xlabel('r ³ (m ³)', fontsize=12)
plt.ylabel('T ² (s ²)', fontsize=12)
plt.tick_params(labelsize=10)
plt.title('T ² = f(r ³)', fontsize=15)
# Tracé des points de mesure
# plt.scatter(rayon, periode, s=50, color='r', marker='x', label='points expérimentaux')
plt.plot(rayon, periode, 'r+', label='points expérimentaux', markersize=10)
# Affichage du modèle ajustable, modele[0] de classe matplotlib.lines.Line2D
modele = plt.plot(rayon_ma, periode_ma, '-g', label='modélisation')
plt.legend(loc=2, fontsize=10) #Légende du graphique
# affichage de l'équation dans le graphique
equation = plt.text(max(rayon)*0.7,max(periode)*0.15,
                    f'T ² = {init_a:.2e} r ³',
                    fontsize = 16, color="green", backgroundcolor = "#FFFF55")
# Création d'un curseur
rectangle_a = plt.axes([0.25, 0.1, 0.5, 0.02]) # en % fenetre x, y, largeur, hauteur
curseur = Slider(rectangle_a, 'coeff directeur', 0, pente_moyenne*2, valinit=init_a) # deb, fin, pos
# appel update lorsque le curseur est modifié
curseur.on_changed(update)
plt.show() # tracé en boucle



