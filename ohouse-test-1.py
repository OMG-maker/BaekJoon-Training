r = [["b", "a", "a", "d"], ["b", "c", "a", "c"], ["b", "a", "d", "c"]]
# r = [["b", "a", "d", "c"],["b", "a", "c", "d"]]


def solution(rounds):
    answer = -1
    answer += 1

    count = [0, 0, 0, 0]

    player = ["a", "b", "c", "d"]
    last_c = ["", "", "", ""]

    for r1 in rounds:
        p = [False, False, False, False]

        for i in range(4):
            if r1[i] == player[i]:
                count[i] += 1
                p[i] = True
            else:
                if r1[i] == last_c[i]:
                    count[i] += 1
                    p[i] = True

        for i in range(4):
            count2 = 0
            if not p[i]:
                j = player.index(r1[i])
                if not p[j] and player[i] == r1[j]:
                    last_c[i] = r1[i]
                    last_c[j] = r1[j]
                    count2 += 1

            if count2 == 0:
                last_c[i] = ""

    answer = sum(count)
    return answer


print(solution(r))