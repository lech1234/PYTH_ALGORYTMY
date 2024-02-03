import time

metody_pomiaru_czasu = (time.monotonic,
                        time.perf_counter,
                        time.process_time,
                        time.thread_time,
                        time.time)

print('METODA          CZAS WYKONANIA')
for zmierz_czas in metody_pomiaru_czasu:
    czas_start = zmierz_czas()
    time.sleep(1)  # uśpienie na 1 sekundę
    czas_stop = zmierz_czas()
    print(f'{zmierz_czas.__name__:15} {czas_stop - czas_start:.5f} s')
