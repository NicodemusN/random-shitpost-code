# Käyttäjä kirjoittaa numeron ja numero muuttuu tietyn funktion mukaan, jota käyttäjä ei tiedä.
from tkinter import Y


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
            print("Oikea arvaus! Sinä ja tietokone arvasitte", karvaus, ".")
         else:
            print("Väärä arvaus. Sinä arvasit", iarvaus, "ja tietokone arvasi", karvaus)
   elif rankys == "n":
         print("Näkemiin.")

def nimi(fname, lname):
   print(fname, lname)
   fnum = len(fname)
   fnum = int(fnum)
   lnum = len(lname)
   lnum = int(lnum)
   print(fnum, "ja", lnum, "kirjainta. Yhteensä kirjaimia", lnum+fnum)
   for letter in fname:
      print(letter)

def nimi(fname, tname, lname):
   print(fname, tname, lname)
   fnum = len(fname)
   fnum = int(fnum)
   tnum = len(tname)
   tnum = int(tnum)
   lnum = len(lname)
   lnum = int(lnum)
   print(fnum, ",", tnum, "ja", lnum, "kirjainta. Yhteensä kirjaimia", lnum+tnum+fnum)
   for letter in fname:
      print(letter)

def nimi(fname, lname):
   print(fname, lname)
   fnum = len(fname)
   fnum = int(fnum)
   lnum = len(lname)
   lnum = int(lnum)
   print(fnum, "ja", lnum, "kirjainta. Yhteensä kirjaimia", +lnum+fnum)
   for letter in fname:
      print(letter)

# Laskin, jossa ei ole perustoimintoja, kuten yhteenlaskua tai kertolaskua :D
def laskin():
   import math
   mkysymys = input("Matemaattinen toimitus: [nj] neliöjuuri, [k] kertoma, [s] sini, [c] kosini, [t] tangentti, [ar] asteet radiaaneiksi, [ra] radiaanit asteiksi.")
   if mkysymys == "nj":
      njkys = input("Sijoita luku, jonka neliöjuuren haluat ratkaista: ")
      njkys = int(njkys)
      print(math.sqrt(njkys))
   elif mkysymys == "k":
      kkys = input("Sijoita luku, jonka kertoman haluat ratkaista: ")
      kkys = int(kkys)
      print(math.factorial(kkys))
   elif mkysymys == "s":
      skys = input("Sijoita luku, jonka sinin haluat ratkaista: ")
      skys = int(skys)
      print(math.sin(skys))
   elif mkysymys == "c":
      ckys = input("Sijoita luku, jonka kosinin haluat ratkaista: ")
      ckys = int(ckys)
      print(math.cos(ckys))
   elif mkysymys == "t":
      tkys = input("Sijoita lunku, jonka tangentin haluat ratkaista: ")
      tkys = int(tkys)
      print(math.tan(tkys))
   elif mkysymys == "ar":
      arkys = input("Sijoita luku, jonka haluat muuttaa asteista radiaaneiksi: ")
      arkys = int(arkys)
      print(math.radians(arkys))
   elif mkysymys == "ra":
      rakys = input("Sijoita luku, jonka haluat muuttaa radiaaneista asteiksi: ")
      rakys = int(rakys)
      print(math.degrees(rakys))

def testi():
   import math
   kkyyss = input("Numero: ")
   kkyyss = int(kkyyss)
   print(math.sqrt(kkyyss))
   
def aky():
   akysymys = input("Kirjautuminen [k], numerot [n], nimi [ni], laskin [l] vai numeroarvaus [na]?")
   if akysymys == "k":
      kirjautu()
   elif akysymys == "t":
      testi()
   elif akysymys == "n":
      numeroita()
   elif akysymys == "l":
      laskin()
   elif akysymys == "na":
      random()
   elif akysymys == "ni":
      fname = input("Etunimi: ")
      lname = input("Sukunimi: ")
      tnimi = input("Onko sinulla toinen nimi? Kyllä [y] / ei [n]")
      if tnimi == "y":
         tname = input("Toinen nimi: ")
         nimi(fname, tname, lname)
      elif tnimi == "n":
         nimi(fname, lname)
      else:
         print("Väärä kirjain, palautetaan...")
   else:
      print("Väärä kirjain, palautetaan...")

jk = input("Haluatko käyttää MemelSoftarea? Kyllä [y] / ei [n]")

while jk == "y":
   aky()
   jk = input("Haluatko jatkaa? Kyllä [y] / ei [n]")

if jk != "y":
   print("Näkemiin...")
