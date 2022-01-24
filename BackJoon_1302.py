import sys

dict1 = dict()
size = int(sys.stdin.readline())

for _ in range(size):
    term = sys.stdin.readline().strip()

    if dict1.get(term):
        dict1[term] += 1
    else:
        dict1[term] = 1

max_key = ''
max_count = -1
for key, value in dict1.items():
    if max_count == -1:
        max_key = key
        max_count = value
    elif max_count <= value and max_key > key:
        max_key = key
        max_count = value

print(max_key)
