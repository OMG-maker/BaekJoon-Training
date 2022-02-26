import sys

A = int(sys.stdin.readline())

result = ''
while A > 0:
    result = str(A % 2) + result
    A //= 2

count = 0
for i in range(len(result)):
    if result[i] == '1':
        count += 1

print(count)
