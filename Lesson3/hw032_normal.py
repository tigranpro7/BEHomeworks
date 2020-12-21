# Задача-2: Дана дата в формате dd.mm.yyyy, например: 02.11.2013.
# Ваша задача вывести дату в текстовом виде, например: второе ноября 2013 года.
# Склонением пренебречь (2000 года, 2010 года)



den = list in range(1,32)
denlist = []
denk = ['первое', 'второе', 'третье', 'четвертое', 'пятое', 'шестое', 'седьмое', 'восьмое', 'девятое', 'десятое', 'одиннадцатое', 'двенадцатое', 'тринадцатое', 'четырнадцатое', 'пятнадцатое', 'шестнадцатое', 'семнадцатое', 'восемнадцатое', 'девятнадцатое', 'двадцатое', 'двадцать первое', 'двадцать второе', 'двадцать третье', 'двадцать четвертое', 'двадцать пятое', 'двадцать шестое', 'двадцать седьмое', 'двадцать восьмое', 'двадцать девятое', 'тридцатое', 'тридцать первое']
for den in range(1,32):
    if den < 10:
        den = '0' + str(den)
        denlist.append(den)
    else:
        den = str(den)
        denlist.append(den)
denslovar = dict(zip(denlist, denk))
mes = denlist[0:12]

mesk = ['января', 'февраля', 'марта', 'апреля', 'мая', 'июня', 'июля', 'августа', 'сентября', 'октября', 'ноября', 'декабря']
messlovar = dict(zip(mes, mesk))
vvod = input('Введите дату в формте dd.mm.yyyy: ')
vvodden = (vvod[0:2])
vvodmes = (vvod[3:5])
vvodgod = (vvod[6:10])
tekdate = []
for denv in denslovar.keys():
    if denv == vvodden:
        tekdate.append(denslovar.get(denv))
for mesv in messlovar.keys():
    if mesv == vvodmes:
        tekdate.append(messlovar.get(mesv))
print(tekdate[0], tekdate[1], vvodgod, 'года')

