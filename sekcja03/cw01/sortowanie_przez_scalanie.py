def _scal_posortowane(scalona_tablica, lewa_tablica, prawa_tablica):
    """
    Funkcja pomocnicza scalająca dwie posortowane tablice.

    :param scalona_tablica: docelowo posortowana tablica zawierająca elementy z obu tablic: "lewej" i "prawej"
    :param lewa_tablica: posortowana tablica
    :param prawa_tablica: posortowana tablica
    :return: None
    """
    lewy_indeks = prawy_indeks = indeks = 0

    while lewy_indeks < len(lewa_tablica) and prawy_indeks < len(prawa_tablica):
        if lewa_tablica[lewy_indeks] <= prawa_tablica[prawy_indeks]:
            scalona_tablica[indeks] = lewa_tablica[lewy_indeks]
            lewy_indeks += 1
        else:
            scalona_tablica[indeks] = prawa_tablica[prawy_indeks]
            prawy_indeks += 1
        indeks += 1

    while lewy_indeks < len(lewa_tablica):
        scalona_tablica[indeks] = lewa_tablica[lewy_indeks]
        lewy_indeks += 1
        indeks += 1

    while prawy_indeks < len(prawa_tablica):
        scalona_tablica[indeks] = prawa_tablica[prawy_indeks]
        prawy_indeks += 1
        indeks += 1


def sortuj_przez_scalanie(dane):
    """
    Funkcja jest implementacją algorytmu sortowania przez scalanie (merge sort)
    :param dane: tablica do posortowania
    :return: None
    """
    if len(dane) > 1:
        srodek = len(dane) // 2
        lewa_polowa = dane[:srodek]
        prawa_polowa = dane[srodek:]

        sortuj_przez_scalanie(lewa_polowa)
        sortuj_przez_scalanie(prawa_polowa)
        _scal_posortowane(dane, lewa_polowa, prawa_polowa)


if __name__ == '__main__':
    from generator_danych import *

    print('LISTA NIEUPORZĄDKOWANA:', lista_unikalnych_wartosci)
    sortuj_przez_scalanie(lista_unikalnych_wartosci)
    print('LISTA POSORTOWANA     :', lista_unikalnych_wartosci)
