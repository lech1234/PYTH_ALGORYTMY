class KolejkaFIFO:

    def __init__(self, implementacja_kolejki):
        self.__kontener = implementacja_kolejki
        self.typ = implementacja_kolejki.__class__.__name__
        if self.typ == 'list':
            KolejkaFIFO.enqueue = KolejkaFIFO.__enqueue_list
        else:
            KolejkaFIFO.enqueue = KolejkaFIFO.__enqueue_deque

    def __enqueue_list(self, element):
        self.__kontener.insert(0, element)

    def __enqueue_deque(self, element):
        self.__kontener.appendleft(element)

    def enqueue(self, element):
        pass

    def dequeue(self):
        return self.__kontener.pop()

    def __str__(self):
        return str(self.__kontener)


if __name__ == '__main__':
    import time
    from collections import deque


    def test_dzialania(kolejka, liczba_elementow):
        print(f'TEST DZIAŁANIA KOLEJKI FIFO ({kolejka.typ}):')
        print('Stan początkowy kolejki:              ', kolejka)

        # dodawanie elementów
        for element in range(liczba_elementow):
            kolejka.enqueue(chr(ord('A') + element))
            print(f'Dodano   element -> zawartość kolejki:', kolejka)

        # usuwanie elementów
        for _ in range(liczba_elementow):
            kolejka.dequeue()
            print(f'Usunięto element -> zawartość kolejki:', kolejka)
        print()


    def test_wydajnosci(kolejka, liczba_operacji):
        print(f'TEST WYDAJNOŚCI KOLEJKI FIFO ({kolejka.typ}):')
        start = time.perf_counter()
        for _ in range(liczba_operacji):
            kolejka.enqueue('x')
        stop = time.perf_counter()
        print(f'Czas dodawania elementów: {stop - start:.3f}s')

        start = time.perf_counter()
        for _ in range(liczba_operacji):
            kolejka.dequeue()
        stop = time.perf_counter()
        print(f'Czas usuwania elementów:  {stop - start:.3f}s\n')


    test_dzialania(KolejkaFIFO(list()), 3)
    test_dzialania(KolejkaFIFO(deque()), 3)

    test_wydajnosci(KolejkaFIFO(list()), 200_000)
    test_wydajnosci(KolejkaFIFO(deque()), 200_000)
