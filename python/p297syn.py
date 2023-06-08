import numpy as np

# angle de lancement par rapport à l'horizontale 
V0 = 25 # en degre
# intensité de la pesanteur g
G = 9.81 # en m·s⁻² 

# angle de lancement converti de degré en radian
alpha = np.radians(V0) 
# calcul de la durée maximale
tmax = (2 * V0 * np.sin(alpha) / G) * 1.1 # Depassement de 10%
# calcul des dates
t = np.linspace(0, tmax, 10)
# calcul des coordonnées x et y des positions
x = V0 * np.cos(alpha) * t
y = -G/(2*(V0 * (np.cos(alpha)))**2) *  x**2 + np.tan(alpha) * x
# calcul des coordonnées vx et vy des vecteurs vitesse
vx=[]
for i in range(len(x)-1) :
    vx = vx + [(x[i+1]-x[i]) / (t[i+1]-t[i])]
vy=[]
for i in range(len(y)-1) :
    vy = vy + [(y[i+1]-y[i]) / (t[i+1]-t[i])]
# calcul des coordonnées ax et ay des vecteurs accélération
ax = []
for i in range(len(vx)-1) :
    ax = ax + [(vx[i+1]-vx[i]) / (t[i+1]-t[i])]
ay = []
for i in range(len(vy)-1) :
    ay = ay + [(vy[i+1]-vy[i]) / (t[i+1]-t[i])]
    
# affichage dans la console
print ("coordonnées successives de la position, (x ; y)")
for i in range (len(x)):
    print(f'({x[i]:+.2E} m ; {y[i]:+.2E} m)') #+ pour le signe .2 pour 2 chiffres et E pour Exposant
print()
print ("coordonnées successives de la vitesse, (vx ; vy)")
for i in range (len(vx)):
    print(f'({vx[i]:+.2E} m·s⁻¹ ; + {vy[i]:+.2E} m·s⁻¹)') 
print("")

print ("coordonnées successives de l'accélération, (ax ; ay)")
for i in range (len (ax)):
    print(f'({ax[i]:+.2E} m·s⁻² ; + {ay[i]:+.2E} m·s⁻²)') 
