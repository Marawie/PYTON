definicje = {}
while (True):



   print("1: Stwórz definicje")
   print("2: Znajdź definicje")
   print("3: Usuń definicje")
   print("4: Zakończ program")

   wybor = input("Co chcesz zrobić?")

   if wybor == "1":
      klucz = input("Podaj słowo do zdefiniowania: ")
      definicja = input("Podaj definicje: ")
      definicje[klucz] = definicja
      print("Wszystko poszło zgodnie z planem! Dodałeś nowe zdefiniowane słowo!")

   elif wybor == "2":
      klucz = input("Czego szukasz?")
      if klucz in definicje:
         print(definicje[klucz])
      else:
         print("Nie znaleziono definicji o nazwie", klucz)

   elif wybor == "3":
      klucz = input("Jaką definicję chcesz usunąć?")
   if klucz in definicje:
      del definicje[klucz]
      print("Klucz został usunięty", klucz)
   else:
      print("Nie znaleziono takiego klucza")

   if wybor == "4":
      print("Narazie!")
      break

















