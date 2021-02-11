# module
import math 
 

# Выбор
f = float(input('T-kreklu skaits: '))
v = input('Printa izvēle (TEKSTS, ZIME, FOTO) ')

def fut():
    global f
    f = math.ceil(f)

fut()
# Цены
if v == 'TEKSTS':
    v = 5 

elif v == 'ZIME':
    v = 7

elif v == 'FOTO':
    v = 20 

else: 
    print('Nederīgs arguments. Pupiņu proporcijas un sadalījums. Jāpieprasa lielie burti.')
# Скидки
f1 = f * v

if f1 < 50:
    f2 = f1 + 15
    print('Pasūtījums maksā: ' + str(f2) + ' EUR')

elif f1 >= 100:
    f3 = f1 - (f1 * 5 / 100) 
    print('Pasūtījums maksā: ' + str(f3) + ' EUR')

elif f1 >= 50:
    print('Pasūtījums maksā: ' + str(f1) + ' EUR')