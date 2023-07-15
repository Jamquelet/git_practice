from collections import defaultdict

def checkMagazine(magazine, note):
    n_mag= defaultdict(int) #valor numero del entero es nulo
    n_note = defaultdict(int) 

    for w in magazine:
        n_mag[w] += 1

    for w in note:
        n_note[w] += 1
    
    bandera = True
    for w in n_note:
        if n_mag[w] < n_note[w]:
            bandera = False
            break

    print("YES" if bandera else "NO")