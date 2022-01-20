import sys

def solution():
    s = sys.stdin.readline().strip()
    result = 0

    for i in range(len(s)):
        if s[i] == "(":
            result = result + 1
        elif s[i] == ")":
            result = result - 1
            if result < 0:
                return 1
        else:
            return 0

    if result == 0:
        return 0
    else:
        return 1

s = []
size = int(sys.stdin.readline())
for _ in range(size):
    r = solution()
    if r == 1:
        print("NO")
    else:
        print("YES")
