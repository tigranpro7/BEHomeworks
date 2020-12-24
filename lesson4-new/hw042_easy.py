# Задание-2:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.
def my_round(number, ndigits):
    digits = 0
    strnumber = str(number)
    end_round = ''
    str_my_round = str(number)
    for elm in str_my_round:
        digits = digits + 1
        if elm == '.':
            break

    ndigit_prav = ndigits + digits
    str_number_prav = str_my_round[:ndigit_prav]
   # print(str_number_prav)

    int_digit = float(str_number_prav)
    int_digit_bez_zap = int_digit*(10**ndigits)
    
    if int_digit_bez_zap % 10 < 5:
        pass
    else:
        int_digit_bez_zap = int_digit_bez_zap +10

    int_digit_bez_zap_kon = int_digit_bez_zap // 10
   # print(int_digit_bez_zap)
    end_round = int_digit_bez_zap_kon/(10**(ndigits-1))

   # if int_digit < 5:
   #     end_round = strnumber[:ndigits]
     #   pass
   # else:
   #     end_round = strnumber[:ndigits-1] + str(float(strnumber[ndigits]) + 1)
    return end_round


print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))
print(my_round(0.6, 1))
print(my_round(0.4, 1))

