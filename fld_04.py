import random

pontszam:int = 0
for i in range(5):
    x:int = random.randint(10, 99)
    y:int = random.randint(10, 99)
    osz = x + y
    dif = x - y
    if dif < 0: dif *= -1
    print(f'{i+1}. kör:')
    print(f'két szám összege: {osz}, különbsége: {dif}')
    print(f'mi lehet ez a két szám?')
    xt:int = int(input('egyik szám: '))
    yt:int = int(input('másik szám: '))
    if (xt==x and yt==y) or (xt==y and yt==x):
        print('eltaláltad! :)')
        pontszam += 1
    else:
        print('sajnos nem :(')
        print(f'a válasz {x} és {y}')
print(f'végeztünk, helyes találataid száma: {pontszam}')