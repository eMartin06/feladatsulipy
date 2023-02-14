import random

randomszam=random.randint(1,3)

szam=int(input('Kérek egy számot 1 és 3 között. '))

if randomszam == szam:
    print(f'A szám meg egyezik a én számommal, Tiéd: {szam} Enyém: {randomszam}.')
    
elif randomszam > szam:
    print(f'Egyel nagyobb a számom! Tiéd {szam}, Enyém{randomszam}.')
    
else:
    print(f'Eggyel kisebb a számom! Tiéd: {szam}, Enyém: {randomszam}.')
    