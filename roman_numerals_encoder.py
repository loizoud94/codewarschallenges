def solution(n):
    roman_numeral = str(millenia(n)) + str(centuries(n)) + str(decem(n)) + str(unitates(n))
    return roman_numeral

def roman_exp(n):
    thousands = n // 1000
    n000 = thousands*1000

    hundreds = (n-n000)//100
    n00 = hundreds*100

    tens = (n - n000 - n00)//10
    n0 = tens*10

    units = n - n000 - n00 - n0
    return thousands, hundreds, tens, units

def millenia(n):
    if roman_exp(n)[0] > 0:
        return (n // 1000)*'M'
    else:
        return ''

def centuries(n):
    if roman_exp(n)[1] in [1,2,3]:
        return roman_exp(n)[1]*'C'
    elif roman_exp(n)[1] == 4:
        return 'CD'
    elif roman_exp(n)[1] in [5,6,7,8]:
        return 'D' + (roman_exp(n)[1] - 5)*'C'
    elif roman_exp(n)[1] == 9:
        return 'CM'
    else:
        return ''

def decem(n):
    if roman_exp(n)[2] in [1,2,3]:
        return roman_exp(n)[2]*'X'
    elif roman_exp(n)[2] == 4:
        return 'XL'
    elif roman_exp(n)[2] in [5,6,7,8]:
        return 'L' + (roman_exp(n)[2] - 5)*'X'
    elif roman_exp(n)[2] == 9:
        return 'XC'
    else:
        return ''

def unitates(n):
    if roman_exp(n)[3] in [1,2,3]:
        return roman_exp(n)[3]*'I'
    elif roman_exp(n)[3] == 4:
        return 'IV'
    elif roman_exp(n)[3] in [5,6,7,8]:
        return 'V' + (roman_exp(n)[3] - 5)*'I'
    elif roman_exp(n)[3] == 9:
        return 'IX'
    else:
        return ''
