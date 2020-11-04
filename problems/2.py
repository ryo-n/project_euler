
a = 1
b = 2
c = a + b

ans = b
while c <= 4000000:
    a, b, c = b, c,  b + c,
    if c % 2 == 0:
        ans += c

print(ans)

