import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Slider

#Fonction d'actualisation des courbes
def update(_x):
    '''
    Actualiser le graphique
    x float la valeur de l'un des curseurs
    variables globales curseur_A, curseur_T, curseur_PHI
    Modifie en place les tracés p1, p2 et p3
    '''
    # Nouveaux coefficients des objets curseurs
    A = curseur_A.val
    T = curseur_T.val
    PHI = curseur_PHI.val
    # Calcul nouveau jeux de valeurs
    y_1 = A * np.cos(2*np.pi/T * time)
    y_2 = A * np.cos(2*np.pi/T * time + PHI)
    y_3 = y_1 + y_2
    #mis à jour des tracés
    p1[0].set_ydata(y_1)
    p2[0].set_ydata(y_2)
    p3[0].set_ydata(y_3)

    
#  valeurs par défaut
AMP = 1.00 # Amplitude
PER = 2.00 # Periode
DPHA = 1.00 # Dephasage
# Définitions des courbes
time = np.linspace(0, 20, 2000)
y1 = AMP * np.cos(2*np.pi/PER * time)
y2 = AMP * np.cos(2*np.pi/PER * time + DPHA)
y3 = y1 + y2

#Tracé des courbes
# taille et position de la fenêtre
plt.figure(figsize=(10,6))
plt.get_current_fig_manager().window.geometry("+5+5")
# Ajustement du plot
plt.subplots_adjust(bottom=0.35) #on laisse un espace pour le curseur
# définition des axes
plt.axis([0, 20, -10, 10])
plt.grid() # Paramètre de la grille
# légendes des axes
plt.xlabel('$t$ (s)')
plt.ylabel('Amplitude ')
plt.title('Somme de deux ondes sinusoïdales synchrones ')

# tracé des courbes pn[0] de classe matplotlib.lines.Line2D
p1 = plt.plot(time, y1, '-g',label=r'$y_1 = A \times \cos( \frac{2\pi}{T}\times t)$')
p2 = plt.plot(time, y2, '-b',label=r'$y_2 = A \times \cos( \frac{2\pi}{T}\times t + \Phi)$')
p3 =  plt.plot(time, y3, '-r',label=r'$y_3= y_1 + y_2$')
plt.legend(loc=2, fontsize=10) #Légende du graphique


# Création des curseurs
# Curseur periode
rectangle_a = plt.axes([0.25, 0.1, 0.5, 0.02])
curseur_T = Slider(rectangle_a, 'Période $T$ (s)', 1, 10, valinit=PER)
# Curseur amplitude
rectangle_b = plt.axes([0.25, 0.155, 0.5, 0.02])
curseur_A = Slider(rectangle_b, 'Amplitude $A$ (m)', 0, 5, valinit=AMP)
# Curseur phase
rectangle_c = plt.axes([0.25, 0.210, 0.5, 0.02])
curseur_PHI = Slider(rectangle_c, r'Phase $\phi$ (rad)', 0, 5, valinit=DPHA)

# appel update lorsque l'un des curseurs est modifié
curseur_T.on_changed(update)
curseur_A.on_changed(update)
curseur_PHI.on_changed(update)

plt.show()