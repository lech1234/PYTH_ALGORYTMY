from pathlib import Path


def galaz(typ_galezi):
    """
    Funkcja pomocnicza zwracająca znaki, które trzeba narysować kontynuując gałąź.

    :param typ_galezi: jeden z poniższych znaków:
                       ' ' - spacja - gałąź już zakończona, więc poniżej musi być spacja
                       'I' - pionowa kreska - kontynuujemy rysowanie gałęzi, ale na razie bez odgałęzień
                       'T' - pionowa kreska z poziomym odgałęzieniem (przewrócona litera T)
                             gałąź niezakończona, ale ma poziome odgałęzienie
                       'L' - kończymy galąź, rysując ostatnie odgałęzienie (przypomina literę L)
    :return: znaki kontynuacji gałęzi w wierszu poniżej
    """
    # symbole graficzne do rysowania gałęzi
    spacja = ' '  # spacja
    __symbol = chr(9472)  # ─
    i_symbol = chr(9474)  # │
    l_symbol = chr(9492)  # └
    t_symbol = chr(9500)  # ├

    # zwraca 4 symbole tworzące kawałek gałęzi
    match typ_galezi:
        case ' ':  # zwraca '    '
            return spacja * 4
        case 'I':  # zwraca '│   '
            return i_symbol + spacja * 3
        case 'T':  # zwraca '├── '
            return t_symbol + __symbol * 2 + spacja
        case 'L':  # zwraca '└── '
            return l_symbol + __symbol * 2 + spacja
        case _:  # zwraca pusty string, gdy parametr błędny
            return ''


def drzewo_katalogu(sciezka_startowa: Path, prefiks: str = ''):
    """
    Funkcja rysuje drzewo zawartości katalogu.

    :param sciezka_startowa: katalog startowy
    :param prefiks: początkowe wcięcie (zwykle pusty string)
    :return: None
    """
    # lista elementów katalogu
    zawartosc_katalogu = list(sciezka_startowa.iterdir())
    # dla każdego elementu katalogu tworzymy poprzedzającą gałąź (dla wszystkich - T, dla ostatniego - L)
    poprzedniki = [galaz('T')] * (len(zawartosc_katalogu) - 1) + [galaz('L')]
    # kojarzymy gałęzie z elementami katalogu
    for poprzednik, sciezka in zip(poprzedniki, zawartosc_katalogu):
        print(prefiks + poprzednik + sciezka.name)
        if sciezka.is_dir():  # jeśli element jest podkatalogiem
            # jeśli poprzednią gałęzią powyżej było 'T', to teraz 'I'
            # jeśli poprzednią gałęzią powyżej było 'L', to teraz ' '
            rozszerzenie_prefiksu = galaz('I') if poprzednik == galaz('T') else galaz(' ')
            # wywołujemy rekurencyjnie funkcję
            drzewo_katalogu(sciezka, prefiks=prefiks + rozszerzenie_prefiksu)


if __name__ == '__main__':
    # ścieżka do katalogu startowego
    drzewo_katalogu(Path.home() / 'PycharmProjects' / 'CDV' / 'PYTH_ALGORYTMY')
