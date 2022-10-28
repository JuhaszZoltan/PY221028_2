a:int = int(input('háromszög "a" oldalának hossza (cm): '))
b:int = int(input('háromszög "b" oldalának hossza (cm): '))
c:int = int(input('háromszög "c" oldalának hossza (cm): '))

if a+b<=c or a+c<=b or b+c<=a:
    print('nincs ilyen háromszög :(')
else:
    s = (a+b+c) / 2
    t = (s*(s-a)*(s-b)*(s-c)) ** .5
    print(f'a háromszög területe: {round(t, 2)} cm^2')