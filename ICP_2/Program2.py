step = 0
a = int(input("enter number:"))
while a != 0:
    if (a % 2) == 0:
        a = a/2
        step = step + 1
    else:
        a = a - 1
        step = step + 1
print(step)