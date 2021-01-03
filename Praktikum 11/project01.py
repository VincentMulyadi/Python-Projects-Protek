from datetime import *

def diffDate(x):
    x = x.split('-')
    year = int(x[0])
    month = int(x[1])
    day = int(x[2])
    date_given = datetime(year, month, day)
    date_now = datetime.now()
    selisih = date_now - date_given
    return selisih.days
