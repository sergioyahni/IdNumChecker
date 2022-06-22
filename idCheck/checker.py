def id_checker(idNumber):
    sumDigits0, sumDigits1 = 0, 0
    n, m = 1, 2

    while n <= 9:
        sumDigits0 += int(idNumber[n - 1])
        n += 2

    while m < 9:
        if int(idNumber[m - 1]) * 2 <= 9:
            sumDigits1 += int(idNumber[m - 1]) * 2
        else:
            d = str(int(idNumber[m - 1]) * 2)
            sumDigits1 += (int(d[0]) + int(d[1]))
        m += 2
    sumDigits = sumDigits0 + sumDigits1
    if sumDigits % 10 == 0:
        return True
    else:
        return False


if __name__ == '__main__':
    print(id_checker("234623944"))
