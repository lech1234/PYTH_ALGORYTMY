def czy_liczba_pierwsza(liczba):
    czy_pierwsza = True
    for dzielnik in range(2, liczba):
        if liczba % dzielnik == 0:
            czy_pierwsza = False
    return czy_pierwsza


def policz_liczby_pierwsze(n):
    licznik_liczb_pierwszych = 0
    for liczba in range(2, n + 1):
        if czy_liczba_pierwsza(liczba):
            licznik_liczb_pierwszych += 1
    return licznik_liczb_pierwszych


if __name__ == '__main__':
    import time


    def zmierz_czas_obliczen(n):
        czas_start = time.perf_counter()
        licznik = policz_liczby_pierwsze(n)
        czas_stop = time.perf_counter()
        print(f'W przedziale od 2 do {n} znaleziono {licznik} liczb pierwszych')
        return czas_stop - czas_start


    # dane referencyjne
    referencyjna_liczba_danych = 2_000
    referencyjny_czas = zmierz_czas_obliczen(referencyjna_liczba_danych)

    for wielokrotnosc in range(2, 6):
        czas = zmierz_czas_obliczen(wielokrotnosc * referencyjna_liczba_danych)
        print(f'Dla {wielokrotnosc} razy dłuższych danych, '
              f'czas wykonania wzrósł {czas / referencyjny_czas:4.1f}-krotnie', end='\n\n')
