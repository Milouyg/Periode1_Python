2 + 2
3 * 10
100 - 10
25 / 5
10 / 3
10 // 3

#Namen
print("Mijn naam is <Jouw naam hier>")
naam = "Milou"
print(naam)
print(naam.upper())
print(naam[0:2])
print(naam[::-1])

leeftijd = 19
print("Hallo " + naam + " ben je al " + str(leeftijd) + " jaar?")
leeftijd = leeftijd + 1
leeftijd
leeftijd-=1 
leeftijd

if leeftijd < 18:
    hoelang_tot18jaar = 18 - leeftijd
    print("Over " + str(hoelang_tot18jaar) + "jaar wordt je 18")
elif leeftijd > 18:
    hoelang_al18jaar = leeftijd - 18
    print("Het is alweer " + str(hoelang_al18jaar) + "jaar geleden dat je 18 werd ;-)")
else:
    print("Je bent precies" +str(leeftijd) + "jaar")

#Willekeurige getallen
from random import randint
randint(0,1000)
willekeurig_getal = randint(0,1000)
willekeurig_getal
print("Willekeurig getal tussen 0 en 1000 = " + str(willekeurig_getal))

#datum en tijd
from datetime import datetime
datum = datetime.now()
print(datum)
datum.strftime('%A %d %B %Y') 

import locale
locale.setlocale(locale.LC_TIME, 'nl_NL')
datum.strftime('%A %d %B %Y')
locale.setlocale(locale.LC_TIME, 'it_IT')
datum.strftime('%A %d %B %Y')

