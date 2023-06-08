import matplotlib.pyplot as plt
import numpy as np

def calcul_quantites_avant_et_a_equivalence(i_ajout):
    v.append(i_ajout) # en nombre d'ajout
    n_AH.append((0.145*10.0 - 0.100*(VDOSE*i_ajout)) * 0.001) # n_AH = c_AH * v_AH  
    n_HO.append(0)
    n_Na.append(0.10 * i_ajout * 0.001)
    n_A.append(0.10 * i_ajout * 0.001)

def calcul_quantites_apres_equivalence(i_ajout) :
    # pass
    v.append(i_ajout)
    n_AH.append(0)
    n_HO.append(0.100*(VDOSE*i_ajout)* 1E-3)
    n_Na.append(0.100*(VDOSE*i_ajout)* 1E-3)
    n_A.append(n_A[-1])

VEQUIVALENCE = 14.5  # Volume équivalence en mL
VEAU = 200 # Volume d’eau ajouté en mL
VDOSE = 1 # Dose délivrée à chaque ajout du réactif titrant en mL
n_AH, n_HO, n_Na, n_A, v = [], [], [], [], [] # initialisation de 5 listes de valeurs
for ajout in range(0, 26, 1) : # nb ajout volume titrant
    if ajout*VDOSE <= VEQUIVALENCE :
        #appelle une fonction qui calcule les quantités avant et à l’équivalence
        calcul_quantites_avant_et_a_equivalence(ajout)
    else :
        #appelle une fonction qui calcule les quantités après l’équivalence
        calcul_quantites_apres_equivalence(ajout)       
# Expression de la conductivité
# Eau + V titrant + titree 10mL acide aqueux 
conductance = (20*np.array(n_HO) + 5.0*np.array(n_Na) + 4.1*np.array(n_A)) / (VEAU*1E-3 + np.array(v)*1E-3 + 10E-3)

# affichage des courbes
plt.subplot(121) # subplot permet d’afﬁcher deux graphes
plt.plot(v, n_AH,'bx-', linewidth=0.5, label="n_AH")
plt.legend()
plt.subplot(122)
plt.plot(v, conductance, 'bo', label=r"Conductivité en $\mathrm{mS\cdot m^{-1}}$") # Affichage en Latex
plt.legend()
plt.show()

