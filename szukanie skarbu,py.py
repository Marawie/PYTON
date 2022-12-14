import random
from collections import Counter
'''
print("Liczba która wylosujesz, będzie Twoją wypłatą")
skarby = input("Czy chcesz otworzyć skrzynkę? Y/N")

skarby = skarby.capitalize()
def gra(skarby):
    if (skarby == "Y"):
        skarb = random.uniform(1,100)
        print("Oto Twoja nagroda! ", skarb , "PLN")
    else:
        return "Debil"
# Tu coś nie działa, ale idę spać zobacze to jutro
'''



# Czy broń trafi człowieka

def strzał (jaki_jest_procent_szansy_ze_trafi):
    czy_strzał_trafi = random.uniform(0,100)
    if czy_strzał_trafi < jaki_jest_procent_szansy_ze_trafi:
        return "DOSTAŁEŚ!"
    else:
        return "FARCIARZU, OBOK CIEBIE!"
print(strzał(1))





x = 0
liczba_trafien = []
while x < 100:
    x = x + 1
liczba_trafien.append(strzał(50),)
print(słownikowe_strzały)

