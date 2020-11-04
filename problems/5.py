def prime_factorization(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors


A = [[0] * 21 for j in range(21)]

for i in range(1, 21):
    for j in prime_factorization(i):
        A[i][j] += 1

ans = 1
for i, a in enumerate(zip(*A)):
    ans *= i ** max(a)

print(ans)
