import random
from enum import Enum


print("Witaj w grze gdzie idziesz do przodu i wygrywasz kasę, w zależności od tego jaką skrzynkę trafisz!")
print("W tej grze możesz zrobić tylko 5 ruchów do przodu, w żadną inną stronę!")

Event = Enum('Event', ['Skrzynia', 'Pusta'])


skrzynieEvent_słownik = {
    Event.Skrzynia: 0.6,
    Event.Pusta: 0.4
}
Lista_event_key = list(skrzynieEvent_słownik.keys())
Lista_event_values = list(skrzynieEvent_słownik.values())


Kolory = Enum ('Kolory',{'Zielony': "Green",
                          'Pomarańczowy': 'Orange',
                          'Fioletowy':'Purple',
                          'Złoty': "Gold"})

Skrzynia_kolor_słownik = {
    Kolory.Zielony: 0.6,
    Kolory.Pomarańczowy: 0.25,
    Kolory.Fioletowy: 0.10,
    Kolory.Złoty: 0.05
}

skrzynie_kolory_keys = list(Skrzynia_kolor_słownik.keys())
skrzynie_kolory_values = list(Skrzynia_kolor_słownik.values())


dlugosc_gry = 5

while dlugosc_gry > 0:
    odpowiedz_gry = input("Czy chcesz iść do przodu? ")

    if odpowiedz_gry == "Y":
        print("Zobaczmy w takim razie, co dostałeś")
        wylosowany_event = random.choices(Lista_event_key, Lista_event_values)[0]
        print('Taak',wylosowany_event)

        if wylosowany_event == Event.Skrzynia:
            print("Wylosowałeś skrzynię!")
            wylosowany_kolor_skrzyni = random.choices(skrzynie_kolory_keys,skrzynie_kolory_values)[0]
            print('Kolor skrzyni to: ', wylosowany_kolor_skrzyni.value)
        elif wylosowany_event == Event.Pusta:
            print("Niestety nic nie tafiłeś!")
    else:
        print("Debilu powiedz tak, bo możemy iść tylko do przodu")
        continue


    dlugosc_gry = dlugosc_gry - 1