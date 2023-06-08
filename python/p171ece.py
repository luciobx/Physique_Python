import matplotlib.pyplot as plt
from numpy import log10, arange

# Concentration en hydroxyde de sodium dans la burette
CB = 0.10 # en mol.L⁻¹ 
# Masse d'acide acétylsalycilique
MA = 500 # en mg
# Masse molaire d'acétylsalycilique
M = 180 #en g.mol⁻¹ 
# Mesures 
v_b = [0.010, 0.012, 0.014, 0.016, 0.018, 0.020] # en L volume ajoutés par burette
ph = [3.3, 3.4, 3.5, 3.6, 3.8, 3.9] # pH de la solution
# calculs des coefficents r
r = [] # coefficient R
for v in v_b :
    r.append(log10(CB*v  / (MA*1E-3/M - CB*v)))
# tracé
plt.title('Courbe pH en fonction de R')
plt.xlabel('R')
plt.ylabel('pH')
plt.axis(xmin=-0.5, xmax=0.5, ymin=3, ymax=4.5)
plt.xticks(arange(-0.5, 0.6, 0.1)) # 1 graduation chaque 0.1
plt.yticks(arange(3, 4.6, 0.1))
plt.grid(linestyle="-.")
plt.plot(r, ph, 'ro')
plt.show()
