n = int(input())
k = int(input())
cnt = 1
if k == n:
    print(cnt, k)
k -= n
if k >= 0:
    cnt = 2
    while k > 0:
        if cnt % 2 == 0:
           k = k - (n + 1)
        else:
           k -= n
        if k > 0:
            cnt += 1
        else:
            break
if k < 0:
    if cnt % 2 == 0:
        k = k + n + 1
    else:
        k += n
    print(cnt, k)
elif k > 0:
    print(cnt, k)
