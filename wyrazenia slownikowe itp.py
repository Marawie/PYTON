#Znajdz liczby tylko parzyste i dodaj je


liczby = [4,23,1,7,9,12]
imiona = ["Heniek","Andrzej","Radek","Roman"]
słowniki = { "Jurek": 23, "Andrzej:": 33, "Marek": 25}


def sum_liczby():
    suma = 0
    [liczba for liczba in liczby if (liczba % 2 == 0)]
    suma += liczba
    return



names_lenght = { imie : len(imie) for imie in imiona}
print(names_lenght)

mnozenie_liczb = { value: value* value for value in liczby}
print(mnozenie_liczb)


names_lenght = { imie : len(imie) for imie in imiona if (imie.startswith("R"))}
print(names_lenght)


słownik = {key:key.upper() for key,age in słowniki.items()}
print(słownik)


# wyszukaj liczby podzielne przez 7 ale niepodzielnych przez 5

liczby_podzielne = [liczby for liczby in range(100,360) if(liczby % 7 ==0) if(liczby % 5 != 0)]
print(liczby_podzielne)






