from calendar import month
from datetime import *
from tkinter import ROUND #импорт
tana=date.today()
print(f"Tere! Täna on {tana}")
tana1 = tana.strftime("%d/%m/%Y")
print(f"Tere! Täna on {tana1}")
# 27/12/2022
#tana = tana.strftime("%d/%m/%Y")

# December 27, 2022
#tana = tana.strftime("%B %d, %Y")

# 12/27/22
#tana = tana.strftime("%m/%d/%y")

# Dec-27-2022
#tana = tana.strftime("%b-%d-%Y")
from calendar import *
paevadekogus=monthrange(2025,1)[1]
print(f"jaanuaris on {paevadekogus} päeva")     
#после функции стоят ()!!
paevad=tana.day
print(paevad)
onjaanyd=paevadekogus-paevad
print(f"jaanuaris on jaanud {onjaanyd} päeva")
aastalopuni=365-monthrange(2025,1)[1]+onjaanyd
print(f"aasta lopuni on jaanud {aastalopuni} paeva")

# Algne tehe
tulemus1 = 3 + 8 / (4 - 2) * 4
# Ilma sulgudeta
tulemus2 = 3 + 8 / 4 - 2 * 4
# Sulgud ümber 8 / 4
tulemus3 = 3 + (8 / 4) - 2 * 4
# Sulgud ümber 3 + 8
tulemus4 = (3 + 8) / 4 - 2 * 4
# Sulgud ümber 4 - 2
tulemus5 = 3 + 8 / 4 - (2 * 4)

print("Algne tehe (3 + 8 / (4 - 2) * 4):", tulemus1)
print("Ilma sulgudeta (3 + 8 / 4 - 2 * 4):", tulemus2)
print("Sulgud ümber 8 / 4 (3 + (8 / 4) - 2 * 4):", tulemus3)
print("Sulgud ümber 3 + 8 ((3 + 8) / 4 - 2 * 4):", tulemus4)
print("Sulgud ümber 4 - 2 (3 + 8 / 4 - (2 * 4)):", tulemus5)

print("▒▒▒▒▒▄██████████▄▒▒▒▒▒")
print("▒▒▒▄██████████████▄▒▒▒")
print("▒▒██████████████████▒▒")
print("▒▐███▀▀▀▀▀██▀▀▀▀▀███▌▒")
print("▒███▒▒▌■▐▒▒▒▒▌■▐▒▒███▒")
print("▒▐██▄▒▀▀▀▒▒▒▒▀▀▀▒▄██▌▒")
print("▒▒▀████▒▄▄▒▒▄▄▒████▀▒▒")
print("▒▒▐███▒▒▒▀▒▒▀▒▒▒███▌▒▒")
print("▒▒███▒▒▒▒▒▒▒▒▒▒▒▒███▒▒")
print("▒▒▒██▒▒▀▀▀▀▀▀▀▀▒▒██▒▒▒")
print("▒▒▒▐██▄▒▒▒▒▒▒▒▒▄██▌▒▒▒")
print("▒▒▒▒▀████████████▀▒▒▒▒")

from math import *
#try:
  #  R=float(input("R: "))
   # Sruudu=round((2*R)**2,2)
  #  Sringi=round(pi*R**2,2)
  #  Pruudu=round(8*R,2)
  #  Pringi=round(2*pi*R,2)
  #  print(f"Vastus:\nRuudu pindala on {Sruudu}, ruudu umbermoot on {Pruudu}, \nringi pindala on {Sringi}, ringi umbermoot on {Pringi}."
   #       print()
#except:
 #   print("sisesta ujukomaarvud")

d=2.575 #mundi d sm
maaR=6378 #maa radius km
maaR*=100000 #maa radius sm
Pmaa=2*pi*maaR #maa umbermoot
kogus=Pmaa/d
print(f"Meil on vaja {int(kogus):,d} mündi")
print(f"Meil on vaja {int(kogus*2):,d} euro")

a="kill-koll ".capitalize()
b="killadi-koll ".capitalize()
print(a*2,b,a*2,b,a*4)

# Laulusõnad
laulusonad = """
Rong see sõitis tsuhh tsuhh tsuhh,
piilupart oli rongijuht.
Rattad tegid rat tat taa,
rat tat taa ja tat tat taa.
Aga seal rongi peal,
kas sa tead, kes olid seal?

Rong see sõitis tuut tuut tuut,
piilupart oli rongijuht.
Rattad tegid kill koll koll,
kill koll koll ja kill koll kill.
"""

# Muuda tekst suurteks tähtedeks
suured_tahed = laulusonad.upper()

# Väljasta tekst
print(suured_tahed)

#ulesanne 8


