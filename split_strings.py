def solution(s):
    list1 = []
    if len(s) % 2 != 0:
        s = s + "_"
    for i in range(1, len(s)):
        if (i+1) % 2 == 0:
            list1.append(s[i-1] + s[i])

    return list1
