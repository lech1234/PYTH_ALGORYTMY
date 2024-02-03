"""
Algorytm nierekurencyjny sumujący kolejne liczby.
"""


def suma_do(stop):
    """
    Funkcja sumuje kolejne liczby całkowite począwszy od 0.

    :param stop: ostatni składnik sumy
    :return: suma od 0 do stop
    """
    n = stop
    acc = 0
    while n > 0:
        acc += n
        n -= 1
    return acc


if __name__ == '__main__':
    import sys


    def test_sumy_do(stop):
        try:
            print(f'1 + 2 + ... + {stop:4d} = ', end='')
            print(suma_do(stop))
        except:
            ec, ex, tb = sys.exc_info()
            print(f'?\n{ec.__name__}: {ex}')


    print('ALGORYTM NIEREKURENCYJNY:')
    test_sumy_do(100)
    test_sumy_do(1_000)
