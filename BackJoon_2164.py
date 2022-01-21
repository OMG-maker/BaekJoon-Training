import sys
from collections import deque


def solution():
    q = deque()
    size = int(sys.stdin.readline())
    if size == 1:
        return 1

    for i in range(1, size + 1):
        q.append(i)

    while True:
        q.popleft()
        if len(q) == 1:
            return q.popleft()
        q.append(q.popleft())


print(solution())