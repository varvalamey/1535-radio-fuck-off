v = int(input())
a = int(input())
i = 1
grad = "Града не было."
while a != 0:
    if a > 20:
        grad = "Град был!"
    v -= a
    if v <= 0:
        p = i
    i += 1
    a = int(input())
if p:
    print(f'Время заполнения {p - 1} секунд.')
    print(grad)
else:
    print('Ведро не полное.')
    print(grad)