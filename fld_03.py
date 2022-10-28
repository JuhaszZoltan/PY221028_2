print('add meg a tanuló következő adatait: ')
nev:str = input('név: ')
maxp:int = int(input('maximális pontszám: '))
elertp:int = int(input('elért pontszám: '))

if elertp > maxp:
    print('hibás adatokat adtál meg.')
    print('az elért pontszám nem lehet nagyobb, mint a maximális!')
else:
    szazalek = elertp / maxp * 100
    osztalyzat = '-'
    if   szazalek < 51: osztalyzat = 'elégtelen'
    elif szazalek < 65: osztalyzat = 'elégséges'
    elif szazalek < 77: osztalyzat = 'közepes'
    elif szazalek < 90: osztalyzat = 'jó'
    else:               osztalyzat = 'jeles'
    print(f'{nev} {round(szazalek, 2)}%-ot ért el, osztályzata: {osztalyzat}')