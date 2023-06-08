import numpy as np
import matplotlib.pyplot as plt
from math import log10


CBI = 0.1  # mol.L⁻¹ Concentration initiale en ion benzoate C₆H₅COO⁻
CA = 0.100 # mol.L⁻¹ Concentration en ion oxonium H³O⁺ solution titrante
V0 = 10 # en mL volume de la solution titrée de benzoate de sodium
VE = 10 # en mL volume de solution titrante à l'équivalence

# Initialisation de 5 tableaux de concentrations en ion benzoate (cb), acide benzoique (cbh), oxonium (ch),  pH et v
cb, cbh, ch, ph, v = [], [], [], [], []

### Remplissage des 5 listes suivant le volume va ajouté 
for va in np.arange(1,26,0.5) :
    if va < VE :
        v.append(va)
        cb.append((CBI*V0 - CA*va) / (V0 + va)) 
        cbh.append((CA*va / (V0 + va)))
        ch.append(0)
        ph.append(4.2 + log10((0.1*V0 - CA*va) / (CA * va))) 
    elif va > VE:
        pass

# Affichage des graphiques
# Ajuste la taille
# Positionner la fenêtre
plt.figure(figsize=(10, 5)) 
mngr = plt.get_current_fig_manager()
mngr.window.geometry("+300+100")
# Dessiner
plt.subplot(121)
plt.plot(v, cb, 'bx-', label="CB")
plt.plot(v, cbh, 'rx-', label="CBH")
plt.legend()
plt.subplot(122)
plt.ylim(0,14)
plt.plot(v, ph, 'rx-', label="pH")
plt.legend()
plt.show()
