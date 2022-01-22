import sys
import heapq as hq

pq1 = []
pq2 = []

size = int(sys.stdin.readline())

for i in range(size):
    a = int(sys.stdin.readline())

    if a < 0:
        hq.heappush(pq1, -a)
    elif a > 0:
        hq.heappush(pq2, a)
    else:
        if not pq1:
            if not pq2:
                print(0)
            else:
                print(hq.heappop(pq2))
        elif not pq2:
            print(-hq.heappop(pq1))
        else:
            p1 = hq.heappop(pq1)
            p2 = hq.heappop(pq2)
            if p1 > p2:
                print(p2)
                hq.heappush(pq1, p1)
            else:
                print(-p1)
                hq.heappush(pq2, p2)