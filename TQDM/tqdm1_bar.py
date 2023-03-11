import pandas as pd
import numpy as np
from time import sleep
from tqdm import tqdm, trange

dogs = np.random.choice(['labradoodle','beagle','mutt'], size = 50_000)
smell = np.random.randint(0, 100, size=50_000)
df = pd.DataFrame(data=np.array([dogs,smell]).T,
                  columns=['dog','smell'])

print(df.head())
print(len(df))

#TQDM
# for dog in dogs:
    # sleep(0.5)
    #ici le prog tourne mais on ne connait pas la fin
print("\non ne voit pas la progression")
for dog in dogs:
    sleep(0.000001)
    #ici le prog tourne mais on ne connait pas la fin

print("\nbarre de progression pour voir le déroulé")
for dog in tqdm(dogs):
    sleep(0.000001)
    #ici le prog tourne mais une barre de progression



#autre cas
print("\ncas sans barre")
for i in range(50):
    sleep(0.1)
print('done1')

print("\ncas avec barre")
for i in trange(50):
    sleep(0.1)
print('done2')


#si on ne connait pas la taille du dataframe ou autre bloc
print("\ntaille du dataframe inconnue")
for dog in tqdm(dogs, total=50_001):
    sleep(0.00001)

#autre technique 
print("\nutilisation de l'objet pbar")
pbar = tqdm(total = 50_000)
for s in smell:
    pbar.update(1)
    sleep(0.00001)
pbar.close()

#description et unité
print("\ndescription nom barre/compteurs et unité")
for dog in tqdm(dogs, desc='compteur de chien', unit='chien'):
    sleep(0.00001)


#plusieurs barres 
print("\nplusieurs barres et sous barres")
for dog in tqdm(dogs[:5], desc='dog counter', total=5):
    for s in tqdm(smell[:2], desc='smell counter', total=2):
        sleep(0.1)


#description dynamique
print("\ndescription dynamique")
pbar = tqdm(dogs[:10])
for dog in pbar:
    sleep(0.5)
    pbar.set_description(f'Processing {dog}')


#controle de la taille de la barre
print("\ntrès petite barre 5 le % reste seul")
for i in tqdm(range(9999999), ncols=5):
    pass

print("\npetite barre 55")
for i in tqdm(range(9999999), ncols=55):
    pass

print("\ngrande barre 100")
for i in tqdm(range(9999999), ncols=100):
    pass

print("\ntrès grande barre 200")
for i in tqdm(range(9999999), ncols=200):
    pass

print("\nsans ncols")
for i in tqdm(range(9999999)):
    pass

#configuration des intervalles
print("\nupdate toutes les secondes (par defaut 0.1sec)")
for dog in tqdm(dogs, mininterval=1):
    sleep(0.00001)


#enable/disable progressbar
print("\nprogressbar activée")
debug = True
for s in tqdm(smell, disable = not debug):
    sleep(0.00001)

print("\nprogressbar désactivée")
debug = False
for s in tqdm(smell, disable = not debug):
    sleep(0.00001)

#TQDM et Pandas
tqdm.pandas(desc='dog bar')

df.progress_apply(lambda row: (row['smell'])**2, axis=1)