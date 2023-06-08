import matplotlib.pyplot as plt
from random import randint, random

def creation_echantillon(na, nb, nc, nd) :
    '''
    Renvoie un echantillon de na espèce A, n b espèce B, nc espèce C, nd espèce D
    na, nb, nc, nd : int par exemple 1, 2, 3, 4
    echantillon [str]  par exemple ['A', 'B', 'B', 'C', 'C', 'C', 'D', 'D', 'D', 'D']
    '''
    echantillon = []
    for _ind in range(na) :
        echantillon.append("A")
    for _ind in range(nb) :
        echantillon.append("B")
    for _ind in range(nc) :
        echantillon.append("C")
    for _ind in range(nd) :
        echantillon.append("D")
    return echantillon

def comptage_especes(ech, nb_a, nb_b, nb_c, nb_d): # fonction qui compte le nombre d'espèces
    '''
    Dénombre dans l'echantillon  ech le nombre de chaque espèce A, B, C, D
    Ajoute en place ces nombres dans les listes nb_a, nb_b, nb_c, nb_d 
    '''
    n_entite = len(ech)
    nbea, nbeb, nbec, nbed = 0,0,0,0
    for j in range(n_entite):
        if ech[j] == "A" :
            nbea = nbea + 1
        elif ech[j] == "B" :
            nbeb = nbeb + 1
        elif ech[j] == "C" :
            nbec = nbec + 1
        elif ech[j] == "D" :
            nbed = nbed + 1
    nb_a.append(nbea)
    nb_b.append(nbeb)
    nb_c.append(nbec)
    nb_d.append(nbed)

def collision(pac, collision_ab) : # fonction qui génère des collisions et remplace A, B éventuellement
    n_entite = len(pac) # nombre d'entité dans le sac
    # définir deux indices différents
    n1 = randint(0, n_entite-1)
    n2 = randint(0, n_entite-1)
    while n2 == n1 :
        n2 = randint(0, n_entite-1)
    # si c'est un choc AB  
    if (pac[n1] == "A" and pac[n2] == "B") or (pac[n1] == "B" and pac[n2] == "A") :
        x = random() # au hasard entre 
        if x > collision_ab :
            pac[n1], pac[n2] = "C", "D"
    return pac

NA = 1000  # nombre d'espèces A 
NB = 800    # nombre d'espèces B 
NC = 0  # nombre d'espèces C 
ND = 100  # nombre d'espèces D 
COLLISION_AB = 0.05  # facteur de collision entre A et B compris entre 0 et 1, plus il est grand moins les chocs sont efficaces
# pas de collision entre C et D
temps = 10000  # nombre d'evenements
nba, nbb, nbc, nbd = [], [], [], [] # création de liste du nombre d'espèces A, B, C et D au cours du temps
sac = creation_echantillon(NA, NB, NC, ND)  # sac une liste 
t = [0] # liste de temps qui a initialement la valeur 0
comptage_especes(sac, nba, nbb, nbc, nbd) # comptage des espèces à t = 0

for i in range(1, temps) : # a chaque unité de temps
    collision(sac, COLLISION_AB) # on envisage une collision à chaque unité de temps
    comptage_especes(sac, nba, nbb, nbc, nbd) # à chaque collision, on compte les espèces
    t.append(i) # on stocke dans une liste les différents temps

# réduction du nombre d'éléments pour alléger le tracé
K = 500
t_light =[t[i] for i in range(len(t)) if i%K == 0]
nba_light =[nba[i] for i in range(len(t)) if i%K == 0]
nbb_light =[nbb[i] for i in range(len(t)) if i%K == 0]
nbc_light =[nbc[i] for i in range(len(t)) if i%K == 0]
nbd_light =[nbd[i] for i in range(len(t)) if i%K == 0]

# affichage des courbes
plt.grid()
plt.title("Population des espèces A, B, C et D")
plt.xlabel("Nombre de Chocs")
plt.ylabel("Nombre d'entités")
plt.plot(t_light, nba_light, "r--+", label="Nombre d'espèces A") # on prépare la trace Nbre de A en fonction de t
plt.plot(t_light, nbb_light, "b--*", label="Nombre d'espèces B") # idem pour B
plt.plot(t_light, nbc_light, "g--o", label="Nombre d'espèces C") # idem pour C
plt.plot(t_light, nbd_light, "k--+", label="Nombre d'espèces D") # idem pour D
plt.legend()
plt.show()


