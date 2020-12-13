def value(r):
    if(r == 'I'):
        return 1
    if(r == 'V'):
        return 5
    if(r == 'X'):
        return 10
    if(r == 'L'):
        return 50
    if(r == 'C'):
        return 100
    if(r == 'D'):
        return 500
    if(r == 'M'):
        return 1000

def romanToDecimal(str):
    result = 0
    i = 0

    while(i < len(str)):
        #Getting the value of the symbol str[i]
        s1 = value(str[i])

        if(i + 1 < len(str)):
            # Getting the value of the symbol str[i + 1]
            s2 = value(str[i + 1])

            if(s1 >= s2):
                result = result + s1
                i = i + 1
            else:
                result = result + s2 - s1
                i = i + 2
        else:
            result = result + s1
            i = i + 2
    return result

print("Decimal form from Roman is")
print(romanToDecimal("LVIII"))

















