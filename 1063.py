import sys

# T = int(sys.stdin.readline())
# arr = list(map(int, sys.stdin.readline().split()))
# board = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]
X, Y, N = map(str, sys.stdin.readline().split())

K1 = ord(X[0]) - 65
K2 = int(X[1])
S1 = ord(Y[0]) - 65
S2 = int(Y[1])

def stone_move(do):
    global K1, K2, S1, S2
    if do == "R":
        if S1 == K1 + 1 and S2 == K2:
            if S1 + 1 < 8:
                S1 += 1
                return True
            else:
                return False
        else:
            return True
    elif do == "L":
        if S1 == K1 - 1 and S2 == K2:
            if S1 - 1 > -1:
                S1 -= 1
                return True
            else:
                return False
        else:
            return True
    elif do == "B":
        if S1 == K1 and S2 == K2 - 1:
            if S2 - 1 > 0:
                S2 -= 1
                return True
            else:
                return False
        else:
            return True
    elif do == "T":
        if S1 == K1 and S2 == K2 + 1:
            if S2 + 1 < 9:
                S2 += 1
                return True
            else:
                return False
        else:
            return True
    elif do == "RT":
        if S1 == K1 + 1 and S2 == K2 + 1:
            if S1 + 1 < 8 and S2 + 1 < 9:
                S1 += 1
                S2 += 1
                return True
            else:
                return False
        else:
            return True
    elif do == "LT":
        if S1 == K1 - 1 and S2 == K2 + 1:
            if S1 - 1 > -1 and S2 + 1 < 9:
                S1 -= 1
                S2 += 1
                return True
            else:
                return False
        else:
            return True
    elif do == "RB":
        if S1 == K1 + 1 and S2 == K2 - 1:
            if S1 + 1 < 8 and S2 - 1 > 0:
                S1 += 1
                S2 -= 1
                return True
            else:
                return False
        else:
            return True
    elif do == "LB":
        if S1 == K1 - 1 and S2 == K2 - 1:
            if S1 - 1 > -1 and S2 - 1 > 0:
                S1 -= 1
                S2 -= 1
                return True
            else:
                return False
        else:
            return True


for _ in range(int(N)):
    # sys.stdin.readline()로 문자열을 입력받을 때엔 .strip()를 뒤에 추가해줘야 개행문자가 들어오지 않는다.
    do = input()

    if do == "R":
        if stone_move(do):
            if K1 + 1 < 8:
                K1 += 1
        else:
            continue
    elif do == "L":
        if stone_move(do):
            if K1 - 1 > -1:
                K1 -= 1
        else:
            continue
    elif do == "B":
        if stone_move(do):
            if K2 - 1 > 0:
                K2 -= 1
        else:
            continue
    elif do == "T":
        if stone_move(do):
            if K2 + 1 < 9:
                K2 += 1
        else:
            continue
    elif do == "RT":
        if stone_move(do):
            if K1 + 1 < 8 and K2 + 1 < 9:
                K1 += 1
                K2 += 1
        else:
            continue
    elif do == "LT":
        if stone_move(do):
            if K1 - 1 > -1 and K2 + 1 < 9:
                K1 -= 1
                K2 += 1
        else:
            continue
    elif do == "RB":
        if stone_move(do):
            if K1 + 1 < 8 and K2 - 1 > 0:
                K1 += 1
                K2 -= 1
        else:
            continue
    elif do == "LB":
        if stone_move(do):
            if K1 - 1 > -1 and K2 - 1 > -0:
                K1 -= 1
                K2 -= 1
        else:
            continue

result1 = chr(K1 + 65) + str(K2)
result2 = chr(S1 + 65) + str(S2)

print(result1)
print(result2)
