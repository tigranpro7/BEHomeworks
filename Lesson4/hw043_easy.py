# Задание-3:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить, должна возвращать либо True,
# ибо False (если счастливый и несчастливый соответственно)

def lucky_ticket(ticket_number):
    biletlist = []
    ticket_number_str = str(ticket_number)
    for elm in ticket_number_str:
        cifra = ticket_number % 10
        biletlist.append(cifra)
        ticket_number = ticket_number // 10
    print(biletlist)
    if len(biletlist) == 6:
        if biletlist[0] + biletlist[1] + biletlist[2] == biletlist[3] + biletlist[4] + biletlist[5]:
            return True
        else:
            return False
    else:
        print('Вы ввели неправильный номер билета')
    



#print(lucky_ticket(123006))
#print(lucky_ticket(12321))
#print(lucky_ticket(436751))
print(lucky_ticket(111111))

