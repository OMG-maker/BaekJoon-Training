import sys

N = int(sys.stdin.readline())

cache = [[-1] * 10 for i in range(N)]
cache[0][0] = 0

for i in range(1, 10):
    cache[0][i] = 1

for i in range(1, N):
    for j in range(10):
        if j == 0:
            cache[i][j] = cache[i - 1][j + 1]
        elif j == 9:
            cache[i][j] = cache[i - 1][j - 1]
        else:
            cache[i][j] = cache[i-1][j-1] + cache[i-1][j+1]


print((sum(cache[N-1])) % 1000000000)