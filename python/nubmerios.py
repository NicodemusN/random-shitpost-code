# Käyttäjä kirjoittaa numeron ja numero muuttuu tietyn funktion mukaan, jota käyttäjä ei tiedä.
def numeroita():
   import time
   number = input("Annappa joku numero. Älä muute postaa negatiivisii numeroit, nollaa tai ygöstä")
   number = int(number)
   kierros = 1
   a_number = number

   if number == 2:
      print("Balls")
      time.sleep(3)
      print("Mogus")
      time.sleep(2)
      print("Joo venaas vähä hitaal käy nykyää")
      time.sleep(2)
      print("Tää on se yks numero joka on aika based")

   else:
      if number <= 2:
         print("Tais tulla tosijaa väärää inputtii")
      
      else:
         while number <= 1267650600228229401496703205376:
            print("Sinun numerosi", a_number, "ja", kierros, "kierroksen jälkeen viimeinen numero on", number)
            time.sleep(1)
            number = number ** 2
            kierros = kierros + 1
            time.sleep(1)
         print("Päättele algoritmi")

# Kirjautuminen.
def kirjautu():
   kysymys_a = input("Haluatko kirjautua sisään? [y] kyllä / [n] ei")
   if kysymys_a == "y":
      ktunnus = input("Kirjoita käyttäjätunnus:")
      if ktunnus == "admin":
         ssana = input("Kirjoita salasana:")
         if ssana == "admin":
            print("Tervetuloa!")
         else:
            print("Väärä salasana. Lopetetaan...")
      else:
         print("Kyseistä käyttäjätunnusta ei ole määritelty. Lopetetaan...")
   else:
      print("Näkemiin.")


# Käyttäjän tulee arvata tietokoneen valitsema numero oikein.
def random():
   import random

   rankys = input("Haluatko yrittää arvata randomisti valitun numeron välillä 1-10? [y] kyllä / [n] ei")
   if rankys == "y":
      iarvaus = input("Kirjoita kokonaisluku välillä 1-10")
      iarvaus = int(iarvaus)
      karvaus = random.randint(1,6)
      karvaus = int(karvaus)
      if iarvaus < 1:
         print("Väärä luku syötetty")
      if iarvaus > 10:
         print("Väärä luku syötetty")
      else:
         if iarvaus == karvaus:
            print("Oikea arvaus! Sinä ja tietokone arvasitte", karvaus, print("."))
         else:
            print("Väärä arvaus. Sinä arvasit", iarvaus, "ja tietokone arvasi", karvaus)
   elif rankys == "n":
         print("Näkemiin.")

def testi(fname, lname):
   print("testi")
   print(fname, lname)

# Kuuluu ylläolevaan testiin. Tulee aina testattaessa.
testi("Jorma", "Ollila")

akysymys = input("Kirjautuminen [k], numerot [n] vai numeroarvaus [na]?")
if akysymys == "k":
   kirjautu()
elif akysymys == "n":
   numeroita()
elif akysymys == "na":
   random()
elif akysymys == "t":
   testi()
else:
   print("Väärä kirjain, palautetaan...")
