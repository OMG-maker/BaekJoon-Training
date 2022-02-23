import sys
import heapq
pq = []

N = int(sys.stdin.readline())

for i in range(N):
    term = int(sys.stdin.readline())
    if term == 0:
        if len(pq) != 0:
            print(heapq.heappop(pq))
        else:
            print(0)
    else:
        heapq.heappush(pq, term)

# heapq.heappush(heap, (-num, num))  # (우선 순위, 값)

# heapq.heappush(pq, 12)
# heapq.heappush(pq, 789)
# heapq.heappush(pq, 231)
# print("size: ", len(pq))
# # 12 231 789
# while len(pq) > 0:
#     print(heapq.heappop(pq))
''''''''''''''''''''''''''' 혹은
while len(pq) > 0:
    print(pq[0])
    heapq.heappop(pq)
'''''''''''''''''''''''''''