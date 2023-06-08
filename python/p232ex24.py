import csv
import matplotlib.pyplot as plt

def import_csv (cible, sep, n):
    '''
    Renvoyer les données d'une colonne d'un fichier csv de séparateur choisi.
    cible : str chemin absolu ou relatif du fichier"
    sep : str le séparateur utilsé (; ou ,)
    n :  int la colonne souhaitée ( à partir de 0)
    rep : liste [ [float]...] les valeurs numériques de la colonne sélectionnée
    '''
    rep = []
    with open(cible, 'r', encoding='utf-8', newline='') as fichier:
        fichier.readline() # elimine la première ligne des noms des champs si nécessaire
        reader = csv.reader(fichier, delimiter=sep)
        for row in reader:
            notation_point = row[n].replace(",",".") # changer le format des nombres "3,5" "3.5"
            rep.append(float(notation_point)) # Transformer en nombre les str
    return rep

K = 0.02 # Facteur echelle pour les accélérations
# Nom du fichier à traiter son chemin csv\balle_de_tennis §attention \ pour les chemins et non /
# m_fichier = input("Quel est le nom du fichier de pointage (sans l'extension .csv)? ") + ".csv"
m_fichier = r"csv\balle_de_tennis.csv"
# Lire les données.
t = import_csv(m_fichier, ";", 0) # la date en s
x = import_csv(m_fichier, ";", 1) # La position abcisse en m
y = import_csv(m_fichier, ";", 2) # La position ordonnée en m

# Calcul des coordonnées vx et vy des vecteurs vitesse
vx = []
for i in range(len(x)-1) :
    vx = vx + [(x[i+1]-x[i]) / (t[i+1]-t[i])]
vy = []
for i in range(len(y)-1) :
    vy = vy + [(y[i+1]-y[i]) / (t[i+1]-t[i])]
# Calcul des coordonnées ax et ay des vecteurs accélération
ax = []
for i in range(len(vx)-1) :
    ax =  ax + [(vy[i+1]-vy[i]) / (t[i+1]-t[i])]
ay = []
for i in range(len(vy)-1) :
    ay =  ay + [(vy[i+1]-vy[i]) / (t[i+1]-t[i])]

# Légende
plt.title("Tracé des positions et vecteurs accélération")
plt.xlabel('x (m)')
plt.ylabel('y (m)')
plt.grid()
plt.text(0.9*max(x), 0.8*max(y), f"Échelle : {10} m‧s⁻²",  color="blue")
plt.plot([2, 2],[0, 10*K], '_-', color='blue') # trace un trait d'échelle 
# Tracé 
for i in range(len(t)-1):
    plt.plot(0, 0, x[i], y[i],'ro') # position
    # vecteurs accélération
    if i < len(t)-2:
        plt.arrow(x[i+1] , y[i+1],
                  ax[i]*K, ay[i]*K, #appliquer le facteur echelle
                  color='b',
                  head_width=0.03,
                  head_length=0.05,
                  length_includes_head=True)
        plt.text(x[i+1]+0.05, y[i+1]-0.15,
                 r'$ \overrightarrow{a}_{%.i}$'%(i+2),
                 color="blue")   
plt.show()
#sauvegarde sous forme d'image
plt.savefig("vecteurs-accélération.png")

