ma = 0
for i in range(100, 1000):
    for j in range(100, 1000):
        ij = i * j
        if str(ij) == str(ij)[::-1] and ij > ma:
            ma = ij

print(ma)
