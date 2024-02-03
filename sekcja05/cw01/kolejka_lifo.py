class KolejkaLIFO:

    def __init__(self, implementacja_kolejki):
        self.__kontener = implementacja_kolejki
        self.typ = implementacja_kolejki.__class__.__name__

    def push(self, element):
        self.__kontener.append(element)

    def pop(self):
        return self.__kontener.pop()

    def __str__(self):
        return str(self.__kontener)


if __name__ == '__main__':
    import time
    from collections import deque


    def test_dzialania(kolejka, liczba_elementow):
        print(f'TEST DZIAŁANIA KOLEJKI LIFO ({kolejka.typ}):')
        print('Stan początkowy kolejki:              ', kolejka)

        # dodawanie elementów
        for element in range(liczba_elementow):
            kolejka.push(chr(ord('A') + element))
            print(f'Dodano   element -> zawartość kolejki:', kolejka)

        # usuwanie elementów
        for _ in range(liczba_elementow):
            element = kolejka.pop()
            print(f'Usunięto element -> zawartość kolejki:', kolejka)
        print()


    def test_wydajnosci(kolejka, liczba_operacji):
        print(f'TEST WYDAJNOŚCI KOLEJKI LIFO ({kolejka.typ}):')
        czas_start = time.perf_counter()
        for _ in range(liczba_operacji):
            kolejka.push('x')
        czas_stop = time.perf_counter()
        print(f'Czas dodawania elementów: {czas_stop - czas_start:.3f}s')

        czas_start = time.perf_counter()
        for _ in range(liczba_operacji):
            kolejka.pop()
        czas_stop = time.perf_counter()
        print(f'Czas usuwania elementów:  {czas_stop - czas_start:.3f}s\n')


    test_dzialania(KolejkaLIFO(list()), 3)
    test_dzialania(KolejkaLIFO(deque()), 3)

    test_wydajnosci(KolejkaLIFO(list()), 200_000)
    test_wydajnosci(KolejkaLIFO(deque()), 200_000)
