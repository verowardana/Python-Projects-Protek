# Soal 1
import datetime

from datetime import *

def diffDate(x):
    when = datetime.date(datetime.strptime(x,'%Y-%m-%d'))
    now = datetime.date(datetime.now())
    selisih = (now - when).days
    if selisih >= 0:
        return selisih
    if selisih < 0:
        return selisih*-1
