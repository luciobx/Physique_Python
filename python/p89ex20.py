import matplotlib.pyplot as plt
# Compléter les listes suivantes à partir de l'exercice 13
t = [0, 200, 400, 600, 800, 1000, 2000] # date en min
c = [200, 100, 50, 25, 12.5, 6.3, 3.1] # concentration en mmol.L⁻ ¹
# calcule des vitesses de disparition
vd = []
# pour indice de 1er date à avant dernière calculer vd
for i in range (len(t)-1) :
    vd = vd + [-1*((c[i+1]-c[i]) / (t[i+1]-t[i]))] # On veut une vitesse positive
# recherche des valeurs max pour dimensionner les graphiques
c_max = max(c)
t_max = max(t)
vd_max = max(vd)
# On veut disposer d'un deuxième jeu d'abcisse pour le graphique de vitesse vd = f(concentration)
c_2 = list(c) # On fait une copie (superficielle)
del c_2[-1] # -1 est l'indice du dernier élément
c2_max = max(c_2)
plt.figure(figsize=(16,8))
#sous-figure 1 - Graphique donnant l'évolution de la concentration en fonction du temps
plt.subplot(221) # 2 lignes 2 colonnes 1er cadre
plt.grid()
plt.title("Évolution de la concentration en fonction du temps")
plt.xlim(0, 1.15*t_max) # Pour avoir un graphe plus grand de 15%
plt.ylim(0, 1.15*c_max)
plt.scatter(t, c)        # permet d'afficher un nuage de points, la fonction plt.plot les affiche reliés par défaut
plt.xlabel("Temps (min)")
plt.ylabel(r"Concentration ($\mathrm{mmol \cdot L^{-1}}$)") # Latex
#sous-figure 2- Graphique donnant l'évolution de la vitesse de disparition en fonction du temps
plt.subplot(222) # 2 lignes 2 colonnes 2ieme cadre
plt.grid()
plt.title("Évolution de la vitesse de disparition en fonction de la concentration")
plt.xlim(0,1.15*c2_max)
plt.ylim(0,1.15*vd_max)
plt.scatter(c_2, vd, color='orange')
plt.ylabel(r"Vitesse ($\mathrm{mmol\cdot L^{-1} \cdot min^{-1}}$)")
plt.xlabel(r"Concentration ($\mathrm{mmol\cdot L^{-1}}$)")
#afficher dans la fenêtre (On fait un graphhe vide)
plt.subplot(212, frameon=True)  # 2 ligne 1 colonne cadre ligne 2
plt.xticks([]) # [n] graduation à indiquer ici aucune
plt.yticks([])
for i in range (len(t)-1) :
    plt.text(0.1,
             ((len(t)-1)-i)/len(t),
             "La vitesse de disparition à " +
             str(t[i]) +" min est v("+str(t[i]) +
             ")=" +
             str(round(vd[i],3)) +
             r"$\mathrm{mmol\cdot L^{-1} \cdot min^{-1}}$",
             fontsize = 10 )
plt.show()
