import random as rnd

_lista_unikalnych_wartosci = rnd.sample(range(100), 21)

nieistniejaca_wartosc = _lista_unikalnych_wartosci.pop()
istniejaca_wartosc = _lista_unikalnych_wartosci[0]
lista_posortowana = sorted(_lista_unikalnych_wartosci)

if __name__ == '__main__':
    print('lista unikalnych wartości :', lista_posortowana)
    print('istniejąca wartość        :', istniejaca_wartosc)
    print('nieistniejąca wartość     :', nieistniejaca_wartosc)
