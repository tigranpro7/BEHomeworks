# Задание-2: Дата задана в виде строки формата 'dd.mm.yyyy'.
# Проверить, корректно ли введена дата.
# Условия корректности:
# 1. День должен приводиться к целому числу в диапазоне от 1 до 30(31)
#  (в зависимости от месяца, февраль не учитываем)
# 2. Месяц должен приводиться к целому числу в диапазоне от 1 до 12
# 3. Год должен приводиться к целому положительному числу в диапазоне от 1 до 9999
# 4. Длина исходной строки для частей должна быть в соответствии с форматом 
#  (т.е. 2 символа для дня, 2 - для месяца, 4 - для года)


date = '31.11.3444'

pol_tochki = date.index('.')
pol_tochki2 = date[::-1].index('.')
mes = date[pol_tochki+1:-pol_tochki2-1]
den = date[:pol_tochki]
god = date[-pol_tochki2:]
print(den)
print(mes)
print(god)
correct = 0
try:  
    int(god)
    if int(god) in range(10000):
        correct = 0
    else:
        correct = 1
except ValueError:  
    print("Неправильно введен год" )
    correct = 1
if god in range(1,10):
    god = '000'+str(god)
if god in range(10,100):
    god = '00'+str(god)
if god in range(100,1000):
    god = '0'+str(god)


denkor = []
for elm in range(1,32):
    if elm < 10:
        elm = '0' + str(elm)
        denkor.append(elm)
    else:
        elm = str(elm)
        denkor.append(elm)
mesmal = ['02', '04', '06', '09', '11']
mesbol = ['01', '03', '05', '07', '08', '10', '12']
if mesbol.count(mes) == 1:
    denkorect = denkor
else:
    denkorect = denkor[:30]
if denkorect.count(den) == 1:
    correct = correct
else:
    correct = 1
if (mesmal + mesbol).count(mes) == 1:
    correct = correct
else:
    correct = 1
if len(date) == 10:
    if correct == 0:
        print('Дата корректна')
    else:
        print('Дата не корректна')
else:
        print('Дата не корректна')
