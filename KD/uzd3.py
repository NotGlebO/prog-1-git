import math

p = float(input("Ievadiet podestu skaitu: ")) 
a = float(input("Ievadiet pjedestāla platuma apgabalu (cm): "))
b = float(input("Ievadiet pjedestāla garuma apgabalu(cm): "))
h = float(input("Ievadiet pjedestāla augstumu(cm): "))

def skr():
    global p
    p = math.ceil(p)

skr()

o = a * b #lapas
b1 = h * b 
b2 = h * a

pl1 = 4 * a #Sloknes 
pl2 = 4 * b
pl3 = 4 * h
#daudzums
pl = 2 * p #lapas
s = 4 * p #sloknes
st = 8 * p # stūra
print("Jums vajag " + str(pl) + " lapas par : " + str(o) + "cm,  " + str(b1) + "cm,  " + str(b2) + "cm")
print("Jums vajag " + str(s)  + " sloksnes par: " + str(pl1) + "cm, " + str(pl2) + "cm, "+ str(pl3) + "cm") 
print("Jums vajag " + str(st) + " stūra savienojumiem.")
