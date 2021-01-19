a = int(input())
b = int(input())
myset1 = {""}
myset2 = {""}
for i in range(a):
    myset1.add(input())
for i in range(b):
    myset2.add(input())
myset1.remove("")
myset2.remove("")
if myset1.isdisjoint(myset2):
    print("NO")
else:
    print(len(myset1.symmetric_difference(myset2)))