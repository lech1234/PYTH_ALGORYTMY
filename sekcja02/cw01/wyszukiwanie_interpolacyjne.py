def wyszukiwanie_interpolacyjne(dane, szukana_wartosc):
    """
    Funkcja wyszukuje pozycję podanej wartości w sekwencji za pomocą algorytmu wyszukiwania interpolacyjnego.

    :param dane: posortowana sekwencja unikalnych wartości
    :param szukana_wartosc: szukana wartość
    :return: indeks pozycji na której została znaleziona wartość, w przeciwnym razie -1
    """
    start = 0
    koniec = len(dane) - 1
    while start < koniec:
        srodek = (start + (koniec - start) * (szukana_wartosc - dane[start]) //
                  (dane[koniec] - dane[start]))
        if srodek < start or srodek > koniec:
            return -1
        if szukana_wartosc < dane[srodek]:
            koniec = srodek - 1
        elif szukana_wartosc > dane[srodek]:
            start = srodek + 1
        else:
            return srodek
    return -1


if __name__ == '__main__':
    from generator_danych import *

    print('UPORZĄDKOWANA LISTA ELEMENTÓW:', lista_posortowana)

    pozycja_istniejacego = wyszukiwanie_interpolacyjne(lista_posortowana, istniejaca_wartosc)
    pozycja_brakujacego = wyszukiwanie_interpolacyjne(lista_posortowana, nieistniejaca_wartosc)

    print(f'Wynik szukania elementu {istniejaca_wartosc:2d}: {pozycja_istniejacego:2d}')
    print(f'Wynik szukania elementu {nieistniejaca_wartosc}: {pozycja_brakujacego:2d}')
