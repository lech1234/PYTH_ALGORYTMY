"""
Algorytm rekurencyjny sumujący kolejne liczby.
"""


def suma_do(stop):
    """
    Funkcja sumuje kolejne liczby całkowite począwszy od 0.

    :param stop: ostatni składnik sumy
    :return: suma od 0 do stop
    """
    return 0 if stop == 0 else suma_do(stop - 1) + stop


if __name__ == '__main__':

    import sys


    def test_sumy_do(stop):
        try:
            print(f'1 + 2 + ... + {stop:4d} = ', end='')
            print(suma_do(stop))
        except:
            ec, ex, tb = sys.exc_info()
            print(f'?\n{ec.__name__}: {ex}')


    # sys.setrecursionlimit(1100)
    print('ALGORYTM REKURENCYJNY:')
    test_sumy_do(100)
    test_sumy_do(1_000)
