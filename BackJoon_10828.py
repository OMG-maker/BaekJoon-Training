import sys

s = []
size = int(sys.stdin.readline())
for _ in range(size):
    # sys.stdin.readline()로 문자열을 입력받을 때엔 .strip()를 뒤에 추가해줘야 개행문자가 들어오지 않는다.
    do = sys.stdin.readline().strip()

    if "push" in do:
        s.append(do.split()[1])
    elif do == "pop":
        if len(s) > 0:
            print(s.pop(-1))
        else:
            print(-1)
    elif do == "size":
        print(len(s))
    elif do == "empty":
        if len(s) == 0:
            print(1)
        else:
            print(0)
    elif do == "top":
        if len(s) > 0:
            print(s[len(s) - 1])
        else:
            print(-1)
    else:
        print("예기치 못한 오류 - else")