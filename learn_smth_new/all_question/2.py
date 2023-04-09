#есть словарь (ключ: число), надо вернуть 2 ключа с самыми болльшими чсилами

d = {'a': 34, 'b': 66, 'c': 12, 'd': 9000}

def check(d: dict):
    ma_1, ma_2 = None, None

    for i in d.keys():
        if ma_1 is None:
            ma_1 = i
        elif ma_2 is None:
            if(d[i] > d[ma_1]):
                ma_1, ma_2 = i, ma_1
            else:
                ma_2 = i
        else:
            if d[i] > d[ma_2]:
                if d[i] > d[ma_1]:
                    ma_1, ma_2 = i, ma_1
                else:
                    ma_2 = i
    return ma_1, ma_2


print(check(d))


def another_solution(d: dict):
    keys = sorted(d.items(), key=lambda x:x[1], reverse=True)
    return keys[0][0], keys[1][0]


print(another_solution(d))