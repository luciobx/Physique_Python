import matplotlib.pyplot as plt
import numpy as np
# Données expérimentales
x = [10.0, 7.5, 5.0, 2.5, 1.0] # C en mm.L⁻¹
y = [5.88, 4.41, 2.94, 1.47, 0.59] # G en mS
# Affichage
plt.title("G=f(C)")
plt.xlabel("C (mm.L\u207B\u00B9)") # unicode ⁻¹
plt.ylabel("G (mS)")
plt.plot(x, y, "bo", label='Mesures') # symbole blue o
plt.legend() 
plt.axis(xmin=0, xmax=10, ymin=0, ymax=6)
plt.grid(linestyle="-.")
plt.xticks(range(11)) # nb de lignes
# Modélisation pôlynome ordre 1
coef = np.polyfit(x, y, 1) # renvoie array([0.5878424 , 0.00121951])
# Calcul du modèle pour 5 valeurs prises entre 0 et xmax
xmod = np.linspace(0, max(x), 5)
modele = [coef[1] + coef[0] * val for val in xmod]  # Calcul du modèle
plt.plot(xmod, modele, color = "red", label =f"Modele y = {coef[0]:.2f}x + {coef[1]:.2f}") # "r-"
plt.legend()
plt.show() # affiche la figure à l'écran
