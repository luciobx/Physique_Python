ph = float(input('pH de la solution ? pH = ')) # pH de la solution
c = float(input('Concentration en soluté apporté en mol.L⁻¹ ? C = '))
v = float(input('Volume de la solution en L ? V = '))
xf = 10**(-ph*v)
xmax = c * v
tau = round(xf/xmax, 2) # arrondi pour l'affichage
if tau > 1 :
    print("tau d'avancement = ", tau, "impossible")
elif tau == 1:
    print("tau d'avancement = ", tau, "Acide fort")
else:
    print("tau d'avancement = ", tau, "Acide faible")
