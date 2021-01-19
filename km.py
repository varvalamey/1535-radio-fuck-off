N = int(input())
summa = 0 # накапливаем сумму
cnt = 0 # накапливаем количество чисел
d = 0 # текущая степень десятки = количество цифр в числах
while True:
    d += 1 
    summa += .9 * 10 ** d * d # например, для двузначных: 90 чисел, в них 90 * 2 цифр
    if summa > N: # остановиться, этот разряд уже целиком не прибавляем
        break
    cnt += .9 * 10 ** d # добавить в счет все d-разрядные числа
summa -= .9 * 10 ** d * d # вычитаем последнее слагаемое из суммы
cnt += (N - summa) / d # вычитаем накопленную сумму, находим, сколько не хватает чисел текущей разрядности
print(cnt)


















'''   
n = int(input())
result = 0
degree = 0  # степень 10
digits = 1  # количество цифр в числе
while True:
    if n < 9 * digits * 10 ** degree:
        result += n // digits
        break
    else:
        n -= 9 * (10 ** degree) * digits
        result += 9 * (10 ** degree)
        degree += 1
        digits += 1
print(result)
'''