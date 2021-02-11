# Модуль
import math

# Значения
cena = 2.50
platums_t = float(input('Ievadīt telpas platumu(Metros): ')) 
garums_t = float(input('Ievadīt telpas garumu (Metros): '))


# Округление
def mozg():
    global platums_t
    platums_t = math.ceil(platums_t)
mozg()

def f():
    global garums_t
    garums_t = math.ceil(garums_t)
f()

# Решение

izmers = garums_t * platums_t # Площадь комнаты

l_c = izmers * cena # Цена всего рулона

print(str(l_c) + (' EUR ')+ str(izmers) + (' m^2'))