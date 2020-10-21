from datetime import datetime as dt
from zoneinfo import ZoneInfo as zi

# Imprime la hora actual en su zona horaria
current_time = dt.now()
print(current_time)

# Imprime la hora actual en cualquier zona horaria
current_time_berlin = dt.now(zi("Europe/Berlin"))
print(current_time_berlin)

"""
Salida

2020-10-20 19:19:01.081683
2020-10-21 02:19:01.082124+02:00
"""