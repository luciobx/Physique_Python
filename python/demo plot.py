import matplotlib.pyplot as plt
x = [-2, 1, 2, 3, 4]
y = [-5, 7, 8, 9,10]

# Tracé 
for i in range(5):
    plt.plot(0, 0, x[i], y[i],'ro') # le graphique deplace sont origine automatiquement !

plt.show()