n = 70
steps = 0
while n != 1:
    print(n)
    steps += 1
    if n % 2 == 0:
        n = n//2
    else:
        n = 3*n + 1
print("steps=", steps)