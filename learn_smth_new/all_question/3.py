# получить число впадин (<0) если на вход подается массив типа [U,D,D,U,D,U]б где U = +1; D = -1
li = ["D", "D", "U", "D", "U", "U"]


def count(li: list):
    res = 0
    prev, cur = 0, 0
    for i in li:
        if i == 'U':
            prev, cur = cur, cur + 1
        else:
            prev, cur = cur, cur - 1
        if prev == 0 and cur < 0:
           res += 1
    return res

print(count(li))