n = int(input())
i = 1
strock = 1
greben = 2
top = False
k = 1
while strock > 0:
    print(i, end=" ")
    if strock < greben and not top:
        strock += 1
        top = True


