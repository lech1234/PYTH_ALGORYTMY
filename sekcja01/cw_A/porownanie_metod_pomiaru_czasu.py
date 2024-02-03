import time

"""
Porównanie metod pomiaru czasu
"""

print('{:15}{:13}{:12}{:14}{:12}'.format('CLOCK', 'ADJUSTABLE', 'MONOTONIC', 'RESOLUTION', 'CLOCK TICKS'))
print('-' * 65)
for zegar in 'monotonic', 'perf_counter', 'process_time', 'thread_time', 'time':
    info = time.get_clock_info(zegar)
    print(f'{zegar:15}'
          f'{str(info.adjustable):13}'
          f'{str(info.monotonic):12}'
          f'{info.resolution:11.9f}'
          f'{int(1 // info.resolution):14}')
